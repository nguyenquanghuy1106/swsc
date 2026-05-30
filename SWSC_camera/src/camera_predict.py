"""
Quét camera realtime bằng model EfficientNet đã train.

Bản này:
- AUTO tự bám theo vật.
- Lọc bớt người bằng cách bỏ contour quá lớn/quá cao/quá rộng.
- Nhấn C đổi mode: AUTO / CENTER / FULL_FRAME.
- Nhấn R reset background.
- Nhấn Q thoát.
"""

from pathlib import Path
from collections import deque
import json
import time
import cv2
import numpy as np
import tensorflow as tf

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "waste_efficientnet.keras"
CLASS_PATH = BASE_DIR / "models" / "class_names.json"
CAPTURE_DIR = BASE_DIR / "captured_frames"
CAPTURE_DIR.mkdir(exist_ok=True)

CAMERA_INDEX = 0

CONF_THRESHOLD = 0.55
SMOOTH_FRAMES = 10
ROI_SCALE = 0.70
PADDING = 0.18

MIN_OBJECT_AREA_RATIO = 0.025
MAX_OBJECT_AREA_RATIO = 0.35
MAX_OBJECT_HEIGHT_RATIO = 0.75
MAX_OBJECT_WIDTH_RATIO = 0.80
MIN_ASPECT_RATIO = 0.25
MAX_ASPECT_RATIO = 3.2

ROI_MODES = ["AUTO_ROI", "CENTER_ROI", "FULL_FRAME"]
roi_mode_index = 0

if not MODEL_PATH.exists():
    raise FileNotFoundError(
        f"Không thấy model: {MODEL_PATH}\n"
        "Hãy train trước bằng lệnh: python src/train_efficientnet.py"
    )

model = tf.keras.models.load_model(MODEL_PATH)

with open(CLASS_PATH, "r", encoding="utf-8") as f:
    class_names = json.load(f)

_, input_h, input_w, _ = model.input_shape
IMG_SIZE = (input_w, input_h)

bg_subtractor = cv2.createBackgroundSubtractorMOG2(
    history=300,
    varThreshold=28,
    detectShadows=True,
)

pred_history = deque(maxlen=SMOOTH_FRAMES)
box_history = deque(maxlen=5)
last_good_box = None


def crop_center_roi(frame, scale=0.70):
    h, w = frame.shape[:2]
    side = int(min(h, w) * scale)

    x1 = (w - side) // 2
    y1 = (h - side) // 2
    x2 = x1 + side
    y2 = y1 + side

    return frame[y1:y2, x1:x2], (x1, y1, x2, y2)


def expand_box(box, frame_shape, padding=0.18):
    x1, y1, x2, y2 = box
    h, w = frame_shape[:2]

    bw = x2 - x1
    bh = y2 - y1

    pad_x = int(bw * padding)
    pad_y = int(bh * padding)

    x1 = max(0, x1 - pad_x)
    y1 = max(0, y1 - pad_y)
    x2 = min(w, x2 + pad_x)
    y2 = min(h, y2 + pad_y)

    return x1, y1, x2, y2


def smooth_box(box):
    box_history.append(box)
    arr = np.array(box_history, dtype=np.float32)
    smoothed = np.mean(arr, axis=0).astype(int)
    return tuple(smoothed.tolist())


def is_valid_object_contour(cnt, frame_shape, min_area):
    h, w = frame_shape[:2]

    area = cv2.contourArea(cnt)
    x, y, bw, bh = cv2.boundingRect(cnt)

    if area < min_area:
        return False

    area_ratio = area / (h * w)
    height_ratio = bh / h
    width_ratio = bw / w
    aspect_ratio = bw / max(1, bh)

    # Bỏ vùng quá lớn: thường là người hoặc thân người
    if area_ratio > MAX_OBJECT_AREA_RATIO:
        return False

    # Bỏ vùng quá cao: thường là người đứng trước camera
    if height_ratio > MAX_OBJECT_HEIGHT_RATIO:
        return False

    # Bỏ vùng quá rộng: thường là nền/người chiếm nhiều khung hình
    if width_ratio > MAX_OBJECT_WIDTH_RATIO:
        return False

    # Bỏ box quá dọc hoặc quá ngang bất thường
    if aspect_ratio < MIN_ASPECT_RATIO or aspect_ratio > MAX_ASPECT_RATIO:
        return False

    # Bỏ vùng chạm mép trên nhiều: thường là đầu/thân người
    if y < int(h * 0.05) and bh > int(h * 0.35):
        return False

    return True


