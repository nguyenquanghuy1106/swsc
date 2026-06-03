from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


# ================== ĐƯỜNG DẪN ==================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "datasets" / "standardized_256"

REPORT_DIR = BASE_DIR / "reports" / "model_tables"
REPORT_DIR.mkdir(parents=True, exist_ok=True)


# ================== HÀM ĐẾM ẢNH ==================

def count_images_in_folder(folder_path):
    image_exts = [".jpg", ".jpeg", ".png", ".bmp", ".webp"]

    return len([
        file for file in folder_path.iterdir()
        if file.is_file() and file.suffix.lower() in image_exts
    ])


# ================== HÀM LƯU BẢNG THÀNH ẢNH ==================

def save_table_image(df, title, file_name):
    fig_height = max(3, len(df) * 0.65)

    fig, ax = plt.subplots(figsize=(14, fig_height))
    ax.axis("off")

    table = ax.table(
        cellText=df.values,
        colLabels=df.columns,
        cellLoc="center",
        loc="center"
    )

    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1.2, 1.8)

    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_text_props(weight="bold")
            cell.set_height(0.09)

    plt.title(title, fontsize=16, fontweight="bold", pad=20)

    save_path = REPORT_DIR / file_name
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"Đã lưu: {save_path}")


# ================== BẢNG 1: PHÂN CHIA DATASET ==================

def create_dataset_split_table(total_images):
    train = int(total_images * 0.8)
    val = int(total_images * 0.1)
    test = total_images - train - val

    return pd.DataFrame([
        ["Train", train, "80%"],
        ["Validation", val, "10%"],
        ["Test", test, "10%"],
        ["Tổng", total_images, "100%"],
    ], columns=["Tập dữ liệu", "Số lượng ảnh", "Tỷ lệ"])


# ================== BẢNG 2: PHÂN BỐ DỮ LIỆU THEO LỚP ==================

def create_class_distribution_table():
    rows = []
    total_images = 0

    if not DATA_DIR.exists():
        raise FileNotFoundError(f"Không tìm thấy dataset tại: {DATA_DIR}")

    for class_dir in sorted(DATA_DIR.iterdir()):
        if class_dir.is_dir():
            count = count_images_in_folder(class_dir)
            rows.append([class_dir.name, count])
            total_images += count

    df = pd.DataFrame(rows, columns=["Lớp dữ liệu", "Số lượng ảnh"])
    return df, total_images


# ================== BẢNG 3: CẤU HÌNH MOBILENETV2 ==================

def create_mobilenetv2_config_table():
    return pd.DataFrame([
        ["Model", "MobileNetV2"],
        ["Chức năng sử dụng", "Upload ảnh"],
        ["Framework", "PyTorch / Torchvision"],
        ["Input Size", "224×224"],
        ["Batch Size", "32"],
        ["Epoch", "5"],
        ["Learning Rate", "0.001"],
        ["Optimizer", "Adam"],
        ["Loss Function", "CrossEntropyLoss"],
        ["Transfer Learning", "Có"],
        ["Pretrained Weight", "ImageNet"],
        ["Fine-tuning", "Không"],
        ["Model Output", "best_model.pth"],
    ], columns=["Thông số", "Giá trị"])


# ================== BẢNG 4: CẤU HÌNH EFFICIENTNETB2 ==================

def create_efficientnetb2_config_table():
    return pd.DataFrame([
        ["Model", "EfficientNetB2"],
        ["Chức năng sử dụng", "Camera AI"],
        ["Framework", "TensorFlow / Keras"],
        ["Input Size", "260×260"],
        ["Batch Size", "24"],
        ["Epoch Stage 1", "15"],
        ["Epoch Fine-tune", "12"],
        ["Tổng Epoch", "27"],
        ["Learning Rate Stage 1", "0.0008"],
        ["Learning Rate Stage 2", "0.000008"],
        ["Optimizer", "Adam"],
        ["Loss Function", "CategoricalCrossentropy"],
        ["Label Smoothing", "0.05"],
        ["Transfer Learning", "Có"],
        ["Pretrained Weight", "ImageNet"],
        ["Fine-tuning", "Có"],
        ["Fine-tune Last Layers", "80"],
        ["Model Output", "waste_efficientnet.keras"],
    ], columns=["Thông số", "Giá trị"])


