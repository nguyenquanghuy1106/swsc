import streamlit as st


def render_bottom_nav():
    st.markdown("""
    <div class="bottom-nav">
        <div class="nav-item">⌂</div>
        <div class="nav-item">⌖</div>
        <div class="nav-center">⌲</div>
        <div class="nav-item">⌕</div>
        <div class="nav-item">◉</div>
    </div>
    """, unsafe_allow_html=True)