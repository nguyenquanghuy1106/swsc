"""
Train / fine-tune EfficientNetB2 cho phân loại rác.

Có:
- Dùng chung dataset ở: D:/SWCS/datasets/standardized_256
- EfficientNetB2 pretrained ImageNet
- Data augmentation
- Class weight cho dữ liệu lệch class
- Biểu đồ accuracy/loss từng giai đoạn
- Biểu đồ tổng toàn bộ quá trình train
- Confusion matrix
- Classification report
"""

from pathlib import Path
from collections import Counter
import json
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay

from tensorflow.keras import layers
from tensorflow.keras.applications import EfficientNetB2
from tensorflow.keras.applications.efficientnet import preprocess_input


# ===================== CẤU HÌNH =====================

# File đang ở: D:/SWCS/SWSC_camera/src/train_efficientnet.py
# parent.parent = D:/SWCS/SWSC_camera
# parent.parent.parent = D:/SWCS
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
CAMERA_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "datasets" / "standardized_256"
MODEL_DIR = CAMERA_DIR / "models"
MODEL_DIR.mkdir(exist_ok=True)

IMG_SIZE = (260, 260)
BATCH_SIZE = 24
SEED = 42

EPOCHS_HEAD = 15
EPOCHS_FINE_TUNE = 12
FINE_TUNE_LAST_N = 80

print("PROJECT_ROOT:", PROJECT_ROOT)
print("DATA_DIR:", DATA_DIR)
print("MODEL_DIR:", MODEL_DIR)

if not DATA_DIR.exists():
    raise FileNotFoundError(f"Không tìm thấy dataset tại: {DATA_DIR}")


# ===================== LOAD DATASET =====================

train_ds_raw = tf.keras.utils.image_dataset_from_directory(
    DATA_DIR,
    validation_split=0.2,
    subset="training",
    seed=SEED,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    label_mode="categorical",
)

val_ds_raw = tf.keras.utils.image_dataset_from_directory(
    DATA_DIR,
    validation_split=0.2,
    subset="validation",
    seed=SEED,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    label_mode="categorical",
    shuffle=False,
)

class_names = train_ds_raw.class_names
num_classes = len(class_names)

print("\nClass names:", class_names)
print("Number of classes:", num_classes)

with open(MODEL_DIR / "class_names.json", "w", encoding="utf-8") as f:
    json.dump(class_names, f, ensure_ascii=False, indent=2)


# ===================== CLASS WEIGHT =====================

class_counts = Counter()

for class_index, class_name in enumerate(class_names):
    class_dir = DATA_DIR / class_name
    count = len([
        p for p in class_dir.iterdir()
        if p.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp", ".webp"]
    ])
    class_counts[class_index] = count

total_images = sum(class_counts.values())

class_weight = {
    i: total_images / (num_classes * max(1, class_counts[i]))
    for i in range(num_classes)
}

print("\n===== CLASS COUNTS =====")
for i, name in enumerate(class_names):
    print(f"{name}: {class_counts[i]} ảnh")

print("\n===== CLASS WEIGHT =====")
for i, name in enumerate(class_names):
    print(f"{name}: {class_weight[i]:.4f}")


AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds_raw.prefetch(AUTOTUNE)
val_ds = val_ds_raw.prefetch(AUTOTUNE)


# ===================== AUGMENTATION =====================

data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.16),
    layers.RandomZoom(0.20),
    layers.RandomTranslation(0.12, 0.12),
    layers.RandomContrast(0.25),
], name="augmentation")


# ===================== MODEL =====================

base_model = EfficientNetB2(
    include_top=False,
    weights="imagenet",
    input_shape=(IMG_SIZE[0], IMG_SIZE[1], 3),
)

base_model.trainable = False

inputs = layers.Input(shape=(IMG_SIZE[0], IMG_SIZE[1], 3))
x = data_augmentation(inputs)
x = preprocess_input(x)
x = base_model(x, training=False)
x = layers.GlobalAveragePooling2D()(x)
x = layers.Dropout(0.30)(x)
x = layers.Dense(256, activation="relu")(x)
x = layers.Dropout(0.25)(x)
outputs = layers.Dense(num_classes, activation="softmax")(x)

model = tf.keras.Model(inputs, outputs)


callbacks = [
    tf.keras.callbacks.ModelCheckpoint(
        MODEL_DIR / "waste_efficientnet.keras",
        monitor="val_accuracy",
        save_best_only=True,
        verbose=1,
    ),
    tf.keras.callbacks.EarlyStopping(
        monitor="val_loss",
        patience=5,
        restore_best_weights=True,
        verbose=1,
    ),
    tf.keras.callbacks.ReduceLROnPlateau(
        monitor="val_loss",
        factor=0.3,
        patience=2,
        min_lr=1e-7,
        verbose=1,
    ),
]


# ===================== HÀM VẼ BIỂU ĐỒ =====================

