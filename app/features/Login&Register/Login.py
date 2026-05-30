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


def login_user(user_name, password):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM Register WHERE userName = %s AND password = %s",
        (user_name, password)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user


def render_login_page():
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
            st.markdown('<div class="form-title">Sign in</div>', unsafe_allow_html=True)

            user_name = st.text_input(
                "Username",
                placeholder="Tên đăng nhập",
                label_visibility="collapsed"
            )

            password = st.text_input(
                "Password",
                placeholder="Mật khẩu",
                type="password",
                label_visibility="collapsed"
            )

            if st.button("Sign in"):
                if not user_name or not password:
                    st.error("Vui lòng nhập đầy đủ tên đăng nhập và mật khẩu")
                else:
                    user = login_user(user_name, password)

                    if user:
                        st.session_state["is_login"] = True
                        st.session_state["user_id"] = user["id"]
                        st.session_state["user_name"] = user["userName"]

                        st.query_params["page"] = "home"
                        st.rerun()
                    else:
                        st.error("Sai tên đăng nhập hoặc mật khẩu")

            if st.button("Sign up here"):
                st.query_params["page"] = "register"
                st.rerun()