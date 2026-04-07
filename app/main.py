import streamlit as st
from .shared.styles.global_css import load_global_css
from .features.home.UI.page import render_home_page


def run_app():
    st.set_page_config(
        page_title="SWCS - Trang chủ",
        page_icon="♻️",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    load_global_css()
    render_home_page()