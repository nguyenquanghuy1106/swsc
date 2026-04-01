import torch
from torchvision import models, transforms
from PIL import Image

# 1. Class names (phải đúng thứ tự)
class_names = ['battery', 'biological', 'cardboard', 'clothes', 'glass',
               'metal', 'paper', 'plastic', 'shoes', 'trash']

# 2. Load model
model = models.mobilenet_v2(weights=None)
model.classifier[1] = torch.nn.Linear(model.last_channel, len(class_names))

model.load_state_dict(torch.load("best_model.pth", map_location="cpu"))
model.eval()

# 3. Transform giống lúc train
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# 4. Load ảnh
image_path = "test.jpg"  # đổi ảnh bạn muốn test
image = Image.open(image_path).convert("RGB")
image = transform(image).unsqueeze(0)

# 5. Predict
with torch.no_grad():
    outputs = model(image)
    predicted = outputs.argmax(1).item()

# 6. In kết quả
print("Dự đoán:", class_names[predicted])