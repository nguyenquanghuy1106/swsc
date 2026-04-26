import streamlit as st


def load_home_css():
    
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #f7faf7 0%, #eef6ef 100%);
    }

    .main .block-container {
        max-width: 1500px;
        padding-top: 1rem;
        padding-bottom: 2rem;
    }

    div[data-testid="stHorizontalBlock"] {
        align-items: stretch;
    }

    .swcs-topbar,
    .swcs-sidebar,
    .swcs-hero,
    .swcs-category-card,
    .swcs-info-box,
    .swcs-footer {
        box-sizing: border-box;
    }

    .swcs-topbar {
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 20px;
        margin-bottom: 18px;
        padding: 4px 0 10px 0;
    }

    .swcs-topbar-title {
        font-size: 23px;
        font-weight: 800;
        color: #1f2937;
        line-height: 1.3;
    }

    .swcs-topbar-right {
        display: flex;
        align-items: center;
        justify-content: flex-end;
        gap: 12px;
        flex-wrap: nowrap;
    }

    .swcs-search-box {
        min-width: 180px;
        height: 42px;
        border-radius: 999px;
        background: #ffffff;
        border: 1px solid #e5e7eb;
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 0 14px;
        color: #9ca3af;
        font-size: 14px;
        font-weight: 600;
        box-shadow: 0 4px 10px rgba(15, 23, 42, 0.04);
    }

    .swcs-noti-wrap {
        position: relative;
        width: 40px;
        height: 40px;
        flex: 0 0 40px;
    }

    .swcs-noti-icon {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: #ffffff;
        border: 1px solid #e5e7eb;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
        box-shadow: 0 4px 10px rgba(15, 23, 42, 0.04);
    }

    .swcs-noti-badge {
        position: absolute;
        top: -4px;
        right: -2px;
        min-width: 16px;
        height: 16px;
        border-radius: 999px;
        background: #ef4444;
        color: #fff;
        font-size: 10px;
        font-weight: 700;
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 2;
        padding: 0 4px;
    }

    .swcs-avatar-wrap {
        width: 42px;
        height: 42px;
        border-radius: 50%;
        overflow: hidden;
        border: 1px solid #e5e7eb;
        background: #ffffff;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 10px rgba(15, 23, 42, 0.04);
        flex: 0 0 42px;
    }

    .swcs-avatar-img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
    }

    .swcs-avatar-fallback {
        font-size: 20px;
    }
    .swcs-sidebar-wrapper {
    position: relative;
    width: 100%;
    }

    .swcs-sidebar-checkbox {
        display: none;
    }

    .swcs-sidebar-toggle {
        display: none;
        width: 46px;
        height: 46px;
        border-radius: 14px;
        background: rgba(255, 255, 255, 0.92);
        border: 1px solid #dbe5dc;
        color: #256f3a;
        font-size: 24px;
        font-weight: 800;
        align-items: center;
        justify-content: center;
        box-shadow: 0 8px 20px rgba(15, 23, 42, 0.08);
        cursor: pointer;
        user-select: none;
        margin-bottom: 12px;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
    }

    .swcs-sidebar-overlay {
        display: none;
    }
    .swcs-sidebar {
        background: #ffffff;
        border: 1px solid #e8ece8;
        border-radius: 24px;
        padding: 22px 16px;
        min-height: 1180px;
        box-shadow: 0 10px 24px rgba(15, 23, 42, 0.04);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .swcs-logo-wrap {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 24px;
        padding-left: 4px;
    }

    .swcs-logo-icon {
        font-size: 26px;
        color: #59a96a;
        font-weight: 800;
    }

    .swcs-logo-text {
        font-size: 22px;
        font-weight: 800;
        color: #1f2937;
    }

    .swcs-menu {
        display: flex;
        flex-direction: column;
        gap: 10px;
        flex: 1;
    }

    .swcs-menu-item {
        text-decoration: none;
        color: #4b5563;
        font-size: 17px;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 13px 14px;
        border-radius: 14px;
        transition: all 0.2s ease;
        background: transparent;
    }

    .swcs-menu-item:hover {
        background: #f3f8f3;
        color: #256f3a;
    }

    .swcs-menu-item.active {
        background: #65b875;
        color: #ffffff;
        box-shadow: 0 8px 18px rgba(101, 184, 117, 0.22);
    }

    .swcs-sidebar-bottom {
        display: flex;
        align-items: center;
        gap: 14px;
        padding-top: 20px;
        margin-top: 24px;
        border-top: 1px solid #eef1ee;
    }

    .swcs-bottom-icon {
        width: 38px;
        height: 38px;
        border-radius: 50%;
        background: #f3f8f3;
        color: #65b875;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        font-weight: 700;
    }

    .swcs-hero {
        width: 100%;
        min-height: 380px;
        border-radius: 28px;
        overflow: hidden;
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        box-shadow: 0 12px 30px rgba(88, 120, 90, 0.08);
        margin-bottom: 28px;
    }

    .swcs-hero-overlay {
        min-height: 380px;
        display: flex;
        align-items: center;
        padding: 48px 42px;
        background: linear-gradient(90deg, rgba(255,255,255,0.80) 0%, rgba(255,255,255,0.45) 45%, rgba(255,255,255,0.08) 100%);
    }

    .swcs-hero-content {
        max-width: 520px;
    }

    .swcs-hero-title {
        font-size: 56px;
        line-height: 1.1;
        font-weight: 900;
        color: #1f2937;
        margin-bottom: 18px;
    }

    .swcs-hero-title span {
        color: #5fa46b;
    }

    .swcs-hero-sub {
        font-size: 24px;
        line-height: 1.5;
        color: #374151;
        margin-bottom: 24px;
    }

    .swcs-hero-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        padding: 14px 28px;
        border-radius: 999px;
        background: linear-gradient(90deg, #74bd78 0%, #4f9957 100%);
        color: #ffffff;
        font-size: 19px;
        font-weight: 800;
        box-shadow: 0 10px 22px rgba(79, 153, 87, 0.25);
    }

    .swcs-section-title {
        font-size: 30px;
        font-weight: 900;
        color: #1f2937;
        margin-bottom: 18px;
    }

    .swcs-category-card {
        display: block;
        text-decoration: none;
        background: #ffffff;
        border-radius: 24px;
        padding: 14px 14px 18px 14px;
        border: 1px solid #e7ece8;
        box-shadow: 0 10px 24px rgba(15, 23, 42, 0.05);
        transition: transform 0.18s ease, box-shadow 0.18s ease;
    }

    .swcs-category-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 16px 30px rgba(15, 23, 42, 0.08);
    }

    .swcs-category-image-wrap {
        width: 100%;
        height: 190px;
        border-radius: 18px;
        overflow: hidden;
        background: #f7faf7;
        margin-bottom: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .swcs-category-img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
    }

    .swcs-category-img-fallback {
        font-size: 42px;
        color: #65b875;
    }

    .swcs-category-title {
        text-align: center;
        font-size: 24px;
        font-weight: 800;
        color: #1f2937;
        margin-bottom: 10px;
    }

    .swcs-category-bar {
        width: 78%;
        margin: 0 auto 10px auto;
        height: 9px;
        border-radius: 999px;
        background: #edf1ed;
        overflow: hidden;
    }

    .swcs-category-bar-fill {
        height: 100%;
        border-radius: 999px;
    }

    .bar-green { width: 82%; background: #8bc68b; }
    .bar-pink { width: 72%; background: #e9a0bd; }
    .bar-orange { width: 68%; background: #f0b14c; }
    .bar-red { width: 64%; background: #ea8b86; }

    .swcs-category-years {
        text-align: center;
        font-size: 18px;
        font-weight: 700;
        color: #374151;
    }

    .swcs-info-box {
        min-height: 310px;
        border-radius: 26px;
        overflow: hidden;
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        border: 1px solid #e6ece6;
        box-shadow: 0 10px 24px rgba(15, 23, 42, 0.05);
    }

    .swcs-info-overlay {
        min-height: 310px;
        padding: 28px 28px 24px 28px;
        background: linear-gradient(180deg, rgba(255,255,255,0.82) 0%, rgba(255,255,255,0.72) 100%);
    }

    .swcs-info-title {
        font-size: 28px;
        font-weight: 900;
        color: #1f2937;
        margin-bottom: 14px;
    }

    .swcs-info-list {
        margin: 0;
        padding-left: 22px;
    }

    .swcs-info-list li {
        font-size: 18px;
        line-height: 1.8;
        color: #374151;
        font-weight: 600;
        margin-bottom: 2px;
    }

    .swcs-footer {
        background: rgba(255,255,255,0.75);
        border: 1px solid #e8ece8;
        border-radius: 24px;
        padding: 28px 26px;
        box-shadow: 0 10px 24px rgba(15, 23, 42, 0.04);
    }

    .swcs-footer-title {
        font-size: 22px;
        font-weight: 900;
        color: #1f2937;
        margin-bottom: 10px;
    }

    .swcs-footer-sub {
        font-size: 16px;
        color: #4b5563;
        margin-bottom: 16px;
    }

    .swcs-footer-bottom {
        display: flex;
        justify-content: space-between;
        gap: 16px;
        flex-wrap: wrap;
        font-size: 14px;
        color: #6b7280;
    }

    .swcs-footer-links {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
    }

    @media (max-width: 1200px) {
        .swcs-hero-title { font-size: 44px; }
        .swcs-hero-sub { font-size: 20px; }
        .swcs-category-image-wrap { height: 160px; }
    }

    @media (max-width: 992px) {
        .swcs-topbar {
            flex-direction: column;
            align-items: flex-start;
        }

        .swcs-topbar-right {
            width: 100%;
            justify-content: flex-start;
            flex-wrap: wrap;
        }

        .swcs-hero-title { font-size: 38px; }
        .swcs-hero-sub { font-size: 18px; }
    }
                @media (max-width: 768px) {
    .swcs-sidebar-toggle {
        display: inline-flex;
        position: relative;
        z-index: 1001;
    }

    .swcs-sidebar-checkbox:checked + .swcs-sidebar-toggle {
        opacity: 0;
        pointer-events: none;
    }

    .swcs-sidebar-checkbox:checked ~ .swcs-sidebar-overlay {
        display: block;
        position: fixed;
        inset: 0;
        background: rgba(15, 23, 42, 0.34);
        z-index: 999;
    }

    .swcs-sidebar {
        position: fixed;
        top: 0;
        left: -290px;
        width: 270px;
        height: 100vh;
        min-height: 100vh;
        border-radius: 0 22px 22px 0;
        z-index: 1000;
        transition: left 0.28s ease;
        overflow-y: auto;
        padding-top: 24px;
        background: rgba(255, 255, 255, 0.96);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
    }

    .swcs-sidebar-checkbox:checked ~ .swcs-sidebar {
        left: 0;
    }

    .swcs-sidebar-bottom {
        padding-bottom: 20px;
    }
    }
    </style>
    """, unsafe_allow_html=True)