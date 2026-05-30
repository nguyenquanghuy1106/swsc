"""
Dự đoán một ảnh đơn bằng model đã train.

Chạy:
    python src/predict_image.py path/to/image.jpg
"""

from pathlib import Path
import sys
import json
import cv2
import numpy as np
import tensorflow as tf

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "waste_efficientnet.keras"
CLASS_PATH = BASE_DIR / "models" / "class_names.json"
IMG_SIZE = (224, 224)

if len(sys.argv) < 2:
    raise SystemExit("Cách chạy: python src/predict_image.py path/to/image.jpg")

image_path = Path(sys.argv[1])
if not image_path.exists():
    raise FileNotFoundError(image_path)

model = tf.keras.models.load_model(MODEL_PATH)
with open(CLASS_PATH, "r", encoding="utf-8") as f:
    class_names = json.load(f)

img_bgr = cv2.imread(str(image_path))
if img_bgr is None:
    raise ValueError(f"Không đọc được ảnh: {image_path}")

img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
img_rgb = cv2.resize(img_rgb, IMG_SIZE).astype(np.float32)
x = np.expand_dims(img_rgb, axis=0)

pred = model.predict(x, verbose=0)[0]
top_idx = pred.argsort()[-5:][::-1]

print("Kết quả dự đoán:")
for i in top_idx:
    print(f"{class_names[int(i)]}: {pred[int(i)] * 100:.2f}%")
