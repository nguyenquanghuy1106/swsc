import streamlit as st

from shared.styles.home_css import load_home_css
from shared.styles.user.login_css import load_login_css
from shared.styles.user.register_css import load_register_css
from shared.styles.user.homepage_user_css import load_homepage_user_css
from shared.styles.user.post_composer_css import load_post_composer_css
from shared.styles.user.setting_user_css import load_setting_user_css
from shared.styles.plastic_css import load_plastic_css
from shared.styles.battery_css import load_battery_css
from shared.styles.nylon_css import load_nylon_css
from shared.styles.medical_css import load_medical_css

from features.home.UI.home_view import render_home_page
from features.home.UI.user.login_view import render_login_page
from features.home.UI.user.register_view import render_register_page
from features.home.UI.user.homepage_user_view import render_homepage_user_page
from features.home.UI.user.post_composer_view import render_post_composer_page
from features.home.UI.user.setting_user_view import render_setting_user_page
from features.home.UI.view_plastic import render_plastic_page
from features.home.UI.battery_view import render_battery_page
from features.home.UI.nylon_view import render_nylon_page
from features.home.UI.medical_view import render_medical_page


def configure_app():
    st.set_page_config(
        page_title="SWCS - Trang chủ",
        page_icon="♻️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )


def get_current_page() -> str:
    current_page = st.query_params.get("page", "homepage_user")
    if isinstance(current_page, list):
        current_page = current_page[0]
    return current_page


def load_page_styles(page: str):
    if page == "login":
        load_login_css()
    elif page == "register":
        load_register_css()
    elif page == "community":
        load_post_composer_css()
    elif page == "setting_user":
        load_setting_user_css()
    elif page == "homepage_user":
        load_homepage_user_css()
    elif page == "home":
        load_home_css()
    elif page == "plastic":
        load_plastic_css()
    elif page == "battery":
        load_battery_css()
    elif page == "nylon":
        load_nylon_css()
    elif page == "medical":
        load_medical_css()
    else:
        load_login_css()


def render_page(page: str):
    if page == "login":
        render_login_page()
    elif page == "register":
        render_register_page()
    elif page == "community":
        render_post_composer_page()
    elif page == "setting_user":
        render_setting_user_page()
    elif page == "homepage_user":
        render_homepage_user_page()
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


def run_app():
    configure_app()

    current_page = get_current_page()
    st.session_state["page"] = current_page

    load_page_styles(current_page)
    render_page(current_page)


def main():
    run_app()


if __name__ == "__main__":
    main()