import streamlit as st


def load_login_css():
    st.markdown(
        """
        <style>
        .stApp {
            background:
                radial-gradient(circle at 15% 20%, rgba(154, 210, 114, 0.18), transparent 22%),
                radial-gradient(circle at 85% 18%, rgba(117, 177, 61, 0.10), transparent 18%),
                radial-gradient(circle at 50% 80%, rgba(183, 226, 151, 0.14), transparent 22%),
                linear-gradient(180deg, #f8fbf5 0%, #eef5ea 100%);
        }

        .main .block-container {
            max-width: 1240px;
            padding-top: 0.8rem;
            padding-bottom: 1rem;
        }

        .login-page-shell {
            min-height: calc(100vh - 40px);
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .login-layout {
            width: 100%;
        }

        .login-info-panel {
            padding: 12px 8px 12px 8px;
            animation: swcsFadeUp 0.6s ease;
        }

        .login-brand-line {
            display: inline-flex;
            align-items: center;
            gap: 12px;
            padding: 10px 18px;
            background: rgba(255,255,255,0.88);
            border: 1px solid #e7eee2;
            border-radius: 999px;
            box-shadow: 0 10px 24px rgba(74, 101, 58, 0.08);
            margin-bottom: 20px;
        }

        .login-brand-leaf {
            font-size: 28px;
        }

        .login-brand-name {
            font-size: 28px;
            font-weight: 900;
            color: #4f9532;
            letter-spacing: 0.3px;
        }

        .accent-text {
            color: #74a91d;
        }

        h3 {
            font-size: 52px !important;
            line-height: 1.08 !important;
            font-weight: 900 !important;
            color: #23411f !important;
            margin: 0 0 16px 0 !important;
        }

        .login-hero-desc {
            font-size: 17px;
            line-height: 1.8;
            color: #5e6b5d;
            margin-bottom: 22px;
            max-width: 520px;
        }

        .login-feature-item {
            display: flex;
            gap: 12px;
            align-items: flex-start;
            padding: 14px 16px;
            background: rgba(255,255,255,0.72);
            border: 1px solid #e8efe3;
            border-radius: 18px;
            box-shadow: 0 10px 22px rgba(80, 109, 63, 0.06);
            margin-bottom: 14px;
        }

        .login-feature-icon {
            width: 38px;
            height: 38px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(180deg, #86bc24 0%, #73a81c 100%);
            color: #fff;
            font-size: 18px;
            font-weight: 700;
            flex: 0 0 38px;
            box-shadow: 0 8px 16px rgba(113, 162, 31, 0.18);
        }

        .login-feature-text {
            font-size: 15px;
            line-height: 1.7;
            color: #4f5b4e;
            font-weight: 600;
        }

        .login-info-note {
            font-size: 14px;
            color: #6a7468;
            line-height: 1.7;
            margin-top: 8px;
        }

        .login-form-panel {
            width: 100%;
            max-width: 480px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.94);
            border: 1px solid rgba(232, 239, 226, 0.98);
            border-radius: 34px;
            box-shadow:
                0 24px 56px rgba(77, 105, 61, 0.12),
                inset 0 1px 0 rgba(255,255,255,0.75);
            padding: 26px 22px 18px 22px;
            position: relative;
            overflow: hidden;
            animation: swcsFadeUp 0.7s ease;
        }

        .login-form-panel::before {
            content: "";
            position: absolute;
            inset: 0 0 auto 0;
            height: 120px;
            background: linear-gradient(180deg, rgba(150,203,102,0.08), rgba(150,203,102,0.00));
            pointer-events: none;
        }

        .login-card-topline {
            width: 68px;
            height: 6px;
            border-radius: 999px;
            background: linear-gradient(90deg, #84b81d 0%, #9acc3f 100%);
            margin: 0 auto 16px auto;
            position: relative;
            z-index: 2;
        }

        .login-panel-title {
            text-align: center;
            font-size: 38px;
            line-height: 1.08;
            font-weight: 900;
            color: #77a923;
            margin: 0 0 8px 0;
            position: relative;
            z-index: 2;
        }

        .login-panel-subtitle {
            text-align: center;
            font-size: 14px;
            line-height: 1.7;
            color: #5f6b5c;
            margin-bottom: 18px;
            position: relative;
            z-index: 2;
        }

        .login-top-tabs {
            display: flex;
            gap: 12px;
            justify-content: center;
            align-items: center;
            margin-bottom: 18px;
            position: relative;
            z-index: 2;
        }

        .login-pill-active,
        .login-pill-ghost {
            min-width: 138px;
            height: 44px;
            border-radius: 999px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 15px;
            font-weight: 800;
            text-decoration: none;
            box-shadow: 0 8px 16px rgba(88, 118, 45, 0.10);
        }

        .login-pill-active {
            background: linear-gradient(90deg, #82b515 0%, #73a614 100%);
            color: #ffffff;
        }

        .login-pill-ghost {
            background: #ffffff;
            color: #5d5d5d;
            border: 1px solid #edf1e8;
        }

        div[data-baseweb="input"] {
            border-radius: 14px !important;
            min-height: 52px !important;
            background: rgba(255,255,255,0.98) !important;
            border: 1px solid #e5eae0 !important;
            box-shadow: none !important;
        }

        div[data-baseweb="input"]:focus-within {
            border-color: #94c63a !important;
            box-shadow: 0 0 0 3px rgba(148,198,58,0.12) !important;
        }

        div[data-baseweb="input"] input {
            font-size: 15px !important;
            color: #334155 !important;
        }

        label[data-testid="stWidgetLabel"] p {
            font-size: 15px !important;
            font-weight: 700 !important;
            color: #454545 !important;
        }

        .stCheckbox {
            padding-top: 4px;
        }

        .stCheckbox label {
            font-size: 14px !important;
            color: #505050 !important;
            font-weight: 600 !important;
        }

        .login-inline-right {
            height: 34px;
            display: flex;
            align-items: center;
            justify-content: flex-end;
        }

        .login-forgot-link {
            font-size: 14px;
            font-weight: 700;
            color: #525252;
            text-decoration: underline;
            text-underline-offset: 4px;
        }

        div[data-testid="stButton"] > button {
            width: 100%;
            min-height: 52px;
            border: none !important;
            border-radius: 14px !important;
            background: linear-gradient(90deg, #7fb51b 0%, #88bc23 100%) !important;
            color: #ffffff !important;
            font-size: 18px !important;
            font-weight: 800 !important;
            box-shadow: 0 12px 24px rgba(113, 162, 31, 0.22) !important;
            transition: 0.24s ease !important;
        }

        div[data-testid="stButton"] > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 16px 26px rgba(113, 162, 31, 0.26) !important;
        }

        .login-divider {
            display: flex;
            align-items: center;
            gap: 12px;
            margin: 14px 0;
            color: #777;
            font-size: 14px;
            justify-content: center;
        }

        .login-divider::before,
        .login-divider::after {
            content: "";
            height: 1px;
            flex: 1;
            background: #d9ded5;
        }

        .login-google-btn {
            width: 100%;
            height: 50px;
            border-radius: 14px;
            background: #ffffff;
            border: 1px solid #ecefe7;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            font-size: 15px;
            font-weight: 700;
            color: #4f4f4f;
            box-shadow: 0 8px 18px rgba(15,23,42,0.05);
            margin-bottom: 12px;
        }

        .login-bottom-text {
            text-align: center;
            font-size: 14px;
            color: #525252;
            margin-top: 8px;
        }

        .login-bottom-link {
            color: #73a61e;
            font-weight: 800;
            text-decoration: none;
        }

        .swcs-auth-message {
            padding: 11px 13px;
            border-radius: 14px;
            font-size: 14px;
            font-weight: 700;
            margin-bottom: 12px;
        }

        .swcs-auth-success {
            background: rgba(111, 190, 104, 0.16);
            color: #2f6d25;
            border: 1px solid rgba(111, 190, 104, 0.28);
        }

        .swcs-auth-error {
            background: rgba(239, 68, 68, 0.10);
            color: #b42318;
            border: 1px solid rgba(239, 68, 68, 0.18);
        }

        @keyframes swcsFadeUp {
            from {
                opacity: 0;
                transform: translateY(16px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @media (max-width: 980px) {
            .login-info-panel {
                padding-top: 0;
                margin-bottom: 24px;
            }

            .login-form-panel {
                max-width: 480px;
            }

            h3 {
                font-size: 42px !important;
            }
        }

        @media (max-width: 768px) {
            .main .block-container {
                padding-top: 0.5rem;
                padding-bottom: 0.8rem;
            }

            .login-brand-line {
                padding: 9px 16px;
            }

            .login-brand-name {
                font-size: 24px;
            }

            h3 {
                font-size: 34px !important;
            }

            .login-hero-desc {
                font-size: 15px;
            }

            .login-form-panel {
                max-width: 100%;
                border-radius: 26px;
                padding: 22px 14px 16px 14px;
            }

            .login-panel-title {
                font-size: 32px;
            }
        }

        @media (max-width: 480px) {
            .login-top-tabs {
                flex-direction: column;
            }

            .login-pill-active,
            .login-pill-ghost {
                width: 100%;
                min-width: unset;
            }

            h3 {
                font-size: 30px !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )