import streamlit as st
from PIL import Image
import html
from urllib.parse import unquote

from shared.styles.ai_css import load_ai_css
from features.database.connection import get_connection
from features.home.logic.AI.ai_servicePlastic import predict_waste_image
from features.home.logic.AI.ai_history_service import save_ai_scan_result


GROUP_MAP = {
    "plastic": {
        "group": "RÁC TÁI CHẾ",
        "icon": "🧴♻️",
        "desc": "Nhựa thuộc nhóm rác tái chế.",
        "action": "Làm sạch, để khô và bỏ vào thùng rác tái chế.",
    },
    "paper": {
        "group": "RÁC TÁI CHẾ",
        "icon": "📄♻️",
        "desc": "Giấy thuộc nhóm rác tái chế.",
        "action": "Giữ khô, làm phẳng và bỏ vào thùng rác tái chế.",
    },
    "cardboard": {
        "group": "RÁC TÁI CHẾ",
        "icon": "📦♻️",
        "desc": "Bìa carton thuộc nhóm rác tái chế.",
        "action": "Gấp gọn và bỏ vào thùng rác tái chế.",
    },
    "glass": {
        "group": "RÁC TÁI CHẾ",
        "icon": "🍾♻️",
        "desc": "Thủy tinh thuộc nhóm rác tái chế.",
        "action": "Rửa sạch, tránh làm vỡ và bỏ vào khu vực tái chế.",
    },
    "metal": {
        "group": "RÁC TÁI CHẾ",
        "icon": "🥫♻️",
        "desc": "Kim loại thuộc nhóm rác tái chế.",
        "action": "Làm sạch và bỏ vào thùng rác tái chế.",
    },
    "biological": {
        "group": "RÁC HỮU CƠ",
        "icon": "🍃🍎",
        "desc": "Rác sinh học thuộc nhóm rác hữu cơ.",
        "action": "Bỏ vào thùng rác hữu cơ hoặc dùng để ủ phân.",
    },
    "battery": {
        "group": "RÁC NGUY HẠI",
        "icon": "🔋💡",
        "desc": "Pin thuộc nhóm rác nguy hại, có thể gây ô nhiễm môi trường.",
        "action": "Không bỏ chung với rác thường. Hãy đưa đến điểm thu gom pin.",
    },
    "clothes": {
        "group": "RÁC KHÁC",
        "icon": "👕",
        "desc": "Quần áo thuộc nhóm rác khác.",
        "action": "Có thể tái sử dụng, quyên góp hoặc bỏ vào khu thu gom phù hợp.",
    },
    "shoes": {
        "group": "RÁC KHÁC",
        "icon": "👟",
        "desc": "Giày dép thuộc nhóm rác khác.",
        "action": "Nếu còn dùng được có thể tái sử dụng hoặc quyên góp.",
    },
    "trash": {
        "group": "RÁC KHÁC",
        "icon": "🗑️",
        "desc": "Rác thường hoặc rác khó tái chế.",
        "action": "Bỏ vào thùng rác khác.",
    },
}


def normalize_class_name(name):
    return str(name).strip().lower().replace(" ", "_")


def get_group_info(predicted_class):
    key = normalize_class_name(predicted_class)

    return GROUP_MAP.get(
        key,
        {
            "group": "CHƯA XÁC ĐỊNH",
            "icon": "❓",
            "desc": "AI chưa xác định rõ nhóm rác.",
            "action": "Hãy thử chụp ảnh rõ hơn, nền đơn giản hơn.",
        },
    )


def restore_user_from_query():
    uid = st.query_params.get("uid")
    uname = st.query_params.get("uname")

    if isinstance(uid, list):
        uid = uid[0]

    if isinstance(uname, list):
        uname = uname[0]

    if uid:
        try:
            st.session_state["user_id"] = int(uid)
            st.session_state["is_login"] = True
        except ValueError:
            pass

    if uname:
        st.session_state["user_name"] = unquote(str(uname))
        st.session_state["is_login"] = True


