import streamlit as st

from features.home.logic.user.register_service import (
    get_register_view_model,
    register_user,
)


def _render_message_box():
    message = st.session_state.get("register_message", "")
    message_type = st.session_state.get("register_message_type", "")

    if not message:
        return

    css_class = "register-auth-success" if message_type == "success" else "register-auth-error"
    st.markdown(
        f'<div class="register-auth-message {css_class}">{message}</div>',
        unsafe_allow_html=True,
    )


def _render_info_panel(app_name: str):
    st.markdown(
        (
            '<div class="register-info-panel">'
            '  <div class="register-brand-line">'
            '    <div class="register-brand-leaf">🌿</div>'
            f'    <div class="register-brand-name">{app_name}</div>'
            '  </div>'
            '  <div class="register-hero-title">Tạo tài khoản với <span class="register-accent-text">SWCS</span></div>'
            '  <div class="register-hero-desc">'
            '    Tham gia hệ thống phân loại rác thông minh để bắt đầu hành trình sống xanh, '
            '    quản lý thông tin dễ dàng và tiếp cận nhiều nội dung hữu ích về môi trường mỗi ngày.'
            '  </div>'
            '  <div class="register-feature-item">'
            '    <div class="register-feature-icon">🌱</div>'
            '    <div class="register-feature-text">Bắt đầu hành trình sống xanh cùng một tài khoản cá nhân đơn giản và hiện đại.</div>'
            '  </div>'
            '  <div class="register-feature-item">'
            '    <div class="register-feature-icon">♻</div>'
            '    <div class="register-feature-text">Tiếp cận các tính năng phân loại rác, kiến thức tái chế và thông điệp môi trường.</div>'
            '  </div>'
            '  <div class="register-feature-item">'
            '    <div class="register-feature-icon">🔒</div>'
            '    <div class="register-feature-text">Thông tin đăng ký rõ ràng, giao diện thân thiện và trải nghiệm dễ sử dụng.</div>'
            '  </div>'
            '  <div class="register-info-note">“Cùng SWCS tạo nên thói quen xanh cho hôm nay và mai sau.”</div>'
            '</div>'
        ),
        unsafe_allow_html=True,
    )


def _render_card_top():
    st.markdown('<div class="register-card-topline"></div>', unsafe_allow_html=True)


def render_register_page():
    vm = get_register_view_model()
    branding = vm["branding"]
    defaults = vm["defaults"]

    left, right = st.columns([1.02, 0.98], gap="large")

    with left:
        _render_info_panel(branding["app_name"])

    with right:
        st.markdown('<div class="register-form-panel">', unsafe_allow_html=True)

        _render_card_top()

        st.markdown(
            f"""
            <div class="register-panel-title">{branding["title"]}</div>
            <div class="register-panel-subtitle">{branding["subtitle"]}</div>

            <div class="register-top-tabs">
                <a class="register-pill-ghost" href="?page=login">{branding["login_text"]}</a>
                <div class="register-pill-active">{branding["register_text"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        _render_message_box()

        with st.form("register_page_form", clear_on_submit=False):
            full_name = st.text_input("Tên", value=defaults["full_name"], placeholder="Nhập tên")
            email = st.text_input("Email", value=defaults["email"], placeholder="Nhập email")
            password = st.text_input(
                "Mật khẩu",
                value=defaults["password"],
                placeholder="Nhập mật khẩu",
                type="password",
            )
            confirm_password = st.text_input(
                "Xác nhận mật khẩu",
                value=defaults["confirm_password"],
                placeholder="Nhập lại mật khẩu",
                type="password",
            )
            agree_terms = st.checkbox(
                "Tôi đồng ý với điều khoản sử dụng",
                value=defaults["agree_terms"],
            )

            submitted = st.form_submit_button(branding["button_text"])

        if submitted:
            success, message = register_user(
                full_name=full_name,
                email=email,
                password=password,
                confirm_password=confirm_password,
                agree_terms=agree_terms,
            )
            st.session_state["register_message"] = message
            st.session_state["register_message_type"] = "success" if success else "error"

            if success:
                st.query_params["page"] = "login"

            st.rerun()

        st.markdown(
            f'<div class="register-bottom-text">{branding["footer_text"]} '
            f'<a class="register-bottom-link" href="?page=login">{branding["footer_link_text"]}</a></div>',
            unsafe_allow_html=True,
        )

        st.markdown('</div>', unsafe_allow_html=True)