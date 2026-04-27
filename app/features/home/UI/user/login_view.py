import streamlit as st

from features.home.logic.user.auth_service import (
    authenticate_user,
    get_auth_view_model,
    register_user,
)


def _render_message_box():
    message = st.session_state.get("auth_message", "")
    message_type = st.session_state.get("auth_message_type", "")

    if not message:
        return

    css_class = "swcs-auth-success" if message_type == "success" else "swcs-auth-error"
    st.markdown(
        f'<div class="swcs-auth-message {css_class}">{message}</div>',
        unsafe_allow_html=True,
    )


def _render_info_panel(app_name: str):
    st.markdown(
        (
            '<div class="login-info-panel">'
            '  <div class="login-brand-line">'
            '    <div class="login-brand-leaf">🌿</div>'
            f'    <div class="login-brand-name">{app_name}</div>'
            '  </div>'
            '</div>'
        ),
        unsafe_allow_html=True,
    )

    st.markdown(
        '### Chào mừng đến với <span class="accent-text">SWCS</span>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="login-hero-desc">
            Nền tảng hỗ trợ phân loại rác thông minh, trực quan và dễ sử dụng.
            Bắt đầu hành trình sống xanh bằng một trải nghiệm đăng nhập đơn giản,
            hiện đại và thân thiện.
        </div>
        """,
        unsafe_allow_html=True,
    )

    features = [
        ("♻", "Phân loại rác nhanh chóng với giao diện dễ hiểu và tối ưu cho người dùng."),
        ("🌱", "Lan tỏa lối sống xanh bằng những hành động nhỏ nhưng bền vững mỗi ngày."),
        ("📊", "Quản lý, theo dõi và học thêm kiến thức môi trường trong cùng một hệ thống."),
    ]

    for icon, text in features:
        st.markdown(
            (
                '<div class="login-feature-item">'
                f'  <div class="login-feature-icon">{icon}</div>'
                f'  <div class="login-feature-text">{text}</div>'
                '</div>'
            ),
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="login-info-note">“Phân loại hôm nay, xanh mãi ngày mai.”</div>',
        unsafe_allow_html=True,
    )


def _render_card_top():
    st.markdown('<div class="login-card-topline"></div>', unsafe_allow_html=True)


def _render_login_form(vm: dict):
    branding = vm["branding"]
    defaults = vm["login_defaults"]

    _render_card_top()

    st.markdown(
        (
            f'<div class="login-panel-title">{branding["login_title"]}</div>'
            f'<div class="login-panel-subtitle">{branding["login_subtitle"]}</div>'
            '<div class="login-top-tabs">'
            '  <div class="login-pill-active">Đăng nhập</div>'
            '  <a class="login-pill-ghost login-tab-link" href="?page=register">Đăng ký</a>'
            '</div>'
        ),
        unsafe_allow_html=True,
    )

    _render_message_box()

    with st.form("login_form", clear_on_submit=False):
        email = st.text_input("Email", value=defaults["email"], placeholder="Nhập email")
        password = st.text_input(
            "Mật khẩu",
            value=defaults["password"],
            placeholder="Nhập mật khẩu",
            type="password",
        )

        c1, c2 = st.columns([1, 1])
        with c1:
            remember = st.checkbox("Nhớ đăng nhập", value=defaults["remember"])
        with c2:
            st.markdown(
                '<div class="login-inline-right"><a class="login-forgot-link" href="#">Quên mật khẩu?</a></div>',
                unsafe_allow_html=True,
            )

        submitted = st.form_submit_button("Đăng nhập")

    if submitted:
        success, message = authenticate_user(email, password)
        st.session_state["remember_login"] = remember
        st.session_state["auth_message"] = message
        st.session_state["auth_message_type"] = "success" if success else "error"

        if success:
            st.query_params["page"] = "home"

        st.rerun()

    st.markdown('<div class="login-divider">Hoặc</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="login-google-btn">🔵 {branding["google_button_text"]}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="login-bottom-text">Chưa có tài khoản? <a class="login-bottom-link" href="?page=register">Đăng ký ngay</a></div>',
        unsafe_allow_html=True,
    )


def _render_register_form(vm: dict):
    branding = vm["branding"]
    defaults = vm["register_defaults"]

    _render_card_top()

    st.markdown(
        (
            f'<div class="login-panel-title">{branding["register_title"]}</div>'
            f'<div class="login-panel-subtitle">{branding["register_subtitle"]}</div>'
            '<div class="login-top-tabs">'
            '  <a class="login-pill-ghost login-tab-link" href="?page=login">Đăng nhập</a>'
            '  <div class="login-pill-active">Đăng ký</div>'
            '</div>'
        ),
        unsafe_allow_html=True,
    )

    _render_message_box()

    with st.form("register_form", clear_on_submit=False):
        full_name = st.text_input("Họ và tên", value=defaults["full_name"], placeholder="Nhập họ và tên")
        email = st.text_input("Email", value=defaults["email"], placeholder="Nhập email")
        password = st.text_input("Mật khẩu", value=defaults["password"], placeholder="Tạo mật khẩu", type="password")
        confirm_password = st.text_input(
            "Xác nhận mật khẩu",
            value=defaults["confirm_password"],
            placeholder="Nhập lại mật khẩu",
            type="password",
        )
        agree_terms = st.checkbox("Tôi đồng ý với điều khoản sử dụng", value=defaults["agree_terms"])

        submitted = st.form_submit_button("Đăng ký")

    if submitted:
        success, message = register_user(
            full_name=full_name,
            email=email,
            password=password,
            confirm_password=confirm_password,
            agree_terms=agree_terms,
        )
        st.session_state["auth_message"] = message
        st.session_state["auth_message_type"] = "success" if success else "error"
        st.rerun()

    st.markdown(
        '<div class="login-bottom-text">Đã có tài khoản? <a class="login-bottom-link" href="?page=login">Đăng nhập ngay</a></div>',
        unsafe_allow_html=True,
    )


def render_login_page(mode: str = "login"):
    vm = get_auth_view_model()


    left, right = st.columns([1.0, 1.0], gap="large")

    with left:
        _render_info_panel(vm["branding"]["app_name"])

    with right:
        st.markdown('<div class="login-form-panel">', unsafe_allow_html=True)

        if mode == "register":
            _render_register_form(vm)
        else:
            _render_login_form(vm)

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)