def plot_history(history, title, save_path):
    acc = history.history.get("accuracy", [])
    val_acc = history.history.get("val_accuracy", [])
    loss = history.history.get("loss", [])
    val_loss = history.history.get("val_loss", [])

    epochs = range(1, len(acc) + 1)

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(epochs, acc, label="Train Accuracy")
    plt.plot(epochs, val_acc, label="Validation Accuracy")
    plt.title(f"{title} - Accuracy")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(epochs, loss, label="Train Loss")
    plt.plot(epochs, val_loss, label="Validation Loss")
    plt.title(f"{title} - Loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()


def merge_histories(history1, history2):
    merged = {}

    for key in history1.history.keys():
        merged[key] = history1.history[key] + history2.history.get(key, [])

    return merged


def plot_merged_history(merged_history, save_path):
    acc = merged_history["accuracy"]
    val_acc = merged_history["val_accuracy"]
    loss = merged_history["loss"]
    val_loss = merged_history["val_loss"]

    epochs = range(1, len(acc) + 1)

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(epochs, acc, label="Train Accuracy")
    plt.plot(epochs, val_acc, label="Validation Accuracy")
    plt.axvline(EPOCHS_HEAD, linestyle="--", label="Start Fine-tune")
    plt.title("Total Training - Accuracy")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(epochs, loss, label="Train Loss")
    plt.plot(epochs, val_loss, label="Validation Loss")
    plt.axvline(EPOCHS_HEAD, linestyle="--", label="Start Fine-tune")
    plt.title("Total Training - Loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()


# ===================== GIAI ĐOẠN 1 =====================

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=8e-4),
    loss=tf.keras.losses.CategoricalCrossentropy(label_smoothing=0.05),
    metrics=["accuracy"],
)

print("\n===== GIAI ĐOẠN 1: TRAIN CLASSIFIER HEAD =====")

history_head = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=EPOCHS_HEAD,
    callbacks=callbacks,
    class_weight=class_weight,
)

plot_history(
    history_head,
    "Stage 1 Head Training",
    MODEL_DIR / "stage_1_head_accuracy_loss.png"
)


# ===================== GIAI ĐOẠN 2 =====================

print("\n===== GIAI ĐOẠN 2: FINE-TUNE EFFICIENTNETB2 =====")

base_model.trainable = True

for layer in base_model.layers[:-FINE_TUNE_LAST_N]:
    layer.trainable = False

for layer in base_model.layers:
    if isinstance(layer, layers.BatchNormalization):
        layer.trainable = False

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=8e-6),
    loss=tf.keras.losses.CategoricalCrossentropy(label_smoothing=0.05),
    metrics=["accuracy"],
)

history_fine = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=EPOCHS_HEAD + EPOCHS_FINE_TUNE,
    initial_epoch=EPOCHS_HEAD,
    callbacks=callbacks,
    class_weight=class_weight,
)

plot_history(
    history_fine,
    "Stage 2 Fine-tune",
    MODEL_DIR / "stage_2_finetune_accuracy_loss.png"
)


# ===================== BIỂU ĐỒ TỔNG =====================

merged_history = merge_histories(history_head, history_fine)

plot_merged_history(
    merged_history,
    MODEL_DIR / "total_training_accuracy_loss.png"
)


# ===================== LƯU MODEL =====================

final_model_path = MODEL_DIR / "waste_efficientnet_final.keras"
model.save(final_model_path)

print("\nĐã lưu model:")
print("-", MODEL_DIR / "waste_efficientnet.keras")
print("-", final_model_path)
print("-", MODEL_DIR / "class_names.json")


# ===================== ĐÁNH GIÁ HIỆU SUẤT =====================

print("\n===== ĐÁNH GIÁ MODEL TRÊN VALIDATION SET =====")

val_loss, val_acc = model.evaluate(val_ds, verbose=1)

print(f"\nValidation Loss: {val_loss:.4f}")
print(f"Validation Accuracy: {val_acc:.4f}")


# Lấy y_true và y_pred
y_true = []
y_pred = []

for images, labels in val_ds:
    preds = model.predict(images, verbose=0)

    y_true.extend(np.argmax(labels.numpy(), axis=1))
    y_pred.extend(np.argmax(preds, axis=1))

y_true = np.array(y_true)
y_pred = np.array(y_pred)


# Classification report
report = classification_report(
    y_true,
    y_pred,
    target_names=class_names,
    digits=4
)

print("\n===== CLASSIFICATION REPORT =====")
print(report)

with open(MODEL_DIR / "classification_report.txt", "w", encoding="utf-8") as f:
    f.write(report)


# Confusion Matrix
cm = confusion_matrix(y_true, y_pred)

plt.figure(figsize=(12, 10))
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=class_names
)
disp.plot(
    xticks_rotation=45,
    cmap="Blues",
    values_format="d"
)
plt.title("Confusion Matrix")
plt.tight_layout()
plt.savefig(MODEL_DIR / "confusion_matrix.png", dpi=300)
plt.close()


print("\nĐã lưu biểu đồ và báo cáo:")
print("-", MODEL_DIR / "stage_1_head_accuracy_loss.png")
print("-", MODEL_DIR / "stage_2_finetune_accuracy_loss.png")
print("-", MODEL_DIR / "total_training_accuracy_loss.png")
print("-", MODEL_DIR / "confusion_matrix.png")
print("-", MODEL_DIR / "classification_report.txt")