from pathlib import Path
from collections import Counter
import json
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)

from tensorflow.keras import layers
from tensorflow.keras.applications import EfficientNetB2
from tensorflow.keras.applications.efficientnet import preprocess_input


# ===================== CẤU HÌNH =====================

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
CAMERA_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "datasets" / "standardized_256"
MODEL_DIR = CAMERA_DIR / "models"
MODEL_DIR.mkdir(parents=True, exist_ok=True)

IMG_SIZE = (260, 260)
BATCH_SIZE = 24
SEED = 42

EPOCHS_HEAD = 15
EPOCHS_FINE_TUNE = 12
TOTAL_EPOCHS = EPOCHS_HEAD + EPOCHS_FINE_TUNE
FINE_TUNE_LAST_N = 80

print("PROJECT_ROOT:", PROJECT_ROOT)
print("DATA_DIR:", DATA_DIR)
print("MODEL_DIR:", MODEL_DIR)

if not DATA_DIR.exists():
    raise FileNotFoundError(f"Không tìm thấy dataset tại: {DATA_DIR}")


# ===================== HÀM LƯU BẢNG THÀNH ẢNH =====================

def save_table_image(df, title, save_path):
    fig_height = max(3, len(df) * 0.55)

    fig, ax = plt.subplots(figsize=(14, fig_height))
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


# ===================== BẢNG 01: DATASET SPLIT =====================

def count_images(folder):
    return len([
        p for p in folder.iterdir()
        if p.is_file() and p.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp", ".webp"]
    ])


class_dirs = [d for d in sorted(DATA_DIR.iterdir()) if d.is_dir()]
total_images = sum(count_images(d) for d in class_dirs)

train_count = int(total_images * 0.8)
val_count = total_images - train_count

dataset_split_df = pd.DataFrame([
    ["Train", train_count, "80%"],
    ["Validation", val_count, "20%"],
    ["Tổng", total_images, "100%"],
], columns=["Tập dữ liệu", "Số lượng ảnh", "Tỷ lệ"])

dataset_split_df.to_csv(
    MODEL_DIR / "efficientnetb2_dataset_split.csv",
    index=False,
    encoding="utf-8-sig"
)

save_table_image(
    dataset_split_df,
    "Bảng. Phân chia tập dữ liệu EfficientNetB2",
    MODEL_DIR / "01_efficientnetb2_dataset_split.png"
)


# ===================== BẢNG 02: CLASS DISTRIBUTION =====================

class_distribution_rows = []

for class_dir in class_dirs:
    class_distribution_rows.append([
        class_dir.name,
        count_images(class_dir)
    ])

class_distribution_df = pd.DataFrame(
    class_distribution_rows,
    columns=["Lớp dữ liệu", "Số lượng ảnh"]
)

class_distribution_df.to_csv(
    MODEL_DIR / "efficientnetb2_class_distribution.csv",
    index=False,
    encoding="utf-8-sig"
)

save_table_image(
    class_distribution_df,
    "Bảng. Phân bố dữ liệu theo lớp EfficientNetB2",
    MODEL_DIR / "02_efficientnetb2_class_distribution.png"
)


# ===================== BẢNG 03: CONFIG =====================

config_df = pd.DataFrame([
    ["Model", "EfficientNetB2"],
    ["Chức năng sử dụng", "Camera AI"],
    ["Framework", "TensorFlow / Keras"],
    ["Input Size", "260×260"],
    ["Batch Size", BATCH_SIZE],
    ["Epoch Stage 1", EPOCHS_HEAD],
    ["Epoch Fine-tune", EPOCHS_FINE_TUNE],
    ["Tổng Epoch tối đa", TOTAL_EPOCHS],
    ["Learning Rate Stage 1", "0.0008"],
    ["Learning Rate Stage 2", "0.000008"],
    ["Optimizer", "Adam"],
    ["Loss Function", "CategoricalCrossentropy"],
    ["Label Smoothing", "0.05"],
    ["Transfer Learning", "Có"],
    ["Pretrained Weight", "ImageNet"],
    ["Fine-tuning", "Có"],
    ["Fine-tune Last Layers", FINE_TUNE_LAST_N],
    ["Output Model", "waste_efficientnet.keras"],
], columns=["Thông số", "Giá trị"])

config_df.to_csv(
    MODEL_DIR / "efficientnetb2_config.csv",
    index=False,
    encoding="utf-8-sig"
)

save_table_image(
    config_df,
    "Bảng. Cấu hình huấn luyện EfficientNetB2",
    MODEL_DIR / "03_efficientnetb2_config.png"
)


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

with open(MODEL_DIR / "class_names.json", "w", encoding="utf-8") as f:
    json.dump(class_names, f, ensure_ascii=False, indent=2)


# ===================== CLASS WEIGHT =====================

class_counts = Counter()

