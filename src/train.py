import copy
import json
from pathlib import Path

import torch
from torch import nn, optim
from torch.utils.data import DataLoader, random_split
from torchvision import datasets, transforms, models

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay


# ===================== CẤU HÌNH =====================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "datasets" / "standardized_256"
MODEL_DIR = BASE_DIR / "models"
REPORT_DIR = BASE_DIR / "reports" / "model_metrics" / "mobilenetv2"

MODEL_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

MODEL_PATH = MODEL_DIR / "best_mobilenetv2.pth"
CLASS_NAMES_PATH = MODEL_DIR / "mobilenetv2_class_names.json"

BATCH_SIZE = 64
TRAIN_RATIO = 0.8
VAL_RATIO = 0.1
TEST_RATIO = 0.1
NUM_EPOCHS = 20
PATIENCE = 5
LEARNING_RATE = 0.001
IMG_SIZE = 224
SEED = 42

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("Device:", device)
print("DATA_DIR:", DATA_DIR)
print("MODEL_PATH:", MODEL_PATH)
print("REPORT_DIR:", REPORT_DIR)

if not DATA_DIR.exists():
    raise FileNotFoundError(f"Không tìm thấy dataset tại: {DATA_DIR}")


# ===================== HÀM LƯU BẢNG DẠNG ẢNH =====================

def save_table_image(df, title, save_path):
    fig_height = max(3, len(df) * 0.55)

    fig, ax = plt.subplots(figsize=(13, fig_height))
    ax.axis("off")

    table = ax.table(
        cellText=df.values,
        colLabels=df.columns,
        cellLoc="center",
        loc="center"
    )

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.7)

    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_text_props(weight="bold")

    plt.title(title, fontsize=15, fontweight="bold", pad=20)
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()

    print("Đã lưu:", save_path)


# ===================== DATASET =====================

transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

full_dataset = datasets.ImageFolder(DATA_DIR, transform=transform)

class_names = full_dataset.classes
num_classes = len(class_names)
total_size = len(full_dataset)

print("Classes:", class_names)
print("Tổng số ảnh:", total_size)

with open(CLASS_NAMES_PATH, "w", encoding="utf-8") as f:
    json.dump(class_names, f, ensure_ascii=False, indent=2)

train_size = int(TRAIN_RATIO * total_size)
val_size = int(VAL_RATIO * total_size)
test_size = total_size - train_size - val_size

generator = torch.Generator().manual_seed(SEED)

train_dataset, val_dataset, test_dataset = random_split(
    full_dataset,
    [train_size, val_size, test_size],
    generator=generator
)

print("Train:", len(train_dataset))
print("Validation:", len(val_dataset))
print("Test:", len(test_dataset))

train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False)
test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)


# ===================== BẢNG DATASET =====================

dataset_split_df = pd.DataFrame([
    ["Train", len(train_dataset), "80%"],
    ["Validation", len(val_dataset), "10%"],
    ["Test", len(test_dataset), "10%"],
    ["Tổng", total_size, "100%"],
], columns=["Tập dữ liệu", "Số lượng ảnh", "Tỷ lệ"])

dataset_split_df.to_csv(
    REPORT_DIR / "dataset_split.csv",
    index=False,
    encoding="utf-8-sig"
)

save_table_image(
    dataset_split_df,
    "Bảng. Phân chia tập dữ liệu MobileNetV2",
    REPORT_DIR / "01_mobilenetv2_dataset_split.png"
)

class_rows = []

for class_dir in sorted(DATA_DIR.iterdir()):
    if class_dir.is_dir():
        image_count = len([
            p for p in class_dir.iterdir()
            if p.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp", ".webp"]
        ])
        class_rows.append([class_dir.name, image_count])

class_distribution_df = pd.DataFrame(
    class_rows,
    columns=["Lớp dữ liệu", "Số lượng ảnh"]
)

class_distribution_df.to_csv(
    REPORT_DIR / "class_distribution.csv",
    index=False,
    encoding="utf-8-sig"
)

save_table_image(
    class_distribution_df,
    "Bảng. Phân bố dữ liệu theo lớp",
    REPORT_DIR / "02_mobilenetv2_class_distribution.png"
)


# ===================== BẢNG CẤU HÌNH =====================