def find_object_roi(frame):
    global last_good_box

    h, w = frame.shape[:2]
    min_area = h * w * MIN_OBJECT_AREA_RATIO

    fg = bg_subtractor.apply(frame)

    # Loại bóng
    _, mask = cv2.threshold(fg, 200, 255, cv2.THRESH_BINARY)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=2)

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if not contours:
        if last_good_box is not None:
            x1, y1, x2, y2 = last_good_box
            return frame[y1:y2, x1:x2], last_good_box, mask, False

        roi, box = crop_center_roi(frame, ROI_SCALE)
        return roi, box, mask, False

    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    chosen = None
    for cnt in contours[:10]:
        if is_valid_object_contour(cnt, frame.shape, min_area):
            chosen = cnt
            break

    if chosen is None:
        if last_good_box is not None:
            x1, y1, x2, y2 = last_good_box
            return frame[y1:y2, x1:x2], last_good_box, mask, False

        roi, box = crop_center_roi(frame, ROI_SCALE)
        return roi, box, mask, False

    x, y, bw, bh = cv2.boundingRect(chosen)
    box = expand_box((x, y, x + bw, y + bh), frame.shape, PADDING)
    box = smooth_box(box)

    last_good_box = box

    x1, y1, x2, y2 = box
    return frame[y1:y2, x1:x2], box, mask, True


def preprocess_frame(frame_bgr):
    frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
    img = cv2.resize(frame_rgb, IMG_SIZE)
    img = img.astype(np.float32)
    img = np.expand_dims(img, axis=0)
    return img


def predict_with_tta(input_frame):
    frames = [input_frame]

    # Lật ngang
    frames.append(cv2.flip(input_frame, 1))

    # Crop giữa nhẹ
    h, w = input_frame.shape[:2]
    crop_scale = 0.90
    ch, cw = int(h * crop_scale), int(w * crop_scale)

    y1 = max(0, (h - ch) // 2)
    x1 = max(0, (w - cw) // 2)

    center_crop = input_frame[y1:y1 + ch, x1:x1 + cw]
    frames.append(center_crop)

    batch = np.vstack([preprocess_frame(f) for f in frames])
    pred = model.predict(batch, verbose=0)

    return np.mean(pred, axis=0)


def draw_text_box(frame, lines, x=20, y=35):
    for i, text in enumerate(lines):
        yy = y + i * 32

        cv2.putText(
            frame,
            text,
            (x, yy),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.78,
            (0, 0, 0),
            4
        )

        cv2.putText(
            frame,
            text,
            (x, yy),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.78,
            (255, 255, 255),
            2
        )


cap = cv2.VideoCapture(CAMERA_INDEX)

if not cap.isOpened():
    raise RuntimeError(
        "Không mở được camera. Thử đổi CAMERA_INDEX = 1 hoặc kiểm tra quyền camera."
    )

print("Đang mở camera...")
print("q: thoát | s: lưu ảnh | c: đổi chế độ ROI | r: reset background")
print("Mẹo: vừa mở camera nên để nền trống 1-2 giây rồi mới đưa vật vào.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Không đọc được frame từ camera.")
        break

    display = frame.copy()
    roi_mode = ROI_MODES[roi_mode_index]
    found_object = True

    if roi_mode == "AUTO":
        input_frame, box, mask, found_object = find_object_roi(frame)

        x1, y1, x2, y2 = box
        color = (0, 255, 0) if found_object else (0, 180, 255)

        cv2.rectangle(display, (x1, y1), (x2, y2), color, 2)

    elif roi_mode == "CENTER":
        input_frame, box = crop_center_roi(frame, ROI_SCALE)

        x1, y1, x2, y2 = box
        cv2.rectangle(display, (x1, y1), (x2, y2), (0, 255, 0), 2)

    else:
        input_frame = frame

    pred = predict_with_tta(input_frame)

    pred_history.append(pred)
    avg_pred = np.mean(pred_history, axis=0)

    idx = int(np.argmax(avg_pred))
    confidence = float(avg_pred[idx])

    if confidence >= CONF_THRESHOLD:
        main_label = class_names[idx]
    else:
        main_label = "Không chắc chắn"

    top3_idx = avg_pred.argsort()[-3:][::-1]

    lines = [
        f"Mode: {roi_mode}",
        f"{main_label}: {confidence * 100:.2f}%",
    ]

    if roi_mode == "AUTO" and not found_object:
        lines.append("Đang tìm vật / dung box gần nhất")

    for rank, i in enumerate(top3_idx, start=1):
        lines.append(
            f"Top {rank}: {class_names[int(i)]} {avg_pred[int(i)] * 100:.2f}%"
        )

    draw_text_box(display, lines)

    cv2.imshow("SWSC Waste Camera - Auto ROI", display)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

    if key == ord("s"):
        filename = CAPTURE_DIR / f"frame_{int(time.time())}.jpg"
        cv2.imwrite(str(filename), frame)
        print("Đã lưu:", filename)

    if key == ord("c"):
        roi_mode_index = (roi_mode_index + 1) % len(ROI_MODES)

        pred_history.clear()
        box_history.clear()

        print("Đổi mode:", ROI_MODES[roi_mode_index])

    if key == ord("r"):
        bg_subtractor = cv2.createBackgroundSubtractorMOG2(
            history=300,
            varThreshold=28,
            detectShadows=True
        )

        pred_history.clear()
        box_history.clear()
        last_good_box = None

        print("Đã reset background. Để nền trống 1-2 giây.")

cap.release()
cv2.destroyAllWindows()