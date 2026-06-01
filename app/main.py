import streamlit as st
import importlib.util
from pathlib import Path

from shared.styles.news_css import load_news_css
from shared.styles.post_composer_css import load_post_composer_css
from shared.styles.home_css import load_home_css
from shared.styles.plastic_css import load_plastic_css
from shared.styles.battery_css import load_battery_css
from shared.styles.nylon_css import load_nylon_css
from shared.styles.medical_css import load_medical_css

from features.home.UI.home_view import render_home_page
from features.home.UI.view_plastic import render_plastic_page
from features.home.UI.battery_view import render_battery_page
from features.home.UI.nylon_view import render_nylon_page
from features.home.UI.medical_view import render_medical_page
from features.home.UI.AI.ai_viewPlastic import render_ai_page
from features.home.UI.AI.camera_view import render_camera_page
from features.home.UI.user.post_composer_view import render_post_composer_page
from features.home.UI.user.news_view import render_news_page
from features.home.UI.user.profile_view import render_profile_page


BASE_DIR = Path(__file__).resolve().parent

LOGIN_FILE = BASE_DIR / "features" / "Login&Register" / "Login.py"
REGISTER_FILE = BASE_DIR / "features" / "Login&Register" / "Register.py"


def load_function_from_file(file_path, function_name):
    spec = importlib.util.spec_from_file_location(file_path.stem, file_path)

    if spec is None or spec.loader is None:
        raise ImportError(f"Không thể load file: {file_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return getattr(module, function_name)


render_login_page = load_function_from_file(LOGIN_FILE, "render_login_page")
render_register_page = load_function_from_file(REGISTER_FILE, "render_register_page")


VALID_PAGES = {
    "login",
    "register",
    "home",
    "plastic",
    "battery",
    "nylon",
    "medical",
    "ai",
    "camera",
    "post",
    "news",
    "profile",
}


PROTECTED_PAGES = {
    "home",
    "plastic",
    "battery",
    "nylon",
    "medical",
    "camera",
    "post",
    "news",
    "profile",
}


def configure_app():
    st.set_page_config(
        page_title="SWCS",
        page_icon="♻️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )


def restore_login_from_query():
    uid = st.query_params.get("uid")
    uname = st.query_params.get("uname")

    if isinstance(uid, list):
        uid = uid[0]

    if isinstance(uname, list):
        uname = uname[0]

    if uid and uname:
        st.session_state["is_login"] = True
        st.session_state["user_id"] = int(uid)
        st.session_state["user_name"] = uname


def get_current_page():
    restore_login_from_query()

    current_page = st.query_params.get("page", "login")

    if isinstance(current_page, list):
        current_page = current_page[0]

    if current_page not in VALID_PAGES:
        current_page = "login"

    is_login = st.session_state.get("is_login", False)

    if current_page in PROTECTED_PAGES and not is_login:
        current_page = "login"
        st.query_params.clear()
        st.query_params["page"] = "login"

    return current_page


def load_page_styles(page):
    if page == "home":
        load_home_css()
    elif page == "plastic":
        load_plastic_css()
    elif page == "battery":
        load_battery_css()
    elif page == "nylon":
        load_nylon_css()
    elif page == "medical":
        load_medical_css()
    elif page == "post":
        load_post_composer_css()
    elif page == "news":
        load_news_css()


def render_page(page):
    if page == "login":
        render_login_page()
    elif page == "register":
        render_register_page()
    elif page == "home":
        render_home_page()
    elif page == "plastic":
        render_plastic_page()
    elif page == "battery":
        render_battery_page()
    elif page == "nylon":
        render_nylon_page()
    elif page == "medical":
        render_medical_page()
    elif page == "ai":
        render_ai_page()
    elif page == "camera":
        render_camera_page()
    elif page == "post":
        render_post_composer_page()
    elif page == "news":
        render_news_page()
    elif page == "profile":
        render_profile_page()
    else:
        render_login_page()


def main():
    configure_app()

    current_page = get_current_page()
    st.session_state["page"] = current_page

    load_page_styles(current_page)
    render_page(current_page)


if __name__ == "__main__":
    main()