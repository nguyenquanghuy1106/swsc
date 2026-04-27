import streamlit as st


def load_register_css():
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

        .register-layout {
            width: 100%;
            min-height: calc(100vh - 40px);
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .register-info-panel {
            padding: 12px 8px 12px 8px;
            animation: registerFadeUp 0.6s ease;
        }

        .register-brand-line {
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

        .register-brand-leaf {
            font-size: 28px;
        }

        .register-brand-name {
            font-size: 28px;
            font-weight: 900;
            color: #4f9532;
            letter-spacing: 0.3px;
        }

        .register-hero-title {
            font-size: 50px;
            line-height: 1.08;
            font-weight: 900;
            color: #23411f;
            margin: 0 0 16px 0;
        }

        .register-accent-text {
            color: #74a91d;
        }

        .register-hero-desc {
            font-size: 17px;
            line-height: 1.8;
            color: #5e6b5d;
            margin-bottom: 22px;
            max-width: 520px;
        }

        .register-feature-item {
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

        .register-feature-icon {
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

        .register-feature-text {
            font-size: 15px;
            line-height: 1.7;
            color: #4f5b4e;
            font-weight: 600;
        }

        .register-info-note {
            font-size: 14px;
            color: #6a7468;
            line-height: 1.7;
            margin-top: 8px;
        }

        .register-form-panel {
            width: 100%;
            max-width: 500px;
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
            animation: registerFadeUp 0.7s ease;
        }

        .register-form-panel::before {
            content: "";
            position: absolute;
            inset: 0 0 auto 0;
            height: 120px;
            background: linear-gradient(180deg, rgba(150,203,102,0.08), rgba(150,203,102,0.00));
            pointer-events: none;
        }

        .register-card-topline {
            width: 68px;
            height: 6px;
            border-radius: 999px;
            background: linear-gradient(90deg, #84b81d 0%, #9acc3f 100%);
            margin: 0 auto 16px auto;
            position: relative;
            z-index: 2;
        }

        .register-panel-title {
            text-align: center;
            font-size: 38px;
            line-height: 1.08;
            font-weight: 900;
            color: #77a923;
            margin: 0 0 8px 0;
            position: relative;
            z-index: 2;
        }

        .register-panel-subtitle {
            text-align: center;
            font-size: 14px;
            line-height: 1.7;
            color: #5f6b5c;
            margin-bottom: 18px;
            position: relative;
            z-index: 2;
        }

        .register-top-tabs {
            display: flex;
            gap: 12px;
            justify-content: center;
            align-items: center;
            margin-bottom: 18px;
            position: relative;
            z-index: 2;
        }

        .register-pill-active,
        .register-pill-ghost {
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

        .register-pill-active {
            background: linear-gradient(90deg, #82b515 0%, #73a614 100%);
            color: #ffffff;
        }

        .register-pill-ghost {
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

        .register-bottom-text {
            text-align: center;
            font-size: 14px;
            color: #525252;
            margin-top: 8px;
        }

        .register-bottom-link {
            color: #73a61e;
            font-weight: 800;
            text-decoration: none;
        }

        .register-auth-message {
            padding: 11px 13px;
            border-radius: 14px;
            font-size: 14px;
            font-weight: 700;
            margin-bottom: 12px;
        }

        .register-auth-success {
            background: rgba(111, 190, 104, 0.16);
            color: #2f6d25;
            border: 1px solid rgba(111, 190, 104, 0.28);
        }

        .register-auth-error {
            background: rgba(239, 68, 68, 0.10);
            color: #b42318;
            border: 1px solid rgba(239, 68, 68, 0.18);
        }

        @keyframes registerFadeUp {
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
            .register-info-panel {
                margin-bottom: 24px;
            }

            .register-hero-title {
                font-size: 42px;
            }
        }

        @media (max-width: 768px) {
            .main .block-container {
                padding-top: 0.5rem;
                padding-bottom: 0.8rem;
            }

            .register-brand-line {
                padding: 9px 16px;
            }

            .register-brand-name {
                font-size: 24px;
            }

            .register-hero-title {
                font-size: 34px;
            }

            .register-hero-desc {
                font-size: 15px;
            }

            .register-form-panel {
                max-width: 100%;
                border-radius: 26px;
                padding: 22px 14px 16px 14px;
            }

            .register-panel-title {
                font-size: 32px;
            }
        }

        @media (max-width: 480px) {
            .register-top-tabs {
                flex-direction: column;
            }

            .register-pill-active,
            .register-pill-ghost {
                width: 100%;
                min-width: unset;
            }

            .register-hero-title {
                font-size: 30px;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )