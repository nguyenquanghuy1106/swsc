def load_setting_user_css():
    import streamlit as st
    st.markdown(
        """
        <style>

        /* ===== BACKGROUND ===== */
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(168, 208, 132, 0.18), transparent 25%),
                radial-gradient(circle at bottom right, rgba(186, 224, 160, 0.18), transparent 25%),
                linear-gradient(180deg, #f7fbf5 0%, #edf5ea 100%);
        }

        /* ===== CONTAINER ===== */
        .main .block-container {
            max-width: 1000px;
            padding-top: 0.4rem;
            padding-bottom: 0.4rem;
        }

        /* ===== NAVBAR ===== */
        .swcs-setting-nav {
            width: 100%;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 16px;
            padding: 10px 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 8px 18px rgba(0,0,0,0.06);
            margin-bottom: 12px;
        }

        .swcs-setting-brand {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 24px;
            font-weight: 900;
            color: #3c7c2f;
        }

        .swcs-setting-links {
            display: flex;
            gap: 18px;
        }

        .swcs-setting-links a {
            font-size: 14px;
            font-weight: 700;
            color: #2c3e2a;
            text-decoration: none;
        }

        .swcs-setting-search {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
            border: 1px solid #e5ebe1;
        }

        /* ===== CARD ===== */
        .swcs-setting-card {
            background: rgba(255,255,255,0.9);
            border-radius: 20px;
            padding: 14px;
            margin-bottom: 10px;
            box-shadow: 0 8px 18px rgba(0,0,0,0.05);
        }

        /* ===== PROFILE ===== */
        .swcs-setting-profile-head {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .swcs-setting-profile-left {
            display: flex;
            gap: 12px;
            align-items: center;
        }

        .swcs-setting-avatar {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            overflow: hidden;
        }

        .swcs-setting-avatar img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .swcs-setting-title {
            font-size: 24px;
            font-weight: 900;
            color: #1e3a1a;
        }

        .swcs-setting-email {
            font-size: 14px;
            color: #2f3f2c;
            font-weight: 600;
        }

        .swcs-setting-gear {
            width: 42px;
            height: 42px;
            border-radius: 14px;
            background: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
        }

        /* ===== ITEM ===== */
        .swcs-setting-item-card {
            background: rgba(255,255,255,0.95);
            border-radius: 18px;
            padding: 10px;
        }

        .swcs-setting-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 6px 4px;
        }

        .swcs-setting-row + .swcs-setting-row {
            border-top: 1px solid rgba(0,0,0,0.08);
            margin-top: 4px;
            padding-top: 10px;
        }

        .swcs-setting-row-left {
            display: flex;
            gap: 10px;
            align-items: center;
        }

        .swcs-setting-row-icon {
            width: 40px;
            height: 40px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.08);
        }

        .theme-dark { background: #8da2fb; }
        .theme-light { background: #ffd768; }
        .sound { background: #ff857f; }
        .notice { background: #b9e24a; }
        .account { background: #ffffff; }

        /* ===== TEXT FIX (QUAN TRỌNG) ===== */
        .swcs-setting-row-title {
            font-size: 15px;
            font-weight: 800;
            color: #1f2d1c;
        }

        .swcs-setting-row-subtitle {
            font-size: 12px;
            color: #4b5d48;
            font-weight: 600;
            opacity: 1 !important;
        }

        /* ===== BUTTON ===== */
        div[data-testid="stButton"] > button {
            min-height: 36px;
            font-size: 13px !important;
            border-radius: 10px !important;
            font-weight: 700 !important;
            color: #1e2f1c !important;
        }

        /* ===== LOGOUT ===== */
        .swcs-setting-action-btn {
            min-height: 38px;
            font-size: 14px !important;
            border-radius: 999px !important;
            color: #e34f3b !important;
        }

        /* ===== MESSAGE ===== */
        .swcs-setting-message {
            padding: 10px;
            border-radius: 10px;
            font-size: 13px;
        }

        /* ===== EXPANDER FIX ===== */
        div[data-testid="stExpander"] summary {
            color: #2a3c28 !important;
            font-weight: 700 !important;
        }

        /* ===== GLOBAL TEXT ===== */
        body, p, span, div {
            -webkit-font-smoothing: antialiased;
            text-rendering: optimizeLegibility;
        }

        /* ===== MOBILE ===== */
        @media (max-width: 768px) {

            .main .block-container {
                padding-top: 0.3rem;
                padding-bottom: 0.3rem;
            }

            .swcs-setting-title {
                font-size: 20px;
            }

            .swcs-setting-avatar {
                width: 50px;
                height: 50px;
            }

            .swcs-setting-row-icon {
                width: 34px;
                height: 34px;
                font-size: 16px;
            }

        }

        </style>
        """,
        unsafe_allow_html=True,
    )