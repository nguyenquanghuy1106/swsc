import streamlit as st


def load_home_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

    :root {
        --swcs-green: #45b85a;
        --swcs-green-dark: #168538;
        --swcs-green-soft: #effaf1;
        --swcs-yellow: #fff4b8;
        --swcs-text: #111827;
        --swcs-muted: #6b7280;
        --swcs-white: #ffffff;
        --swcs-border: #e5f2e7;
        --swcs-shadow: 0 24px 70px rgba(30, 96, 45, 0.14);
    }

    html, body, .stApp {
        font-family: 'Inter', sans-serif !important;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(85, 190, 100, 0.18), transparent 34%),
            radial-gradient(circle at top right, rgba(255, 218, 83, 0.18), transparent 32%),
            linear-gradient(135deg, #f6fff7 0%, #eef9f0 100%);
    }

    .main .block-container {
        max-width: 1280px;
        padding: 24px 28px 40px !important;
    }

    header[data-testid="stHeader"],
    #MainMenu,
    footer,
    div[data-testid="stDecoration"] {
        display: none !important;
    }

    a {
        text-decoration: none !important;
    }

    .swcs-page-bg {
        width: 100%;
        min-height: 100vh;
    }

    .swcs-web-home-layout {
        width: 100%;
        margin: 0 auto;
    }

    .swcs-home-web-card {
        position: relative;
        width: 100%;
        min-height: 920px;
        padding: 32px 42px 0;
        border-radius: 34px;
        overflow: hidden;
        background:
            radial-gradient(circle at 64% 26%, rgba(255, 232, 135, 0.38), transparent 28%),
            radial-gradient(circle at 35% 28%, rgba(112, 209, 132, 0.2), transparent 24%),
            linear-gradient(180deg, rgba(255,255,255,0.96), rgba(248,255,249,0.98));
        box-shadow: var(--swcs-shadow);
        border: 1px solid var(--swcs-border);
    }

    .swcs-home-top {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 26px;
    }

    .swcs-menu-btn,
    .swcs-bell {
        width: 48px;
        height: 48px;
        border-radius: 16px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background: #ffffff;
        color: #14532d !important;
        font-size: 23px;
        font-weight: 900;
        box-shadow: 0 10px 26px rgba(20, 120, 52, 0.09);
        border: 1px solid #e3f1e5;
    }

    .swcs-top-right {
        display: flex;
        align-items: center;
        gap: 14px;
    }

    .swcs-bell {
        position: relative;
    }

    .swcs-bell-dot {
        position: absolute;
        top: 9px;
        right: 9px;
        width: 9px;
        height: 9px;
        border-radius: 50%;
        background: #ef4444;
        border: 2px solid white;
    }

    .swcs-point-pill {
        height: 44px;
        padding: 0 18px 0 12px;
        border-radius: 999px;
        background: linear-gradient(135deg, #5ec968, #22963f);
        color: white;
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 14px;
        font-weight: 900;
        box-shadow: 0 14px 28px rgba(34, 130, 51, 0.24);
    }

    .swcs-gift {
        width: 28px;
        height: 28px;
        border-radius: 50%;
        background: white;
        display: inline-flex;
        align-items: center;
        justify-content: center;
    }

    .swcs-user-row {
        margin-bottom: 26px;
    }

    .swcs-user-left {
        display: flex;
        align-items: center;
        gap: 14px;
    }

    .swcs-user-avatar {
        width: 66px;
        height: 66px;
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid white;
        box-shadow: 0 14px 30px rgba(30, 96, 45, 0.18);
        background: #eaf8ec;
    }

    .swcs-user-avatar.fallback {
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 30px;
    }

    .swcs-hi {
        color: var(--swcs-text);
        font-size: 17px;
        font-weight: 700;
    }

    .swcs-user-sub {
        margin-top: 4px;
        color: var(--swcs-muted);
        font-size: 14px;
        font-weight: 500;
    }

    .swcs-hero-web {
        display: grid;
        grid-template-columns: 1fr 1fr;
        align-items: center;
        gap: 40px;
        min-height: 420px;
        margin-bottom: 36px;
    }

    .swcs-hero-badge {
        width: fit-content;
        padding: 9px 16px;
        border-radius: 999px;
        background: #eaf8ec;
        color: #238944;
        font-size: 13px;
        font-weight: 800;
        border: 1px solid #d8efdc;
        margin-bottom: 18px;
    }

    .swcs-hero-text h1 {
        margin: 0;
        color: #0f172a;
        font-size: clamp(44px, 5vw, 72px);
        line-height: 1.04;
        letter-spacing: -2.4px;
        font-weight: 900;
    }

    .swcs-hero-text h1 span {
        color: var(--swcs-green);
    }

    .swcs-hero-text p {
        max-width: 520px;
        margin: 22px 0 0;
        color: #647067;
        font-size: 18px;
        line-height: 1.65;
        font-weight: 500;
    }

    .swcs-hero-actions {
        display: flex;
        flex-wrap: wrap;
        gap: 14px;
        margin-top: 28px;
    }

    .swcs-start-btn,
    .swcs-outline-btn {
        height: 50px;
        padding: 0 26px;
        border-radius: 999px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 15px;
        font-weight: 800;
        transition: 0.2s ease;
    }

    .swcs-start-btn {
        background: linear-gradient(135deg, #61c96c, #2e9f46);
        color: white !important;
        box-shadow: 0 16px 34px rgba(55, 153, 67, 0.22);
    }

    .swcs-outline-btn {
        background: white;
        color: #22963f !important;
        border: 1px solid #d8efdc;
        box-shadow: 0 10px 24px rgba(20, 120, 52, 0.07);
    }

    .swcs-start-btn:hover,
    .swcs-outline-btn:hover,
    .swcs-web-category:hover {
        transform: translateY(-4px);
    }

    .swcs-hero-visual {
        position: relative;
        height: 420px;
    }

    .swcs-collage {
        position: absolute;
        overflow: hidden;
        background: #eaf6eb;
        box-shadow: 0 22px 44px rgba(15, 23, 42, 0.14);
    }

    .swcs-collage.big {
        width: 46%;
        height: 330px;
        left: 4%;
        top: 54px;
        border-radius: 32px;
    }

    .swcs-collage.small {
        width: 42%;
        height: 180px;
        right: 4%;
        border-radius: 28px;
    }

    .swcs-collage.small.top {
        top: 22px;
    }

    .swcs-collage.small.bottom {
        bottom: 22px;
    }

    .swcs-collage-img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
    }

    .swcs-img-fallback {
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--swcs-green);
        font-size: 50px;
    }

    .swcs-blob {
        position: absolute;
        border-radius: 999px;
        z-index: 0;
    }

    .swcs-blob.one {
        width: 42px;
        height: 42px;
        left: 0;
        top: 150px;
        background: #3fa14c;
    }

    .swcs-blob.two {
        width: 28px;
        height: 28px;
        left: 42%;
        top: 225px;
        background: #f2c126;
    }

    .swcs-blob.three {
        width: 16px;
        height: 16px;
        left: 16%;
        top: 280px;
        background: #76bf34;
    }

