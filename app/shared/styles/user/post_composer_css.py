import streamlit as st


def load_post_composer_css():
    st.markdown(
        """
        <style>
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(168, 208, 132, 0.18), transparent 24%),
                radial-gradient(circle at bottom right, rgba(186, 224, 160, 0.18), transparent 24%),
                linear-gradient(180deg, #f7fbf5 0%, #edf5ea 100%);
        }

        .main .block-container {
            max-width: 1300px;
            padding-top: 0.8rem;
            padding-bottom: 1rem;
        }

        .swcs-community-nav {
            width: 100%;
            background: rgba(255, 255, 255, 0.90);
            border: 1px solid rgba(232, 239, 226, 0.95);
            border-radius: 22px;
            padding: 18px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 18px;
            box-shadow: 0 16px 34px rgba(78, 104, 62, 0.08);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            margin-bottom: 22px;
        }

        .swcs-community-brand {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 34px;
            font-weight: 900;
            color: #4e9432;
            flex-shrink: 0;
        }

        .swcs-community-brand-icon {
            font-size: 34px;
        }

        .swcs-community-links {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 26px;
            flex: 1;
            flex-wrap: wrap;
        }

        .swcs-community-links a {
            color: #3f4c3d;
            text-decoration: none;
            font-size: 16px;
            font-weight: 700;
        }

        .swcs-community-search {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 48px;
            height: 48px;
            border-radius: 50%;
            background: rgba(255,255,255,0.9);
            border: 1px solid #e5ebe1;
            box-shadow: 0 8px 20px rgba(15,23,42,0.05);
            font-size: 20px;
            flex-shrink: 0;
        }

        .swcs-community-main-card {
            width: 100%;
            background: rgba(255, 255, 255, 0.52);
            border: 1px solid rgba(233, 239, 227, 0.94);
            border-radius: 34px;
            padding: 20px;
            box-shadow: 0 18px 42px rgba(78, 104, 62, 0.08);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
        }

        .swcs-composer-user {
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .swcs-composer-avatar {
            width: 62px;
            height: 62px;
            border-radius: 50%;
            overflow: hidden;
            border: 2px solid rgba(255,255,255,0.92);
            box-shadow: 0 8px 18px rgba(15,23,42,0.08);
            flex-shrink: 0;
        }

        .swcs-composer-avatar img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        .swcs-composer-meta {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }

        .swcs-composer-name {
            font-size: 20px;
            font-weight: 900;
            color: #334034;
            line-height: 1.1;
        }

        .swcs-composer-chip {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            width: fit-content;
            padding: 8px 14px;
            border-radius: 12px;
            background: #68879b;
            color: #fff;
            font-size: 15px;
            font-weight: 800;
        }

        .swcs-top-post-btn-space {
            height: 24px;
        }

        .swcs-bottom-actions-shell {
            margin-top: 20px;
            background: rgba(255,255,255,0.64);
            border: 1px solid rgba(234,239,228,0.96);
            border-radius: 26px;
            padding: 18px;
            box-shadow: 0 12px 30px rgba(78,104,62,0.06);
        }

        .swcs-action-card {
            background: rgba(255,255,255,0.88);
            border: 1px solid #e8ede3;
            border-radius: 18px;
            padding: 18px 20px;
            min-height: 78px;
            display: flex;
            align-items: center;
            gap: 14px;
            box-shadow: 0 8px 18px rgba(15,23,42,0.05);
            transition: 0.22s ease;
        }

        .swcs-action-card:hover {
            transform: translateY(-2px);
        }

        .swcs-action-icon {
            font-size: 28px;
            width: 40px;
            text-align: center;
        }

        .swcs-action-label {
            font-size: 18px;
            font-weight: 800;
            color: #3f4a3d;
        }

        .swcs-mini-dots {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            padding-top: 14px;
        }

        .swcs-mini-dot {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: rgba(121, 186, 88, 0.38);
        }

        .swcs-mini-dot.active {
            background: #8bc34a;
        }

        .swcs-helper-row {
            display: flex;
            gap: 12px;
            align-items: center;
            flex-wrap: wrap;
            margin-top: 10px;
        }

        .swcs-helper-badge {
            padding: 7px 12px;
            border-radius: 999px;
            background: rgba(255,255,255,0.75);
            border: 1px solid #e7ece4;
            font-size: 13px;
            font-weight: 700;
            color: #576056;
        }

        .swcs-post-message {
            padding: 12px 14px;
            border-radius: 14px;
            font-size: 14px;
            font-weight: 700;
            margin: 10px 0 12px 0;
        }

        .swcs-post-success {
            background: rgba(111, 190, 104, 0.16);
            color: #2f6d25;
            border: 1px solid rgba(111, 190, 104, 0.28);
        }

        .swcs-post-error {
            background: rgba(239, 68, 68, 0.10);
            color: #b42318;
            border: 1px solid rgba(239, 68, 68, 0.18);
        }

        div[data-baseweb="select"] {
            border-radius: 12px !important;
            min-height: 48px !important;
            background: rgba(255,255,255,0.92) !important;
            border: 1px solid #dbe5d2 !important;
            box-shadow: 0 8px 18px rgba(15,23,42,0.05) !important;
        }

        div[data-testid="stFileUploader"] section {
            border-radius: 16px !important;
            background: rgba(255,255,255,0.72) !important;
            border: 1px dashed #dfe7d9 !important;
        }

        label[data-testid="stWidgetLabel"] p {
            font-size: 15px !important;
            font-weight: 700 !important;
            color: #454545 !important;
        }

        div[data-testid="stTextArea"] textarea {
            min-height: 320px !important;
            border-radius: 22px !important;
            border: 1px solid rgba(234, 239, 228, 0.95) !important;
            background: rgba(255,255,255,0.42) !important;
            font-size: 26px !important;
            line-height: 1.5 !important;
            color: #4a5148 !important;
            padding: 18px 18px !important;
            box-shadow: none !important;
            resize: none !important;
        }

        div[data-testid="stTextArea"] textarea::placeholder {
            color: #7e857d !important;
            opacity: 1 !important;
        }

        div[data-testid="stButton"] > button {
            width: 100%;
            min-height: 54px;
            border: none !important;
            border-radius: 999px !important;
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
        /* ===== EXPANDER FIX ===== */
        div[data-testid="stExpander"] {
            border-radius: 18px !important;
            border: 1px solid #dfe7d9 !important;
            background: rgba(255,255,255,0.85) !important;
            box-shadow: 0 8px 20px rgba(15,23,42,0.05);
            overflow: hidden;
        }

        /* Header expander */
        div[data-testid="stExpander"] summary {
            font-size: 16px !important;
            font-weight: 800 !important;
            color: #3c4a3a !important;
            padding: 14px 16px !important;
            background: rgba(245, 250, 242, 0.9) !important;
            border-radius: 18px !important;
            cursor: pointer;
            transition: 0.2s ease;
        }

        /* Hover đẹp hơn */
        div[data-testid="stExpander"] summary:hover {
            background: rgba(226, 244, 212, 0.9) !important;
        }

        /* Nội dung bên trong */
        div[data-testid="stExpander"] div[role="region"] {
            padding: 14px 16px 16px 16px !important;
            background: rgba(255,255,255,0.9) !important;
        }

        @media (max-width: 900px) {
            .swcs-community-nav {
                flex-wrap: wrap;
                justify-content: center;
            }

            .swcs-community-links {
                order: 3;
                width: 100%;
                justify-content: center;
                gap: 18px;
            }

            div[data-testid="stTextArea"] textarea {
                font-size: 22px !important;
                min-height: 260px !important;
            }

            .swcs-top-post-btn-space {
                display: none;
            }
        }

        @media (max-width: 640px) {
            .main .block-container {
                padding-top: 0.45rem;
                padding-bottom: 0.7rem;
            }

            .swcs-community-nav {
                padding: 14px 14px;
                border-radius: 18px;
            }

            .swcs-community-brand {
                font-size: 28px;
            }

            .swcs-community-links a {
                font-size: 14px;
            }

            .swcs-community-main-card {
                padding: 12px;
                border-radius: 24px;
            }

            .swcs-composer-avatar {
                width: 52px;
                height: 52px;
            }

            .swcs-composer-name {
                font-size: 18px;
            }

            .swcs-composer-chip {
                font-size: 13px;
                padding: 7px 12px;
            }

            div[data-testid="stTextArea"] textarea {
                font-size: 18px !important;
                min-height: 220px !important;
            }

            .swcs-action-card {
                min-height: 70px;
                padding: 14px 16px;
            }

            .swcs-action-label {
                font-size: 16px;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )