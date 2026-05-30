import streamlit as st
import importlib.util
from pathlib import Path

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


BASE_DIR = Path(__file__).resolve().parent
LOGIN_FILE = BASE_DIR / "features" / "Login&Register" / "Login.py"
REGISTER_FILE = BASE_DIR / "features" / "Login&Register" / "Register.py"


def load_function_from_file(file_path, function_name):
    spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
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
}


def configure_app():
    st.set_page_config(
        page_title="SWCS",
        page_icon="♻️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )


def get_current_page():
    current_page = st.query_params.get("page", "login")

    if isinstance(current_page, list):
        current_page = current_page[0]

    if current_page not in VALID_PAGES:
        current_page = "login"

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


def render_page(page):
    if page not in ["login", "register"]:
        if not st.session_state.get("is_login", False):
            st.query_params["page"] = "login"
            st.rerun()

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