# ================== BẢNG 5: DATA AUGMENTATION ==================

def create_augmentation_table():
    return pd.DataFrame([
        ["RandomFlip", "Lật ngang ảnh", "horizontal"],
        ["RandomRotation", "Xoay ảnh ngẫu nhiên", "0.16"],
        ["RandomZoom", "Phóng to / thu nhỏ ảnh", "0.20"],
        ["RandomTranslation", "Dịch chuyển ảnh", "0.12, 0.12"],
        ["RandomContrast", "Thay đổi độ tương phản", "0.25"],
    ], columns=["Kỹ thuật", "Ý nghĩa", "Giá trị"])


# ================== BẢNG 6: CLASS WEIGHT ==================

def create_class_weight_table(total_images):
    rows = []

    class_dirs = [d for d in sorted(DATA_DIR.iterdir()) if d.is_dir()]
    num_classes = len(class_dirs)

    for class_dir in class_dirs:
        count = count_images_in_folder(class_dir)
        weight = total_images / (num_classes * max(1, count))

        rows.append([
            class_dir.name,
            count,
            round(weight, 4)
        ])

    return pd.DataFrame(
        rows,
        columns=["Lớp dữ liệu", "Số lượng ảnh", "Class Weight"]
    )


# ================== BẢNG 7: SO SÁNH CẤU HÌNH 2 MODEL ==================

def create_model_comparison_table():
    return pd.DataFrame([
        ["Chức năng sử dụng", "Upload ảnh", "Camera AI"],
        ["Framework", "PyTorch", "TensorFlow/Keras"],
        ["Input Size", "224×224", "260×260"],
        ["Batch Size", "32", "24"],
        ["Epoch", "5", "27"],
        ["Optimizer", "Adam", "Adam"],
        ["Loss Function", "CrossEntropyLoss", "CategoricalCrossentropy"],
        ["Transfer Learning", "Có", "Có"],
        ["Pretrained Weight", "ImageNet", "ImageNet"],
        ["Fine-tuning", "Không", "Có"],
        ["Data Augmentation", "Cơ bản", "Có"],
        ["Class Weight", "Không", "Có"],
        ["Output Model", "best_model.pth", "waste_efficientnet.keras"],
    ], columns=["Tiêu chí", "MobileNetV2", "EfficientNetB2"])


# ================== MAIN ==================

def main():
    print("Đang tạo bảng báo cáo model...")

    class_distribution_df, total_images = create_class_distribution_table()

    dataset_split_df = create_dataset_split_table(total_images)
    mobilenetv2_config_df = create_mobilenetv2_config_table()
    efficientnetb2_config_df = create_efficientnetb2_config_table()
    augmentation_df = create_augmentation_table()
    class_weight_df = create_class_weight_table(total_images)
    model_comparison_df = create_model_comparison_table()

    save_table_image(
        dataset_split_df,
        "Bảng 4.1. Phân chia tập dữ liệu",
        "01_dataset_split.png"
    )

    save_table_image(
        class_distribution_df,
        "Bảng 4.2. Phân bố dữ liệu theo lớp",
        "02_class_distribution.png"
    )

    save_table_image(
        mobilenetv2_config_df,
        "Bảng 4.3. Cấu hình huấn luyện MobileNetV2",
        "03_mobilenetv2_config.png"
    )

    save_table_image(
        efficientnetb2_config_df,
        "Bảng 4.4. Cấu hình huấn luyện EfficientNetB2",
        "04_efficientnetb2_config.png"
    )

    save_table_image(
        augmentation_df,
        "Bảng 4.5. Các kỹ thuật tăng cường dữ liệu EfficientNetB2",
        "05_efficientnetb2_augmentation.png"
    )

    save_table_image(
        class_weight_df,
        "Bảng 4.6. Trọng số lớp dữ liệu EfficientNetB2",
        "06_efficientnetb2_class_weight.png"
    )

    save_table_image(
        model_comparison_df,
        "Bảng 4.7. So sánh cấu hình MobileNetV2 và EfficientNetB2",
        "07_model_comparison.png"
    )

    print("\nHoàn tất.")
    print(f"Các bảng ảnh đã được lưu tại: {REPORT_DIR}")


if __name__ == "__main__":
    main()