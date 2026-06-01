import streamlit as st
from PIL import Image

from features.home.logic.AI.ai_serviceNylon import predict_nylon_image


def render_ai_nylon_page():
    st.title("🤖 Nhận diện rác sinh học bằng AI")

    st.info("Chức năng này chỉ chấp nhận ảnh thuộc nhóm biological.")

    uploaded_file = st.file_uploader(
        "Tải ảnh lên",
        type=["jpg", "jpeg", "png", "webp"],
        key="nylon_ai_uploader"
    )

    if uploaded_file is None:
        return

    image = Image.open(uploaded_file)
    st.image(image, caption="Ảnh đã tải lên", use_container_width=True)

    if st.button("🔍 Nhận diện", use_container_width=True, key="nylon_ai_predict"):
        try:
            result = predict_nylon_image(image)

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

            st.markdown("### Tỉ lệ biological")
            st.write(f"Biological: {result['biological_rate']}%")
            st.progress(result["biological_rate"] / 100)

        except Exception as e:
            st.error(f"Lỗi khi nhận diện: {e}")

    if st.button("⬅️ Quay lại trang Nilon", use_container_width=True):
        st.query_params["page"] = "nylon"
        st.rerun()