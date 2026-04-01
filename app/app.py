import streamlit as st
from PIL import Image
# đoc file ảnh và xử lý ảnh
import sys
import os

# Thêm thư mục gốc project vào đường dẫn import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.models_utils import predict_image


st.set_page_config(page_title="Phân loại rác bằng AI", page_icon="♻️")

st.title("SWSC - Phân loại rác bằng AI")
st.write("Tải ảnh lên để hệ thống dự đoán loại rác.")

uploaded_file = st.file_uploader("Chọn một ảnh", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption="Ảnh bạn đã tải lên", width="stretch")

    predicted_class, confidence_score = predict_image(image)

    st.subheader("Kết quả dự đoán")
    st.write(f"**Loại rác:** {predicted_class}")
    st.write(f"**Độ tin cậy:** {confidence_score:.2f}%")