config_df = pd.DataFrame([
    ["Model", "MobileNetV2"],
    ["Chức năng sử dụng", "Upload ảnh"],
    ["Framework", "PyTorch / Torchvision"],
    ["Input Size", "224×224"],
    ["Batch Size", BATCH_SIZE],
    ["Epoch tối đa", NUM_EPOCHS],
    ["Early Stopping Patience", PATIENCE],
    ["Learning Rate", LEARNING_RATE],
    ["Optimizer", "Adam"],
    ["Loss Function", "CrossEntropyLoss"],
    ["Transfer Learning", "Có"],
    ["Pretrained Weight", "ImageNet"],
    ["Fine-tuning", "Không"],
    ["Output Model", MODEL_PATH.name],
], columns=["Thông số", "Giá trị"])

config_df.to_csv(
    REPORT_DIR / "mobilenetv2_config.csv",
    index=False,
    encoding="utf-8-sig"
)

save_table_image(
    config_df,
    "Bảng. Cấu hình huấn luyện MobileNetV2",
    REPORT_DIR / "03_mobilenetv2_config.png"
)


# ===================== MODEL =====================

model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT)

for param in model.features.parameters():
    param.requires_grad = False

model.classifier[1] = nn.Linear(model.last_channel, num_classes)
model = model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.classifier.parameters(), lr=LEARNING_RATE)

print("Model MobileNetV2 đã sẵn sàng.")


# ===================== TRAIN / EVALUATE =====================

def train_one_epoch(model, loader):
    model.train()

    running_loss = 0.0
    running_correct = 0

    for batch_idx, (images, labels) in enumerate(loader):
        print(f"Train Batch {batch_idx + 1}/{len(loader)}", end="\r")

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


def evaluate(model, loader):
    model.eval()

    running_loss = 0.0
    running_correct = 0

    y_true = []
    y_pred = []

    with torch.no_grad():
        for batch_idx, (images, labels) in enumerate(loader):
            print(f"Eval Batch {batch_idx + 1}/{len(loader)}", end="\r")

            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)
            loss = criterion(outputs, labels)

            running_loss += loss.item() * images.size(0)

            preds = outputs.argmax(dim=1)
            running_correct += (preds == labels).sum().item()

            y_true.extend(labels.cpu().numpy())
            y_pred.extend(preds.cpu().numpy())

    epoch_loss = running_loss / len(loader.dataset)
    epoch_acc = running_correct / len(loader.dataset)

    return epoch_loss, epoch_acc, y_true, y_pred


# ===================== VÒNG LẶP TRAIN =====================

history = []

best_val_acc = 0.0
best_model_wts = copy.deepcopy(model.state_dict())
early_stop_counter = 0

for epoch in range(NUM_EPOCHS):
    print("\n" + "=" * 60)
    print(f"Epoch {epoch + 1}/{NUM_EPOCHS}")
    print("=" * 60)

    train_loss, train_acc = train_one_epoch(model, train_loader)
    val_loss, val_acc, _, _ = evaluate(model, val_loader)

    history.append({
        "Epoch": epoch + 1,
        "Train Loss": round(train_loss, 4),
        "Train Accuracy": round(train_acc, 4),
        "Validation Loss": round(val_loss, 4),
        "Validation Accuracy": round(val_acc, 4),
    })

    print()
    print(f"Train Loss: {train_loss:.4f} | Train Acc: {train_acc:.4f}")
    print(f"Val   Loss: {val_loss:.4f} | Val   Acc: {val_acc:.4f}")

    if val_acc > best_val_acc:
        best_val_acc = val_acc
        best_model_wts = copy.deepcopy(model.state_dict())

        torch.save(model.state_dict(), MODEL_PATH)

        early_stop_counter = 0

        print(f">> Đã lưu model tốt nhất. Val Acc = {val_acc:.4f}")

    else:
        early_stop_counter += 1

        print(f">> Không cải thiện ({early_stop_counter}/{PATIENCE})")

        if early_stop_counter >= PATIENCE:
            print("Early Stopping Activated!")
            print(f"Dừng train tại Epoch {epoch + 1}")
            break


# ===================== LOAD BEST MODEL =====================

model.load_state_dict(best_model_wts)

print("\n" + "=" * 60)
print("LOAD BEST MODEL")
print("=" * 60)
print(f"Best Validation Accuracy: {best_val_acc:.4f}")


# ===================== ĐÁNH GIÁ TEST =====================

