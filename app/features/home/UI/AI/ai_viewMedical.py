import streamlit as st
from PIL import Image

from features.home.logic.AI.ai_serviceMedical import predict_medical_image


def render_ai_medical_page():
    st.title("🤖 Nhận diện rác y tế bằng AI")

    st.info("Chức năng này chỉ chấp nhận 3 nhóm: clothes, shoes, trash.")

    uploaded_file = st.file_uploader(
        "Tải ảnh lên",
        type=["jpg", "jpeg", "png", "webp"],
        key="medical_ai_uploader"
    )

    if uploaded_file is None:
        return

    image = Image.open(uploaded_file)
    st.image(image, caption="Ảnh đã tải lên", use_container_width=True)

    if st.button("🔍 Nhận diện", use_container_width=True, key="medical_ai_predict"):
        try:
            result = predict_medical_image(image)

            if result["success"]:
                st.success(result["message"])
                st.subheader(f"Kết quả: {result['display_name']}")
                st.metric("Độ tin cậy", f"{result['confidence']}%")
            else:
                st.error(result["message"])
                st.warning(
                    f"AI dự đoán: {result['predicted_class']} "
                    f"({result['confidence']}%)"
                )

            st.markdown("### Tỉ lệ trong 3 nhóm được phép")

            for name, value in result["allowed_probabilities"].items():
                st.write(f"{name}: {value}%")
                st.progress(value / 100)

        except Exception as e:
            st.error(f"Lỗi khi nhận diện: {e}")

    if st.button("⬅️ Quay lại trang Dụng cụ y tế", use_container_width=True):
        st.query_params["page"] = "medical"
        st.rerun()