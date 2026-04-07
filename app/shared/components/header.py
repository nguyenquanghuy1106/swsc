import streamlit as st


def render_top_icons():
    st.markdown("""
    <div class="top-row">
        <div class="icon-btn">☰</div>
        <div class="icon-btn">🔔</div>
    </div>
    """, unsafe_allow_html=True)