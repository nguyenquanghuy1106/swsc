import streamlit as st
from PIL import Image

from features.home.logic.AI.ai_servicePlastic import predict_waste_image

def render_ai_page():
    st.title("🤖 Nhận diện rác bằng AI")

    st.info(
        "Chức năng này chỉ nhận diện 5 nhóm: "
        "Nhựa, Giấy, Bìa carton, Thủy tinh, Kim loại."
    )

    uploaded_file = st.file_uploader(
        "Tải ảnh rác lên",
        type=["jpg", "jpeg", "png", "webp"]
    )

    if uploaded_file is None:
        return

    image = Image.open(uploaded_file)
    st.image(image, caption="Ảnh đã tải lên", use_container_width=True)

    if st.button("🔍 Nhận diện", use_container_width=True):
        try:
            result = predict_waste_image(image)

            if not result["success"]:
                st.error(result["message"])
                st.warning(
                    f"AI dự đoán: {result['predicted_class']} "
                    f"({result['confidence']}%)"
                )
            else:
                st.success(result["message"])
                st.subheader(f"Kết quả: {result['display_name']}")
                st.metric("Độ tin cậy", f"{result['confidence']}%")

            st.markdown("### Tỉ lệ trong 5 nhóm được phép")

            for name, value in result["allowed_probabilities"].items():
                st.write(f"{name}: {value}%")
                st.progress(value / 100)

        except Exception as e:
            st.error(f"Lỗi khi nhận diện: {e}")