test_loss, test_acc, y_true, y_pred = evaluate(model, test_loader)

print()
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_acc:.4f}")


# ===================== LƯU BẢNG HISTORY =====================

history_df = pd.DataFrame(history)

history_df.to_csv(
    REPORT_DIR / "mobilenetv2_training_history.csv",
    index=False,
    encoding="utf-8-sig"
)

save_table_image(
    history_df,
    "Bảng. Kết quả Train/Validation MobileNetV2 theo từng Epoch",
    REPORT_DIR / "04_mobilenetv2_train_val_history.png"
)


# ===================== BIỂU ĐỒ ACC / LOSS =====================

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(
    history_df["Epoch"],
    history_df["Train Accuracy"],
    marker="o",
    label="Train Accuracy"
)
plt.plot(
    history_df["Epoch"],
    history_df["Validation Accuracy"],
    marker="o",
    label="Validation Accuracy"
)
plt.title("MobileNetV2 - Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(
    history_df["Epoch"],
    history_df["Train Loss"],
    marker="o",
    label="Train Loss"
)
plt.plot(
    history_df["Epoch"],
    history_df["Validation Loss"],
    marker="o",
    label="Validation Loss"
)
plt.title("MobileNetV2 - Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig(
    REPORT_DIR / "05_mobilenetv2_accuracy_loss_curve.png",
    dpi=300
)
plt.close()

print("Đã lưu biểu đồ Accuracy/Loss.")


# ===================== BẢNG TEST RESULT =====================

result_df = pd.DataFrame([
    ["Best Validation Accuracy", round(best_val_acc, 4)],
    ["Test Accuracy", round(test_acc, 4)],
    ["Test Loss", round(test_loss, 4)],
], columns=["Metric", "Value"])

result_df.to_csv(
    REPORT_DIR / "mobilenetv2_test_result.csv",
    index=False,
    encoding="utf-8-sig"
)

save_table_image(
    result_df,
    "Bảng. Kết quả đánh giá MobileNetV2 trên tập Test",
    REPORT_DIR / "06_mobilenetv2_test_result.png"
)


# ===================== CLASSIFICATION REPORT =====================

report_dict = classification_report(
    y_true,
    y_pred,
    target_names=class_names,
    output_dict=True,
    zero_division=0
)

report_df = pd.DataFrame(report_dict).transpose()
report_df = report_df.round(4)

report_df.to_csv(
    REPORT_DIR / "mobilenetv2_classification_report.csv",
    encoding="utf-8-sig"
)

report_image_df = report_df.reset_index().rename(columns={"index": "Class"})

save_table_image(
    report_image_df,
    "Bảng. Classification Report MobileNetV2",
    REPORT_DIR / "07_mobilenetv2_classification_report.png"
)


# ===================== CONFUSION MATRIX =====================

cm = confusion_matrix(y_true, y_pred)

fig, ax = plt.subplots(figsize=(12, 10))

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=class_names
)

disp.plot(
    ax=ax,
    xticks_rotation=45,
    values_format="d"
)

plt.title("Confusion Matrix - MobileNetV2")
plt.tight_layout()
plt.savefig(
    REPORT_DIR / "08_mobilenetv2_confusion_matrix.png",
    dpi=300
)
plt.close()

print("Đã lưu Confusion Matrix.")


# ===================== LƯU TỔNG KẾT JSON =====================

summary = {
    "model": "MobileNetV2",
    "framework": "PyTorch",
    "input_size": IMG_SIZE,
    "batch_size": BATCH_SIZE,
    "max_epochs": NUM_EPOCHS,
    "actual_epochs": len(history_df),
    "learning_rate": LEARNING_RATE,
    "best_val_accuracy": round(best_val_acc, 4),
    "test_loss": round(test_loss, 4),
    "test_accuracy": round(test_acc, 4),
    "model_path": str(MODEL_PATH),
    "report_dir": str(REPORT_DIR),
    "classes": class_names
}

with open(REPORT_DIR / "mobilenetv2_summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)


print("\n" + "=" * 60)
print("HOÀN TẤT TRAIN MOBILENETV2")
print("=" * 60)
print("Model lưu tại:", MODEL_PATH)
print("Class names lưu tại:", CLASS_NAMES_PATH)
print("Bảng ảnh và biểu đồ lưu tại:", REPORT_DIR)