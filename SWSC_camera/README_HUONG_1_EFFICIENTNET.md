# SWSC Camera - Hướng 1: Pretrained EfficientNetB0

Project này đã được bổ sung hướng train bằng **EfficientNetB0 pretrained ImageNet** và quét camera realtime.

## 1. Cấu trúc dataset hiện có

Trong file bạn gửi, dataset đang có **10 class**, không phải 12 class:

```text
datasets/standardized_256/
  battery/
  biological/
  cardboard/
  clothes/
  glass/
  metal/
  paper/
  plastic/
  shoes/
  trash/
```

Nếu bạn thật sự cần 12 class thì tạo thêm 2 thư mục class còn thiếu vào `datasets/standardized_256/`, rồi bỏ ảnh vào trước khi train.

## 2. Cài thư viện

Mở terminal tại thư mục project:

```bash
pip install -r requirements.txt
```

## 3. Train model EfficientNetB0

```bash
python src/train_efficientnet.py
```

Sau khi chạy xong sẽ có:

```text
models/waste_efficientnet.keras
models/waste_efficientnet_final.keras
models/class_names.json
```

File `waste_efficientnet.keras` là model tốt nhất theo `val_accuracy`.

## 4. Quét camera realtime

```bash
python src/camera_predict.py
```

Phím sử dụng:

```text
q : thoát camera
s : lưu frame hiện tại vào captured_frames/
```

## 5. Vì sao hướng này tốt hơn CNN tự xây?

EfficientNetB0 đã học đặc trưng ảnh từ ImageNet, nên nó hiểu hình dạng, cạnh, texture, màu sắc tốt hơn CNN nhỏ tự train từ đầu. Khi fine-tune với dataset rác của bạn, model thường tổng quát hóa tốt hơn trên ảnh camera ngoài đời.

## 6. Nhưng có cần chụp thêm ảnh ngoài đời không?

Không bắt buộc để chạy được camera. Nhưng nếu muốn độ chính xác ngoài đời thật cao và ổn định, vẫn nên bổ sung ảnh thật sau này.

Hướng này giúp tốt hơn vì dùng pretrained model, augmentation, fine-tune và vùng ROI giữa camera. Tuy nhiên không có model nào đảm bảo 100% đúng với mọi vật ngoài đời nếu dataset chưa đủ đa dạng.

## 7. Chỉnh ngưỡng tin cậy

Trong `src/camera_predict.py`:

```python
CONF_THRESHOLD = 0.60
```

Nếu model đoán bừa nhiều, tăng lên `0.70` hoặc `0.80`.

Nếu model hay báo không chắc chắn, giảm xuống `0.50`.

## 8. Chỉnh camera

Nếu không mở được webcam, đổi:

```python
CAMERA_INDEX = 0
```

thành:

```python
CAMERA_INDEX = 1
```

## 9. Lưu ý quan trọng

Camera realtime vẫn phải resize ảnh về `224x224` trước khi đưa vào model. Đây không phải là làm sai ý tưởng, mà là yêu cầu kỹ thuật vì model chỉ nhận input cố định.