for class_index, class_name in enumerate(class_names):
    class_dir = DATA_DIR / class_name
    class_counts[class_index] = count_images(class_dir)

class_weight = {
    i: total_images / (num_classes * max(1, class_counts[i]))
    for i in range(num_classes)
}

class_weight_rows = []

for i, name in enumerate(class_names):
    class_weight_rows.append([
        name,
        class_counts[i],
        round(class_weight[i], 4)
    ])

class_weight_df = pd.DataFrame(
    class_weight_rows,
    columns=["Lớp dữ liệu", "Số lượng ảnh", "Class Weight"]
)

class_weight_df.to_csv(
    MODEL_DIR / "efficientnetb2_class_weight.csv",
    index=False,
    encoding="utf-8-sig"
)


# ===================== MODEL =====================

AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds_raw.prefetch(AUTOTUNE)
val_ds = val_ds_raw.prefetch(AUTOTUNE)

data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.16),
    layers.RandomZoom(0.20),
    layers.RandomTranslation(0.12, 0.12),
    layers.RandomContrast(0.25),
], name="augmentation")

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


# ===================== TRAIN STAGE 1 =====================

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=8e-4),
    loss=tf.keras.losses.CategoricalCrossentropy(label_smoothing=0.05),
    metrics=["accuracy"],
)

print("\n===== STAGE 1: TRAIN CLASSIFIER HEAD =====")

history_head = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=EPOCHS_HEAD,
    callbacks=callbacks,
    class_weight=class_weight,
)


# ===================== TRAIN STAGE 2 =====================

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

print("\n===== STAGE 2: FINE-TUNE EFFICIENTNETB2 =====")

history_fine = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=TOTAL_EPOCHS,
    initial_epoch=EPOCHS_HEAD,
    callbacks=callbacks,
    class_weight=class_weight,
)


# ===================== HISTORY MERGE =====================

merged_history = {
    "accuracy": history_head.history.get("accuracy", []) + history_fine.history.get("accuracy", []),
    "val_accuracy": history_head.history.get("val_accuracy", []) + history_fine.history.get("val_accuracy", []),
    "loss": history_head.history.get("loss", []) + history_fine.history.get("loss", []),
    "val_loss": history_head.history.get("val_loss", []) + history_fine.history.get("val_loss", []),
}

history_rows = []

for i in range(len(merged_history["accuracy"])):
    stage = "Stage 1 - Head Training" if i < len(history_head.history.get("accuracy", [])) else "Stage 2 - Fine-tune"

    history_rows.append([
        i + 1,
        stage,
        round(merged_history["loss"][i], 4),
        round(merged_history["accuracy"][i], 4),
        round(merged_history["val_loss"][i], 4),
        round(merged_history["val_accuracy"][i], 4),
    ])

history_df = pd.DataFrame(
    history_rows,
    columns=[
        "Epoch",
        "Giai đoạn",
        "Train Loss",
        "Train Accuracy",
        "Validation Loss",
        "Validation Accuracy",
    ]
)

history_df.to_csv(
    MODEL_DIR / "efficientnetb2_training_history.csv",
    index=False,
    encoding="utf-8-sig"
)

save_table_image(
    history_df,
    "Bảng. Kết quả Train/Validation EfficientNetB2 theo từng Epoch",
    MODEL_DIR / "04_efficientnetb2_train_val_history.png"
)


# ===================== BIỂU ĐỒ ACC / LOSS =====================