.swcs-section-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    margin: 18px 0 20px;
    width: 100%;
    overflow: visible !important;
}
                
.swcs-section-title {
    color: #07111f !important;
    font-size: 30px !important;
    font-weight: 900 !important;
    line-height: 1.2 !important;
    letter-spacing: -0.5px !important;
    font-family: 'Inter', sans-serif !important;

    display: block !important;
    width: 600px !important;
    min-width: 420px !important;
    max-width: 420px !important;

    white-space: nowrap !important;
    overflow: visible !important;
    text-overflow: clip !important;
    flex: 0 0 420px !important;
}
.swcs-section-link {
    color: #168538 !important;
    font-size: 16px !important;
    font-weight: 800 !important;
    font-family: 'Inter', sans-serif !important;

    display: inline-flex !important;
    align-items: center !important;
    justify-content: flex-end !important;
    white-space: nowrap !important;
    overflow: visible !important;
    text-overflow: unset !important;
    flex-shrink: 0 !important;
    text-decoration: none !important;
}


    .swcs-category-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
        margin-bottom: 30px;
    }

    .swcs-web-category {
        min-height: 160px;
        padding: 24px 16px;
        border-radius: 28px;
        background: rgba(255,255,255,0.72);
        border: 1px solid #e2efe4;
        color: var(--swcs-text) !important;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 14px;
        box-shadow: 0 14px 32px rgba(30, 96, 45, 0.06);
        transition: 0.2s ease;
    }

    .swcs-category-circle {
        width: 86px;
        height: 86px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .swcs-category-circle span {
        font-size: 40px;
        line-height: 1;
    }

    .swcs-category-circle.yellow { background: #fff58f; }
    .swcs-category-circle.blue { background: #bdf5ff; }
    .swcs-category-circle.pink { background: #ffc9d7; }
    .swcs-category-circle.green { background: #caffc3; }

    .swcs-web-category-name {
        max-width: 130px;
        text-align: center;
        color: var(--swcs-text);
        font-size: 16px;
        line-height: 1.25;
        font-weight: 850;
    }

    .swcs-banner-card {
        position: relative;
        display: block;
        height: 230px;
        border-radius: 30px;
        overflow: hidden;
        background-size: cover;
        background-position: center;
        box-shadow: 0 18px 38px rgba(25, 92, 38, 0.13);
        margin-bottom: 16px;
    }

    .swcs-banner-overlay {
        width: 100%;
        height: 100%;
        padding: 28px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background:
            linear-gradient(180deg, rgba(0,0,0,0.05), rgba(0,0,0,0.46)),
            linear-gradient(90deg, rgba(71, 143, 76, 0.24), rgba(255,255,255,0.04));
        text-align: center;
    }

    .swcs-banner-brand {
        color: white;
        font-size: clamp(32px, 5vw, 54px);
        letter-spacing: 10px;
        line-height: 1;
        font-weight: 900;
        text-shadow: 0 6px 18px rgba(0,0,0,0.34);
    }

    .swcs-banner-title {
        margin-top: 14px;
        color: white;
        font-size: 20px;
        font-weight: 800;
        text-shadow: 0 5px 16px rgba(0,0,0,0.35);
    }

    .swcs-slider-dots {
        display: flex;
        justify-content: center;
        gap: 7px;
        margin: 12px 0 26px;
    }

    .swcs-slider-dots span {
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: #d4d4d4;
    }

    .swcs-slider-dots span.active {
        background: var(--swcs-green);
        width: 24px;
        border-radius: 999px;
    }

    .swcs-info-row {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 18px;
        margin-bottom: 34px;
    }

    .swcs-info-card {
        display: flex;
        gap: 14px;
        padding: 20px;
        border-radius: 24px;
        background: rgba(255,255,255,0.82);
        border: 1px solid #e2efe4;
        box-shadow: 0 12px 26px rgba(18, 78, 38, 0.06);
    }

    .swcs-info-icon {
        width: 48px;
        height: 48px;
        flex: 0 0 48px;
        border-radius: 16px;
        background: #eaf8ec;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
    }

    .swcs-info-card h3 {
        margin: 0;
        color: var(--swcs-text);
        font-size: 17px;
        font-weight: 850;
    }

    .swcs-info-card p {
        margin: 6px 0 0;
        color: var(--swcs-muted);
        font-size: 14px;
        line-height: 1.5;
        font-weight: 500;
    }

    .swcs-floating-recycle {
        position: absolute;
        right: 30px;
        bottom: 104px;
        width: 54px;
        height: 54px;
        border-radius: 50%;
        background: white;
        color: var(--swcs-green) !important;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 32px;
        box-shadow: 0 12px 26px rgba(0,0,0,0.16);
        z-index: 8;
    }

    .swcs-bottom-space {
        height: 104px;
    }

    .swcs-bottom-nav {
        position: absolute;
        left: 0;
        right: 0;
        bottom: 0;
        height: 82px;
        padding: 0 36px 12px;
        background: #4dbb5c;
        border-radius: 0 0 34px 34px;
        display: grid;
        grid-template-columns: 1fr 1fr 104px 1fr 1fr;
        align-items: center;
        z-index: 10;
    }

    .swcs-nav-item {
        height: 54px;
        border-radius: 999px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        color: white !important;
        font-weight: 800;
    }

    .swcs-nav-item.active,
    .swcs-nav-item:hover {
        background: rgba(24, 128, 49, 0.86);
    }

    .swcs-nav-icon {
        font-size: 25px;
    }

    .swcs-nav-label {
        font-size: 14px;
    }

    .swcs-scan-btn {
        position: relative;
        width: 78px;
        height: 78px;
        margin: -42px auto 0;
        border-radius: 50%;
        background: white;
        border: 7px solid #f1f8f2;
        box-shadow: 0 14px 28px rgba(0,0,0,0.18);
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .swcs-scan-dot {
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: #111827;
    }

    .swcs-scan-corner {
        position: absolute;
        width: 17px;
        height: 17px;
        border-color: #111827;
        border-style: solid;
    }

    .swcs-scan-corner.tl {
        top: 20px;
        left: 20px;
        border-width: 3px 0 0 3px;
    }

    .swcs-scan-corner.tr {
        top: 20px;
        right: 20px;
        border-width: 3px 3px 0 0;
    }

    .swcs-scan-corner.bl {
        bottom: 20px;
        left: 20px;
        border-width: 0 0 3px 3px;
    }

    .swcs-scan-corner.br {
        bottom: 20px;
        right: 20px;
        border-width: 0 3px 3px 0;
    }

    @media (max-width: 980px) {
        .main .block-container {
            padding: 14px !important;
        }

        .swcs-home-web-card {
            padding: 24px 24px 0;
        }

        .swcs-hero-web {
            grid-template-columns: 1fr;
            gap: 20px;
        }

        .swcs-hero-visual {
            height: 360px;
        }

        .swcs-category-grid {
            grid-template-columns: repeat(2, 1fr);
        }

        .swcs-info-row {
            grid-template-columns: 1fr;
        }
    }

    @media (max-width: 560px) {
        .main .block-container {
            padding: 0 !important;
        }

        .swcs-home-web-card {
            min-height: 100vh;
            border-radius: 0;
            box-shadow: none;
            border: none;
            padding: 18px 14px 0;
        }

        .swcs-hero-text h1 {
            font-size: 38px;
            letter-spacing: -1.4px;
        }

        .swcs-hero-text p {
            font-size: 15px;
        }

        .swcs-hero-visual {
            height: 270px;
        }

        .swcs-collage.big {
            width: 44%;
            height: 190px;
            top: 52px;
        }

        .swcs-collage.small {
            width: 43%;
            height: 116px;
        }

        .swcs-category-grid {
            grid-template-columns: repeat(4, 1fr);
            gap: 8px;
        }

        .swcs-web-category {
            min-height: auto;
            padding: 10px 4px;
            background: transparent;
            border: none;
            box-shadow: none;
        }

        .swcs-category-circle {
            width: 56px;
            height: 56px;
        }

        .swcs-category-circle span {
            font-size: 27px;
        }

        .swcs-web-category-name {
            font-size: 11px;
        }

        .swcs-banner-card {
            height: 150px;
            border-radius: 20px;
        }

        .swcs-banner-title {
            font-size: 14px;
        }

        .swcs-info-row {
            display: none;
        }

        .swcs-nav-label {
            display: none;
        }

        .swcs-bottom-nav {
            position: fixed;
            height: 66px;
            border-radius: 24px 24px 0 0;
            grid-template-columns: 1fr 1fr 84px 1fr 1fr;
            padding: 0 12px 12px;
        }

        .swcs-scan-btn {
            width: 66px;
            height: 66px;
            margin-top: -34px;
        }

        .swcs-floating-recycle {
            position: fixed;
            right: 16px;
            bottom: 84px;
            width: 46px;
            height: 46px;
            font-size: 26px;
        }
    }
    </style>
    """, unsafe_allow_html=True)