import streamlit as st

from features.home.logic.user.post_composer_service import (
    create_post_payload,
    get_post_composer_view_model,
    validate_post_content,
)


def _get_visibility_icon(visibility: str) -> str:
    mapping = {
        "Công khai": "🌍",
        "Bạn bè": "👥",
        "Riêng tư": "🔒",
    }
    return mapping.get(visibility, "🕒")


def _sync_visibility_state(default_visibility: str):
    # Khởi tạo state chính
    if "composer_visibility" not in st.session_state:
        st.session_state["composer_visibility"] = default_visibility

    # Nếu selectbox đã từng thay đổi, đồng bộ ngược lên chip/header ngay từ đầu run
    if "composer_visibility_selectbox" in st.session_state:
        st.session_state["composer_visibility"] = st.session_state["composer_visibility_selectbox"]


def _render_navbar(vm: dict):
    nav_items_html = "".join(
        f'<a href="{item["href"]}">{item["label"]}</a>'
        for item in vm["branding"]["nav_items"]
    )

    navbar_html = (
        '<div class="swcs-community-nav">'
        '  <div class="swcs-community-brand">'
        '    <span class="swcs-community-brand-icon">🌿</span>'
        f'    <span>{vm["branding"]["app_name"]}</span>'
        '  </div>'
        f'  <div class="swcs-community-links">{nav_items_html}</div>'
        '  <div class="swcs-community-search">🔍</div>'
        '</div>'
    )
    st.markdown(navbar_html, unsafe_allow_html=True)


def _render_post_message():
    message = st.session_state.get("post_message", "")
    message_type = st.session_state.get("post_message_type", "")

    if not message:
        return

    css_class = "swcs-post-success" if message_type == "success" else "swcs-post-error"
    st.markdown(
        f'<div class="swcs-post-message {css_class}">{message}</div>',
        unsafe_allow_html=True,
    )


def _render_profile_header(vm: dict):
    user = vm["user"]
    visibility = st.session_state.get("composer_visibility", user["default_visibility"])
    visibility_icon = _get_visibility_icon(visibility)

    profile_html = (
        '<div class="swcs-composer-top">'
        '  <div class="swcs-composer-user">'
        '    <div class="swcs-composer-avatar">'
        f'      <img src="{user["avatar_url"]}" alt="avatar">'
        '    </div>'
        '    <div class="swcs-composer-meta">'
        f'      <div class="swcs-composer-name">{user["name"]}</div>'
        f'      <div class="swcs-composer-chip">{visibility_icon} {visibility} ▼</div>'
        '    </div>'
        '  </div>'
        '</div>'
    )
    st.markdown(profile_html, unsafe_allow_html=True)


def _render_action_card(icon: str, label: str):
    html = (
        '<div class="swcs-action-card">'
        f'  <div class="swcs-action-icon">{icon}</div>'
        f'  <div class="swcs-action-label">{label}</div>'
        '</div>'
    )
    st.markdown(html, unsafe_allow_html=True)


def _render_action_cards(vm: dict):
    items = vm["branding"]["action_items"]
    col1, col2 = st.columns(2, gap="medium")

    with col1:
        for item in [items[0], items[2]]:
            _render_action_card(item["icon"], item["label"])
            st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    with col2:
        for item in [items[1], items[3]]:
            _render_action_card(item["icon"], item["label"])
            st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    st.markdown(
        '<div class="swcs-mini-dots">'
        '  <div class="swcs-mini-dot active"></div>'
        '  <div class="swcs-mini-dot"></div>'
        '</div>',
        unsafe_allow_html=True,
    )


def render_post_composer_page():
    vm = get_post_composer_view_model()
    defaults = vm["defaults"]

    _sync_visibility_state(defaults["visibility"])

    _render_navbar(vm)

    top_left, top_right = st.columns([6, 2], gap="medium")

    with top_left:
        _render_profile_header(vm)

    with top_right:
        st.markdown('<div class="swcs-top-post-btn-space"></div>', unsafe_allow_html=True)
        submitted = st.button(
            vm["branding"]["post_button_text"] + " ➤",
            key="composer_main_submit_btn",
            use_container_width=True,
        )

    _render_post_message()

    visibility_options = vm["branding"]["visibility_options"]
    current_visibility = st.session_state["composer_visibility"]
    current_index = visibility_options.index(current_visibility)

    visibility = st.selectbox(
        "Chế độ hiển thị",
        visibility_options,
        index=current_index,
        key="composer_visibility_selectbox",
    )

    # Đồng bộ ngay sau widget để lần tương tác tiếp theo và rerun hiện đúng
    st.session_state["composer_visibility"] = visibility

    post_text = st.text_area(
        "",
        value=defaults["post_text"],
        placeholder=vm["branding"]["post_placeholder"],
        label_visibility="collapsed",
        key="composer_post_text",
    )

    uploaded_files = []
    location = ""
    feeling = ""

    with st.expander("Tùy chọn bổ sung", expanded=False):
        uploaded_files = st.file_uploader(
            "Tải ảnh/video",
            accept_multiple_files=True,
            type=["png", "jpg", "jpeg", "webp", "mp4", "mov"],
            key="composer_file_uploader",
        )
        location = st.text_input(
            "Check in",
            value=defaults["location"],
            placeholder="Bạn đang ở đâu?",
            key="composer_location",
        )
        feeling = st.text_input(
            "Cảm xúc",
            value=defaults["feeling"],
            placeholder="Bạn đang cảm thấy thế nào?",
            key="composer_feeling",
        )

    st.markdown(
        '<div class="swcs-helper-row">'
        '  <div class="swcs-helper-badge">🖼️ Ảnh / Video</div>'
        '  <div class="swcs-helper-badge">📍 Check in</div>'
        '  <div class="swcs-helper-badge">📷 Camera</div>'
        '  <div class="swcs-helper-badge">😊 Cảm xúc</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    if submitted:
        uploaded_files = uploaded_files or []
        location = location or ""
        feeling = feeling or ""

        is_valid, message = validate_post_content(
            post_text=post_text,
            uploaded_media_count=len(uploaded_files),
            location=location,
            feeling=feeling,
        )

        if is_valid:
            payload = create_post_payload(
                author_name=vm["user"]["name"],
                visibility=visibility,
                post_text=post_text,
                uploaded_files=[getattr(file, "name", "file") for file in uploaded_files],
                location=location,
                feeling=feeling,
            )
            st.session_state["latest_post_payload"] = payload
            st.session_state["post_message"] = "Đăng bài thành công."
            st.session_state["post_message_type"] = "success"
        else:
            st.session_state["post_message"] = message
            st.session_state["post_message_type"] = "error"

        st.rerun()

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    st.markdown('<div class="swcs-bottom-actions-shell">', unsafe_allow_html=True)
    _render_action_cards(vm)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)