def restore_user_from_current_login():
    """
    Nếu URL không có uid/uname thì lấy user đăng nhập mới nhất
    trong bảng current_login.
    """
    if st.session_state.get("user_id") and st.session_state.get("user_name"):
        return

    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT user_id, userName
            FROM current_login
            WHERE id = 1
            LIMIT 1
            """
        )

        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:
            st.session_state["is_login"] = True
            st.session_state["user_id"] = int(user["user_id"])
            st.session_state["user_name"] = str(user["userName"])

    except Exception:
        pass


def get_logged_user():
    restore_user_from_query()
    restore_user_from_current_login()

    return (
        st.session_state.get("user_id"),
        st.session_state.get("user_name"),
    )


def render_result_card(
    display_name,
    confidence,
    predicted_class,
    group_name,
    group_desc,
    group_action,
):
    display_name = html.escape(str(display_name))
    confidence = html.escape(str(confidence))
    predicted_class = html.escape(str(predicted_class).upper())
    group_name = html.escape(str(group_name))
    group_desc = html.escape(str(group_desc))
    group_action = html.escape(str(group_action))

    st.html(
        f"""
        <div style="
            background:#ffffff;
            border-radius:22px;
            padding:34px;
            box-shadow:0 12px 32px rgba(0,0,0,0.14);
            min-height:420px;
            font-family:Arial, sans-serif;
        ">
            <div style="
                font-size:31px;
                font-weight:950;
                color:#111;
                margin-bottom:24px;
                line-height:1.3;
            ">
                🎯 NHẬN DIỆN: {display_name} ({confidence}%)
            </div>

            <div style="
                background:linear-gradient(135deg,#15a646,#22c55e);
                color:white;
                padding:19px 20px;
                border-radius:16px;
                font-size:29px;
                font-weight:950;
                margin-bottom:26px;
                text-align:center;
            ">
                LOẠI RÁC: {predicted_class}
            </div>

            <div style="
                color:#101010;
                font-size:23px;
                line-height:1.85;
                font-weight:650;
            ">
                <b>📂 Thuộc nhóm:</b> {group_name}<br>
                <b>📝 Mô tả:</b> {group_desc}<br>
                <b>♻️ Hành động:</b> {group_action}
            </div>
        </div>
        """
    )


def render_group_card(group_icon, group_name):
    group_icon = html.escape(str(group_icon))
    group_name = html.escape(str(group_name))

    st.html(
        f"""
        <div style="
            background:#ffffff;
            border-radius:22px;
            padding:42px 24px;
            box-shadow:0 12px 32px rgba(0,0,0,0.14);
            text-align:center;
            min-height:420px;
            display:flex;
            flex-direction:column;
            justify-content:center;
            align-items:center;
            font-family:Arial, sans-serif;
        ">
            <div style="font-size:125px; margin-bottom:28px; line-height:1;">
                {group_icon}
            </div>

            <div style="
                font-size:42px;
                font-weight:950;
                color:#0b0b0b;
                line-height:1.2;
            ">
                {group_name}
            </div>
        </div>
        """
    )


def render_ai_page():
    load_ai_css()

    user_id, user_name = get_logged_user()

    st.markdown(
        """
<div class="hero-title">
    PHÂN LOẠI RÁC THẢI THÔNG MINH - CHỈ VỚI MỘT BỨC ẢNH
</div>
        """,
        unsafe_allow_html=True,
    )

    if user_id and user_name:
        st.success(f"Đang đăng nhập: {user_name} - ID: {user_id}")
    else:
        st.warning("Chưa đăng nhập nên kết quả sẽ không được lưu vào database.")

    col_left, col_right = st.columns([1, 1.45])

    with col_left:
        st.markdown(
            """
<div style="text-align:center; padding-top:35px;">
    <div style="font-size:105px;">👨‍👩‍👧‍👦</div>
    <div style="font-size:82px;">🗑️♻️🗑️</div>
</div>
            """,
            unsafe_allow_html=True,
        )

    with col_right:
        st.markdown(
            """
<div class="upload-box">
    <div class="upload-title">TẢI ẢNH LÊN ĐỂ PHÂN LOẠI</div>
    <div class="upload-icon">☁️</div>
    <div class="upload-text">Kéo thả ảnh hoặc click để chọn tệp</div>
</div>
            """,
            unsafe_allow_html=True,
        )

        uploaded_file = st.file_uploader(
            "Tải ảnh lên để phân loại",
            type=["jpg", "jpeg", "png", "webp"],
            label_visibility="collapsed",
        )

    if uploaded_file is None:
        return

    image = Image.open(uploaded_file).convert("RGB")

    if not st.button("🔍 Nhận diện và lưu kết quả", use_container_width=True):
        return

    try:
        result = predict_waste_image(image)

        if not result.get("success", True):
            st.warning(result.get("message", "AI nhận diện chưa chắc chắn."))

        predicted_class = result.get("predicted_class", "unknown")
        display_name = result.get("display_name", predicted_class)
        confidence = result.get("confidence", 0)

        group_info = get_group_info(predicted_class)

    except Exception as e:
        st.error(f"Lỗi khi nhận diện: {e}")
        return

    group_name = group_info.get("group", "CHƯA XÁC ĐỊNH")
    group_icon = group_info.get("icon", "❓")
    group_desc = group_info.get("desc", "")
    group_action = group_info.get("action", "")

    user_id, user_name = get_logged_user()

    if user_id and user_name:
        try:
            save_result = save_ai_scan_result(
                user_id=user_id,
                user_name=user_name,
                predicted_class=predicted_class,
                confidence=confidence,
                image_name=uploaded_file.name,
            )

            if save_result.get("success"):
                st.session_state["total_score"] = save_result["total_score"]

                st.success(
                    f"Đã lưu vào bảng {save_result['table']} "
                    f"và cộng {save_result['score']} điểm. "
                    f"Tổng điểm hiện tại: {save_result['total_score']} Point."
                )
            else:
                st.warning(save_result.get("message", "Không lưu được kết quả."))

        except Exception as e:
            st.error(f"Lỗi khi lưu database: {e}")
    else:
        st.warning("Chưa đăng nhập nên chưa lưu kết quả vào database.")

    st.markdown(
        '<div class="result-title">KẾT QUẢ PHÂN LOẠI</div>',
        unsafe_allow_html=True,
    )

    col_img, col_result, col_group = st.columns([1.25, 1.6, 1.05])

    with col_img:
        st.markdown('<div class="image-card">', unsafe_allow_html=True)
        st.image(image, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown(
            '<div class="uploaded-caption">Ảnh đã tải</div>',
            unsafe_allow_html=True,
        )

    with col_result:
        render_result_card(
            display_name=display_name,
            confidence=confidence,
            predicted_class=predicted_class,
            group_name=group_name,
            group_desc=group_desc,
            group_action=group_action,
        )

    with col_group:
        render_group_card(
            group_icon=group_icon,
            group_name=group_name,
        )