import streamlit as st


def load_ai_css():
    st.markdown(
        """
<style>
.stApp {
    background: linear-gradient(135deg, #f3fbf4 0%, #eaf7ee 100%);
}

header {
    visibility: hidden;
}

.main .block-container {
    padding-top: 0rem;
    max-width: 1380px;
}

.navbar {
    height: 76px;
    background: #ffffff;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 70px;
    box-shadow: 0 3px 18px rgba(0,0,0,0.08);
    margin: -1rem -4rem 34px -4rem;
}

.logo {
    display: flex;
    align-items: center;
    gap: 13px;
    font-size: 27px;
    font-weight: 900;
    color: #2f8f43;
}

.menu {
    display: flex;
    gap: 38px;
    font-size: 18px;
    font-weight: 800;
    color: #111;
}

.hero-title {
    text-align: center;
    font-size: 40px;
    font-weight: 950;
    color: #0b0b0b;
    margin-bottom: 35px;
}

.result-title {
    text-align: center;
    font-size: 48px;
    font-weight: 950;
    color: #0b0b0b;
    margin-top: 45px;
    margin-bottom: 32px;
}

.upload-box {
    border: 3px dashed #2f2f2f;
    border-radius: 18px;
    background: #ffffff;
    padding: 35px;
    text-align: center;
    min-height: 215px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
}

.upload-title {
    font-size: 28px;
    font-weight: 950;
    color: #111;
    margin-bottom: 16px;
}

.upload-icon {
    font-size: 66px;
}

.upload-text {
    font-size: 20px;
    color: #222;
    font-weight: 600;
}

div[data-testid="stFileUploader"] label {
    display: none;
}

.image-card {
    background: #ffffff;
    border-radius: 22px;
    padding: 14px;
    box-shadow: 0 12px 32px rgba(0,0,0,0.14);
}

.uploaded-caption {
    text-align: center;
    font-size: 22px;
    color: #111;
    font-weight: 900;
    margin-top: 14px;
}
</style>
        """,
        unsafe_allow_html=True,
    )