epochs = range(1, len(merged_history["accuracy"]) + 1)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(epochs, merged_history["accuracy"], marker="o", label="Train Accuracy")
plt.plot(epochs, merged_history["val_accuracy"], marker="o", label="Validation Accuracy")
plt.axvline(EPOCHS_HEAD, linestyle="--", label="Start Fine-tune")
plt.title("EfficientNetB2 - Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(epochs, merged_history["loss"], marker="o", label="Train Loss")
plt.plot(epochs, merged_history["val_loss"], marker="o", label="Validation Loss")
plt.axvline(EPOCHS_HEAD, linestyle="--", label="Start Fine-tune")
plt.title("EfficientNetB2 - Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig(MODEL_DIR / "05_efficientnetb2_accuracy_loss_curve.png", dpi=300)
plt.close()


# ===================== EVALUATE =====================

final_model_path = MODEL_DIR / "waste_efficientnet_final.keras"
model.save(final_model_path)

val_loss, val_acc = model.evaluate(val_ds, verbose=1)

y_true = []
y_pred = []

for images, labels in val_ds:
    preds = model.predict(images, verbose=0)
    y_true.extend(np.argmax(labels.numpy(), axis=1))
    y_pred.extend(np.argmax(preds, axis=1))

y_true = np.array(y_true)
y_pred = np.array(y_pred)

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, average="macro", zero_division=0)
recall = recall_score(y_true, y_pred, average="macro", zero_division=0)
f1 = f1_score(y_true, y_pred, average="macro", zero_division=0)


# ===================== BẢNG 06: TEST RESULT =====================

result_df = pd.DataFrame([
    ["Validation Accuracy", round(float(val_acc), 4)],
    ["Validation Loss", round(float(val_loss), 4)],
    ["Macro Precision", round(float(precision), 4)],
    ["Macro Recall", round(float(recall), 4)],
    ["Macro F1-score", round(float(f1), 4)],
], columns=["Metric", "Value"])

result_df.to_csv(
    MODEL_DIR / "efficientnetb2_test_result.csv",
    index=False,
    encoding="utf-8-sig"
)

save_table_image(
    result_df,
    "Bảng. Kết quả đánh giá EfficientNetB2",
    MODEL_DIR / "06_efficientnetb2_test_result.png"
)


# ===================== BẢNG 07: CLASSIFICATION REPORT =====================

report_dict = classification_report(
    y_true,
    y_pred,
    target_names=class_names,
    output_dict=True,
    zero_division=0
)

report_df = pd.DataFrame(report_dict).transpose().round(4)

report_df.to_csv(
    MODEL_DIR / "efficientnetb2_classification_report.csv",
    encoding="utf-8-sig"
)

save_table_image(
    report_df.reset_index().rename(columns={"index": "Class"}),
    "Bảng. Classification Report EfficientNetB2",
    MODEL_DIR / "07_efficientnetb2_classification_report.png"
)


# ===================== BẢNG 08: CONFUSION MATRIX =====================

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

plt.title("Confusion Matrix - EfficientNetB2")
plt.tight_layout()
plt.savefig(MODEL_DIR / "08_efficientnetb2_confusion_matrix.png", dpi=300)
plt.close()


# ===================== BẢNG 09: SO SÁNH 2 MODEL =====================

mobilenet_summary_path = PROJECT_ROOT / "reports" / "model_metrics" / "mobilenetv2" / "mobilenetv2_summary.json"

mobilenet_acc = "Chưa có"
mobilenet_loss = "Chưa có"

if mobilenet_summary_path.exists():
    with open(mobilenet_summary_path, "r", encoding="utf-8") as f:
        mobilenet_summary = json.load(f)

    mobilenet_acc = mobilenet_summary.get("test_accuracy", "Chưa có")
    mobilenet_loss = mobilenet_summary.get("test_loss", "Chưa có")

comparison_df = pd.DataFrame([
    ["Chức năng sử dụng", "Upload ảnh", "Camera AI"],
    ["Framework", "PyTorch / Torchvision", "TensorFlow / Keras"],
    ["Model", "MobileNetV2", "EfficientNetB2"],
    ["Input Size", "224×224", "260×260"],
    ["Batch Size", "64", str(BATCH_SIZE)],
    ["Epoch tối đa", "20", str(TOTAL_EPOCHS)],
    ["Fine-tuning", "Không", "Có"],
    ["Data Augmentation", "Cơ bản", "Có"],
    ["Class Weight", "Không", "Có"],
    ["Accuracy", mobilenet_acc, round(float(accuracy), 4)],
    ["Loss", mobilenet_loss, round(float(val_loss), 4)],
    ["Precision", "Xem Classification Report", round(float(precision), 4)],
    ["Recall", "Xem Classification Report", round(float(recall), 4)],
    ["F1-score", "Xem Classification Report", round(float(f1), 4)],
], columns=["Tiêu chí", "MobileNetV2", "EfficientNetB2"])

comparison_df.to_csv(
    MODEL_DIR / "model_comparison_mobilenetv2_efficientnetb2.csv",
    index=False,
    encoding="utf-8-sig"
)

save_table_image(
    comparison_df,
    "Bảng. So sánh MobileNetV2 và EfficientNetB2",
    MODEL_DIR / "09_model_comparison_mobilenetv2_efficientnetb2.png"
)


# ===================== SUMMARY JSON =====================

summary = {
    "model": "EfficientNetB2",
    "framework": "TensorFlow / Keras",
    "input_size": "260x260",
    "batch_size": BATCH_SIZE,
    "max_epochs": TOTAL_EPOCHS,
    "actual_epochs": len(history_df),
    "validation_accuracy": round(float(val_acc), 4),
    "validation_loss": round(float(val_loss), 4),
    "macro_precision": round(float(precision), 4),
    "macro_recall": round(float(recall), 4),
    "macro_f1": round(float(f1), 4),
    "model_path": str(MODEL_DIR / "waste_efficientnet.keras"),
    "final_model_path": str(final_model_path),
    "classes": class_names
}

with open(MODEL_DIR / "efficientnetb2_summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)


print("\nHOÀN TẤT TRAIN EFFICIENTNETB2")
print("Model và bảng ảnh đã lưu tại:", MODEL_DIR)