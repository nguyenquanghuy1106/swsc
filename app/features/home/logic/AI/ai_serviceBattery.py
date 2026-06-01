import os
import torch
from PIL import Image
from torchvision import models, transforms


CLASS_NAMES = [
    "battery",
    "biological",
    "cardboard",
    "clothes",
    "glass",
    "metal",
    "paper",
    "plastic",
    "shoes",
    "trash",
]

ALLOWED_CLASSES = {
    "battery": "Pin / Ắc quy"
}

_MODEL = None

_TRANSFORM = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])


def _get_model():
    global _MODEL

    if _MODEL is not None:
        return _MODEL

    model = models.mobilenet_v2(weights=None)
    model.classifier[1] = torch.nn.Linear(model.last_channel, len(CLASS_NAMES))

    base_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "..")
    )

    model_path = os.path.join(base_dir, "models", "best_model.pth")

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Không tìm thấy model tại: {model_path}")

    state_dict = torch.load(model_path, map_location="cpu")
    model.load_state_dict(state_dict)
    model.eval()

    _MODEL = model
    return _MODEL


def predict_battery_image(image: Image.Image):
    if image.mode != "RGB":
        image = image.convert("RGB")

    tensor = _TRANSFORM(image).unsqueeze(0)
    model = _get_model()

    with torch.no_grad():
        outputs = model(tensor)
        probabilities = torch.softmax(outputs, dim=1)[0]

    confidence, predicted_idx = torch.max(probabilities, dim=0)

    predicted_class = CLASS_NAMES[predicted_idx.item()]
    confidence_score = confidence.item() * 100

    battery_rate = round(
        probabilities[CLASS_NAMES.index("battery")].item() * 100,
        2
    )

    if predicted_class != "battery":
        return {
            "success": False,
            "message": (
                f"Ảnh này được AI dự đoán là '{predicted_class}', "
                "không thuộc nhóm battery được phép."
            ),
            "predicted_class": predicted_class,
            "confidence": round(confidence_score, 2),
            "battery_rate": battery_rate,
        }

    return {
        "success": True,
        "message": "Nhận diện thành công.",
        "predicted_class": predicted_class,
        "display_name": ALLOWED_CLASSES[predicted_class],
        "confidence": round(confidence_score, 2),
        "battery_rate": battery_rate,
    }