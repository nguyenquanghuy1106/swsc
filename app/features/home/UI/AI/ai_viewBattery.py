import streamlit as st
from PIL import Image

from features.home.logic.AI.ai_serviceBattery import predict_battery_image
from features.home.logic.AI.ai_history_service import save_ai_history


def render_ai_battery_page():
    st.title("🤖 Nhận diện pin bằng AI")
    st.info("Chức năng này chỉ chấp nhận ảnh thuộc nhóm battery.")

    uploaded_file = st.file_uploader(
        "Tải ảnh pin lên",
        type=["jpg", "jpeg", "png", "webp"],
        key="battery_ai_uploader"
    )

    if uploaded_file is None:
        return

    image = Image.open(uploaded_file)
    st.image(image, caption="Ảnh đã tải lên", use_container_width=True)

    if st.button("🔍 Nhận diện", use_container_width=True, key="battery_ai_predict"):
        try:
            result = predict_battery_image(image)

            if result["success"]:
                save_ai_history(
                    user_id=st.session_state.get("user_id"),
                    user_name=st.session_state.get("user_name"),
                    waste_type="battery",
                    predicted_class=result["predicted_class"],
                    confidence=result["confidence"],
                    image_name=uploaded_file.name
                )

                st.success("Nhận diện thành công và đã lưu lịch sử vào database.")
                st.subheader(f"Kết quả: {result['display_name']}")
                st.metric("Độ tin cậy", f"{result['confidence']}%")
            else:
                st.error(result["message"])
                st.warning(
                    f"AI dự đoán: {result['predicted_class']} "
                    f"({result['confidence']}%)"
                )

            st.markdown("### Tỉ lệ battery")
            st.write(f"Battery: {result['battery_rate']}%")
            st.progress(result["battery_rate"] / 100)

        except Exception as e:
            st.error(f"Lỗi khi nhận diện: {e}")

    if st.button("⬅️ Quay lại trang Pin", use_container_width=True):
        st.query_params["page"] = "battery"
        st.rerun()