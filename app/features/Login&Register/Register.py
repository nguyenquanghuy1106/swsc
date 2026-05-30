import streamlit as st
from pathlib import Path
import base64

from features.database.connection import get_connection


BASE_DIR = Path(__file__).resolve().parents[3]
BG_PATH = BASE_DIR / "assets" / "auth" / "register.jpg"
CSS_PATH = BASE_DIR / "app" / "features" / "Login&Register" / "Register.css"


def image_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def load_css(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def load_auth_style():
    bg_base64 = image_to_base64(BG_PATH)
    css = load_css(CSS_PATH)

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image:
                linear-gradient(rgba(0,0,0,0.25), rgba(0,0,0,0.25)),
                url("data:image/jpg;base64,{bg_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}

        {css}
        </style>
        """,
        unsafe_allow_html=True
    )


def register_user(user_name, phone, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM Register WHERE userName = %s OR phone = %s",
        (user_name, phone)
    )

    exists = cursor.fetchone()

    if exists:
        cursor.close()
        conn.close()
        return False, "Tên người dùng hoặc số điện thoại đã tồn tại"

    cursor.execute(
        "INSERT INTO Register (userName, phone, password) VALUES (%s, %s, %s)",
        (user_name, phone, password)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return True, "Đăng ký thành công"


def render_register_page():
    load_auth_style()

    st.markdown('<div class="page-space"></div>', unsafe_allow_html=True)

    left_blank, card, right_blank = st.columns([0.12, 0.76, 0.12])

    with card:
        left, right = st.columns([1.15, 1])

        with left:
            st.markdown(
                """
                <div class="left-panel">
                    <h1>SWCS</h1>
                    <p>
                        Phân loại rác hôm nay – Bảo vệ môi trường ngày mai.
                        Vì một thế giới xanh sạch đẹp không rác thải nguy hại.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with right:
            st.markdown('<div class="form-title">Sign up</div>', unsafe_allow_html=True)

            user_name = st.text_input(
                "Username",
                placeholder="Tên của bạn",
                label_visibility="collapsed"
            )

            phone = st.text_input(
                "Phone",
                placeholder="Số điện thoại",
                label_visibility="collapsed"
            )

            password = st.text_input(
                "Password",
                placeholder="Tạo mật khẩu",
                type="password",
                label_visibility="collapsed"
            )

            confirm_password = st.text_input(
                "Confirm Password",
                placeholder="Nhập lại mật khẩu",
                type="password",
                label_visibility="collapsed"
            )

            if st.button("Sign up"):
                if not user_name or not phone or not password or not confirm_password:
                    st.error("Vui lòng nhập đầy đủ thông tin")
                elif password != confirm_password:
                    st.error("Mật khẩu nhập lại không khớp")
                else:
                    success, message = register_user(user_name, phone, password)

                    if success:
                        st.query_params["page"] = "login"
                        st.rerun()
                    else:
                        st.error(message)

            if st.button("Sign in here"):
                st.query_params["page"] = "login"
                st.rerun()