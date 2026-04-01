# Kết nối với DATASETS
# import torch
# from torch import nn, optim
# from torch.utils.data import DataLoader, random_split
# from torchvision import datasets, transforms, models

# # 1. Cấu hình
# DATA_DIR = "datasets/standardized_256"
# BATCH_SIZE = 32
# TRAIN_RATIO = 0.8
# VAL_RATIO = 0.1
# TEST_RATIO = 0.1

# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# print("Device:", device)

# # 2. Transform ảnh
# transform = transforms.Compose([
#     transforms.Resize((224, 224)),
#     transforms.ToTensor(),
# ])

# # 3. Load dataset
# full_dataset = datasets.ImageFolder(DATA_DIR, transform=transform)

# print("Classes:", full_dataset.classes)
# print("Tổng số ảnh:", len(full_dataset))

# # 4. Chia dataset
# total_size = len(full_dataset)
# train_size = int(TRAIN_RATIO * total_size)
# val_size = int(VAL_RATIO * total_size)
# test_size = total_size - train_size - val_size

# train_dataset, val_dataset, test_dataset = random_split(
#     full_dataset, [train_size, val_size, test_size]
# )

# print("Train:", len(train_dataset))
# print("Val:", len(val_dataset))
# print("Test:", len(test_dataset))

# # 5. DataLoader
# train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
# val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False)
# test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)

# # 6. Load model có sẵn
# model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT)

# # Đóng băng phần trích xuất đặc trưng
# for param in model.features.parameters():
#     param.requires_grad = False

# # Thay lớp cuối cho đúng số class
# num_classes = len(full_dataset.classes)
# model.classifier[1] = nn.Linear(model.last_channel, num_classes)

# model = model.to(device)

# print("Model đã sẵn sàng.")
# print(model.classifier);

import copy
import torch
from torch import nn, optim
# optim thuật toán Adam ,SDG
from torch.utils.data import DataLoader, random_split
# DataLoader để load dữ liệu, random_split để chia dữ liệu train/val/test
from torchvision import datasets, transforms, models
# datasets để load dataset, transforms để biến đổi ảnh, models để load model có sẵn

# 1. Cấu hình
DATA_DIR = "datasets/standardized_256"
BATCH_SIZE = 32
# một lần Train sẽ lấy 32 ảnh, nếu có 1000 ảnh thì sẽ có 1000/32 = 31.25 -> 32 lần train
TRAIN_RATIO = 0.8
VAL_RATIO = 0.1
TEST_RATIO = 0.1
NUM_EPOCHS = 5
# train 5 lần qua toàn bộ dữ liệu, mỗi lần gọi là 1 epoch
LEARNING_RATE = 0.001
MODEL_PATH = "best_model.pth"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Device:", device)

# 2. Transform ảnh
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    # resize ảnh về 224x224 để phù hợp với input của MobileNetV2
    transforms.ToTensor(),
])

# 3. Load dataset
full_dataset = datasets.ImageFolder(DATA_DIR, transform=transform)

print("Classes:", full_dataset.classes)
print("Tổng số ảnh:", len(full_dataset))

# 4. Chia dataset
total_size = len(full_dataset)
train_size = int(TRAIN_RATIO * total_size)
val_size = int(VAL_RATIO * total_size)
test_size = total_size - train_size - val_size

train_dataset, val_dataset, test_dataset = random_split(
    full_dataset, [train_size, val_size, test_size]
)

print("Train:", len(train_dataset))
print("Val:", len(val_dataset))
print("Test:", len(test_dataset))

# 5. DataLoader
train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False)
test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)

# 6. Load model có sẵn
model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT)

for param in model.features.parameters():
    param.requires_grad = False

num_classes = len(full_dataset.classes)
model.classifier[1] = nn.Linear(model.last_channel, num_classes)
model = model.to(device)

print("Model đã sẵn sàng.")

# 7. Loss và optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.classifier.parameters(), lr=LEARNING_RATE)

# 8. Hàm train 1 epoch
def train_one_epoch(model, loader, criterion, optimizer):
    model.train()
    running_loss = 0.0
    running_correct = 0

    for images, labels in loader:
        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * images.size(0)
        preds = outputs.argmax(dim=1)
        running_correct += (preds == labels).sum().item()

    epoch_loss = running_loss / len(loader.dataset)
    epoch_acc = running_correct / len(loader.dataset)
    return epoch_loss, epoch_acc

# 9. Hàm evaluate
def evaluate(model, loader, criterion):
    model.eval()
    running_loss = 0.0
    running_correct = 0

    with torch.no_grad():
        for images, labels in loader:
            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)
            loss = criterion(outputs, labels)

            running_loss += loss.item() * images.size(0)
            preds = outputs.argmax(dim=1)
            running_correct += (preds == labels).sum().item()

    epoch_loss = running_loss / len(loader.dataset)
    epoch_acc = running_correct / len(loader.dataset)
    return epoch_loss, epoch_acc

# 10. Vòng lặp train
best_val_acc = 0.0
best_model_wts = copy.deepcopy(model.state_dict())

for epoch in range(NUM_EPOCHS):
    print(f"\nEpoch {epoch+1}/{NUM_EPOCHS}")

    train_loss, train_acc = train_one_epoch(model, train_loader, criterion, optimizer)
    val_loss, val_acc = evaluate(model, val_loader, criterion)

    print(f"Train Loss: {train_loss:.4f} | Train Acc: {train_acc:.4f}")
    print(f"Val   Loss: {val_loss:.4f} | Val   Acc: {val_acc:.4f}")

    if val_acc > best_val_acc:
        best_val_acc = val_acc
        best_model_wts = copy.deepcopy(model.state_dict())
        torch.save(model.state_dict(), MODEL_PATH)
        print(">> Đã lưu model tốt nhất.")

# 11. Load lại model tốt nhất
model.load_state_dict(best_model_wts)

# 12. Đánh giá trên test
test_loss, test_acc = evaluate(model, test_loader, criterion)
print(f"\nTest Loss: {test_loss:.4f} | Test Acc: {test_acc:.4f}")

print(f"Model tốt nhất đã lưu tại: {MODEL_PATH}")