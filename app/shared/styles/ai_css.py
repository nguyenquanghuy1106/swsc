import streamlit as st


def load_ai_css():
    st.markdown(
        """
<style>
.stApp {
    background:
        radial-gradient(circle at top left, rgba(71,199,99,.18), transparent 32%),
        radial-gradient(circle at bottom right, rgba(32,178,170,.15), transparent 30%),
        linear-gradient(135deg, #f3fbf4 0%, #eaf7ee 100%) !important;
}

header[data-testid="stHeader"] {
    display: none;
}

.main .block-container {
    padding-top: 34px;
    padding-bottom: 125px;
    max-width: 1180px;
}

.hero-title {
    text-align: center;
    font-size: 40px;
    font-weight: 950;
    color: #123f1c;
    margin-bottom: 18px;
    background: white;
    border: 1.5px solid #a6d995;
    border-radius: 26px;
    padding: 26px 20px;
    box-shadow: 0 10px 28px rgba(47,125,50,.14);
}

.hero-subtitle {
    font-size: 17px;
    color: #4f704a;
    font-weight: 750;
    margin-top: 8px;
}

.login-status {
    background: #d9f7d8;
    color: #135724;
    padding: 14px 18px;
    border-radius: 18px;
    border: 1px solid #a8dd9a;
    font-weight: 850;
    margin-bottom: 18px;
}

.upload-box {
    border: 2px dashed #45b463;
    border-radius: 24px;
    background: #ffffff;
    padding: 35px;
    text-align: center;
    min-height: 245px;
    box-shadow: 0 10px 28px rgba(47,125,50,.13);
}

.upload-title {
    font-size: 28px;
    font-weight: 950;
    color: #123f1c;
    margin-bottom: 16px;
}

.upload-icon {
    font-size: 72px;
}

.upload-text {
    font-size: 19px;
    color: #405d3b;
    font-weight: 750;
}

div[data-testid="stFileUploader"] label {
    display: none;
}

div[data-testid="stFileUploader"] section {
    background: white !important;
    border: 1.5px dashed #7ccc74 !important;
    border-radius: 18px !important;
}

.ai-illustration-card {
    background: white;
    border: 1.5px solid #bde4b6;
    border-radius: 26px;
    min-height: 330px;
    padding: 34px 24px;
    text-align: center;
    box-shadow: 0 10px 28px rgba(47,125,50,.13);
}

.ai-illustration-main {
    font-size: 105px;
    line-height: 1;
    margin-bottom: 12px;
}

.ai-illustration-icons {
    font-size: 42px;
    margin-bottom: 18px;
}

.ai-illustration-card h3 {
    color: #123f1c;
    font-size: 27px;
    font-weight: 950;
    margin: 0 0 8px;
}

.ai-illustration-card p {
    color: #496c42;
    font-size: 16px;
    font-weight: 750;
    line-height: 1.5;
}

.result-title {
    text-align: center;
    font-size: 42px;
    font-weight: 950;
    color: #123f1c;
    margin-top: 40px;
    margin-bottom: 28px;
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

.stButton button {
    height: 56px !important;
    background: linear-gradient(135deg, #62ce86, #19aaa3) !important;
    color: white !important;
    border: none !important;
    border-radius: 20px !important;
    font-weight: 950 !important;
    font-size: 17px !important;
    box-shadow: 0 10px 24px rgba(25,170,120,.24) !important;
}

.swcs-bottom-nav {
    position: fixed !important;
    left: 50% !important;
    bottom: 18px !important;
    transform: translateX(-50%) !important;
    width: min(560px, calc(100% - 24px)) !important;
    height: 72px !important;
    background: rgba(255,255,255,.96) !important;
    border: 1.5px solid #a6d995 !important;
    border-radius: 28px !important;
    box-shadow: 0 10px 32px rgba(47,125,50,.25) !important;
    display: grid !important;
    grid-template-columns: 1fr 1fr 90px 1fr 1fr !important;
    align-items: center !important;
    justify-items: center !important;
    z-index: 9999 !important;
    backdrop-filter: blur(14px) !important;
}

.swcs-nav-item {
    width: 100% !important;
    height: 58px !important;
    text-decoration: none !important;
    color: #4a4a4a !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 4px !important;
    font-size: 13px !important;
    font-weight: 850 !important;
    white-space: nowrap !important;
}

.swcs-nav-item:hover {
    transform: translateY(-3px) !important;
}

.swcs-nav-icon {
    font-size: 24px !important;
    line-height: 1 !important;
}

.swcs-nav-label {
    font-size: 13px !important;
    line-height: 1 !important;
}

.swcs-scan-btn {
    width: 74px !important;
    height: 74px !important;
    border-radius: 50% !important;
    background: linear-gradient(135deg,#42c96f,#1aa6a6) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    margin-top: -36px !important;
    border: 5px solid #fff !important;
    box-shadow: 0 8px 24px rgba(26,166,166,.42) !important;
    text-decoration: none !important;
}

.swcs-nav-ai {
    font-size: 32px !important;
    line-height: 1 !important;
}
</style>
        """,
        unsafe_allow_html=True,
    )