import streamlit as st


def load_global_css():
    st.markdown("""
    <style>
    .stApp {
        background: #f4f4f4;
    }

    .main .block-container {
        max-width: 430px;
        padding-top: 1rem;
        padding-bottom: 2rem;
    }

    .phone-shell {
        background: #ffffff;
        border-radius: 28px;
        padding: 18px 16px 90px 16px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.08);
        position: relative;
        min-height: 860px;
    }

    .top-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 18px;
    }

    .icon-btn {
        font-size: 22px;
        font-weight: bold;
        color: #222;
    }

    .profile-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }

    .profile-left {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .avatar-circle {
        width: 54px;
        height: 54px;
        border-radius: 50%;
        overflow: hidden;
        border: 4px solid #d7f0d2;
        box-shadow: 0 3px 10px rgba(0,0,0,0.12);
    }

    .user-name {
        font-size: 20px;
        font-weight: 700;
        color: #222;
    }

    .point-badge {
        background: #59b35a;
        color: white;
        border-radius: 999px;
        padding: 10px 18px;
        font-weight: 700;
        font-size: 14px;
        box-shadow: 0 4px 10px rgba(89,179,90,0.35);
    }

    .hero-title {
        font-size: 30px;
        line-height: 1.15;
        font-weight: 800;
        color: #111;
        margin-bottom: 8px;
    }

    .green-text {
        color: #5bb65d;
    }

    .hero-sub {
        color: #757575;
        font-size: 16px;
        margin-top: 10px;
        margin-bottom: 18px;
    }

    .hero-layout {
        display: flex;
        gap: 14px;
        margin-top: 6px;
        margin-bottom: 8px;
        min-height: 380px;
    }

    .hero-left-content {
        flex: 1;
        min-width: 0;
        padding-right: 8px;
    }

    .hero-right-stack {
        width: 44%;
        min-width: 150px;
        position: relative;
        padding-top: 4px;
    }

    .hero-card {
        border-radius: 22px;
        object-fit: cover;
        box-shadow: 0 6px 14px rgba(0,0,0,0.12);
        border: 3px solid #2da8ff;
        display: block;
    }

    .hero-card-top,
    .hero-card-bottom {
        width: 100%;
        height: 168px;
    }

    .hero-card-bottom {
        margin-top: 14px;
    }

    .hero-card-middle {
        position: absolute;
        width: 138px;
        height: 210px;
        left: -128px;
        top: 128px;
        z-index: 3;
    }

    .main-btn {
        display: inline-block;
        background: #57b35b;
        color: white;
        border-radius: 999px;
        padding: 12px 22px;
        font-weight: 700;
        text-decoration: none;
        margin-top: 8px;
    }

    .section-title-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 26px;
        margin-bottom: 14px;
    }

    .section-title {
        font-size: 16px;
        font-weight: 800;
        color: #111;
    }

    .see-all {
        color: #5bb65d;
        font-weight: 700;
        font-size: 14px;
    }

    .category-card {
        text-align: center;
    }

    .category-circle {
        width: 78px;
        height: 78px;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0 auto 8px auto;
        box-shadow: 0 4px 10px rgba(0,0,0,0.06);
    }

    .category-name {
        font-size: 14px;
        font-weight: 700;
        color: #222;
    }

    .promo-banner {
        margin-top: 16px;
        border-radius: 18px;
        overflow: hidden;
        box-shadow: 0 6px 16px rgba(0,0,0,0.08);
    }

    .bottom-nav {
        position: absolute;
        left: 0;
        right: 0;
        bottom: 0;
        background: #5cb85c;
        border-top-left-radius: 34px;
        border-top-right-radius: 34px;
        padding: 14px 24px 18px 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .nav-item {
        color: white;
        font-size: 24px;
        text-align: center;
    }

    .nav-center {
        width: 62px;
        height: 62px;
        background: #eef6ff;
        border-radius: 50%;
        margin-top: -35px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: black;
        font-size: 28px;
        box-shadow: 0 6px 14px rgba(0,0,0,0.12);
        border: 6px solid #dce8ff;
    }

    .hero-right-img {
        border-radius: 18px;
        overflow: hidden;
        box-shadow: 0 6px 14px rgba(0,0,0,0.12);
        margin-bottom: 12px;
    }
    </style>
    """, unsafe_allow_html=True)