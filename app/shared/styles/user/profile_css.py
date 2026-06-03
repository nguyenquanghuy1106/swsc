import streamlit as st


def load_profile_css():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #f1ffe9, #eaf9df) !important;
        }

        header[data-testid="stHeader"] {
            display: none;
        }

        .block-container {
            max-width: 1180px !important;
            padding-top: 28px !important;
            padding-bottom: 125px !important;
        }

        .profile-menu {
            background: rgba(255,255,255,.82);
            border-radius: 20px;
            padding: 14px;
            border: 1px solid #b7d9aa;
            box-shadow: 0 8px 24px rgba(54,100,37,.13);
            position: sticky;
            top: 20px;
        }

        .profile-menu a {
            display: block;
            text-decoration: none !important;
            color: #173d18 !important;
            font-weight: 900;
            padding: 13px 12px;
            border-radius: 14px;
            margin-bottom: 8px;
        }

        .profile-menu a.active,
        .profile-menu a:hover {
            background: #cceebe;
        }

        .profile-hero {
            background:
                linear-gradient(90deg, rgba(20,70,32,.82), rgba(42,122,67,.48)),
                url("https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=900&q=80");
            background-size: cover;
            background-position: center;
            border-radius: 24px;
            padding: 26px;
            color: white !important;
            display: flex;
            align-items: center;
            gap: 18px;
            box-shadow: 0 10px 28px rgba(30,80,35,.25);
            margin-bottom: 16px;
        }

        .profile-avatar {
            width: 92px;
            height: 92px;
            background: rgba(255,255,255,.94);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 48px;
            border: 4px solid #d9ffd0;
        }

        .profile-hero h2,
        .profile-hero p,
        .profile-hero small {
            color: white !important;
        }

        .profile-hero h2 {
            margin: 0;
            font-size: 31px;
            font-weight: 900;
        }

        .profile-hero p {
            margin: 6px 0;
            font-weight: 800;
        }

        .profile-summary-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            margin-bottom: 18px;
        }

        .summary-card {
            background: white;
            border: 1px solid #b7d9aa;
            border-radius: 18px;
            padding: 16px;
            color: #173d18;
            box-shadow: 0 6px 18px rgba(54,100,37,.10);
            display: flex;
            flex-direction: column;
            gap: 4px;
            font-weight: 900;
        }

        .summary-card b {
            font-size: 25px;
            color: #1f7a33;
        }

        .summary-card span {
            color: #496c42;
            font-size: 13px;
        }

        .section-title,
        .password-title {
            background: white;
            border: 1px solid #b7d9aa;
            border-radius: 20px;
            padding: 18px 24px;
            color: #173d18 !important;
            font-size: 22px;
            font-weight: 900;
            margin: 18px 0 18px;
            box-shadow: 0 6px 20px rgba(54,100,37,.12);
        }

        .data-card {
            background: white;
            border: 1px solid #b7d9aa;
            border-radius: 22px;
            padding: 16px;
            box-shadow: 0 8px 24px rgba(54,100,37,.13);
            position: sticky;
            top: 20px;
        }

        .data-card h3 {
            color: #173d18 !important;
            font-size: 20px;
            font-weight: 900;
            margin-bottom: 14px;
        }

        .stat-box {
            background: #f4fff0;
            border: 1px solid #c4e8b8;
            border-radius: 15px;
            padding: 13px;
            margin-bottom: 10px;
            color: #173d18 !important;
            font-weight: 800;
        }

        .stat-box b {
            color: #173d18 !important;
        }

        .my-post-card {
            background: white;
            border: 1px solid #b7d9aa;
            border-radius: 20px;
            padding: 14px;
            display: flex;
            align-items: center;
            gap: 14px;
            margin-bottom: 10px;
            box-shadow: 0 6px 18px rgba(54,100,37,.10);
        }

        .my-post-img {
            width: 118px;
            height: 96px;
            object-fit: cover;
            border-radius: 15px;
            border: 1px solid #d6edce;
        }

        .my-post-info {
            flex: 1;
        }

        .post-topline {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
        }

        .my-post-info h4 {
            margin: 0 0 6px;
            color: #173d18 !important;
            font-size: 22px;
            font-weight: 900;
        }

        .my-post-info p {
            color: #111 !important;
            margin: 0 0 8px;
            font-size: 16px;
            line-height: 1.45;
        }

        .my-post-info span {
            background: #dff1ff;
            color: #13517c !important;
            padding: 6px 11px;
            border-radius: 14px;
            font-weight: 900;
            display: inline-block;
            margin-right: 8px;
        }

        .my-post-info small {
            color: #55714e !important;
            font-weight: 800;
        }

        .status-pill {
            padding: 7px 10px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: 900;
            white-space: nowrap;
        }

        .status-posted {
            background: #ddf8df;
            color: #1f7a33;
        }

        .status-hidden {
            background: #fff1bf;
            color: #946000;
        }

        .status-draft {
            background: #e6ecff;
            color: #244aa5;
        }

        .go-news-btn {
            height: 46px;
            background: #e7f5ff;
            color: #13517c !important;
            text-decoration: none !important;
            border-radius: 16px;
            font-weight: 900;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px solid #b9dbf5;
        }

        div[data-testid="stTextInput"] label p {
            color: #173d18 !important;
            font-weight: 900 !important;
            font-size: 15px !important;
        }

        div[data-testid="stTextInput"] input {
            background: #ffffff !important;
            color: #111111 !important;
            border: 2px solid #2e7d32 !important;
            border-radius: 16px !important;
            font-size: 16px !important;
            font-weight: 700 !important;
            height: 52px !important;
            box-shadow: 0 4px 14px rgba(47,125,50,.12) !important;
        }

        div[data-testid="stTextInput"] input::placeholder {
            color: #6d7f68 !important;
            opacity: 1 !important;
            font-weight: 700 !important;
        }

        .stButton button {
            height: 48px !important;
            background: linear-gradient(135deg, #69c798, #24aaa3) !important;
            color: white !important;
            border-radius: 16px !important;
            font-weight: 900 !important;
            border: none !important;
            box-shadow: 0 8px 22px rgba(36,170,163,.22) !important;
        }

        .swcs-bottom-nav {
            position: fixed;
            left: 50%;
            bottom: 18px;
            transform: translateX(-50%);
            width: min(560px, calc(100% - 24px));
            height: 72px;
            background: rgba(255,255,255,.96);
            border: 1.5px solid #a6d995;
            border-radius: 28px;
            box-shadow: 0 10px 32px rgba(47,125,50,.25);
            display: flex;
            align-items: center;
            justify-content: space-around;
            z-index: 9999;
        }

        .swcs-nav-item {
            text-decoration: none !important;
            color: #4a4a4a !important;
            display: flex;
            flex-direction: column;
            align-items: center;
            font-size: 13px;
            font-weight: 800;
        }

        .swcs-nav-item.active {
            color: #2e7d32 !important;
        }

        .swcs-nav-icon {
            font-size: 22px;
        }

        .swcs-scan-btn {
            width: 68px;
            height: 68px;
            border-radius: 50%;
            background: linear-gradient(135deg, #42c96f, #1aa6a6);
            color: white !important;
            display: flex;
            align-items: center;
            justify-content: center;
            text-decoration: none !important;
            margin-top: -34px;
            box-shadow: 0 8px 24px rgba(26,166,166,.42);
            border: 5px solid white;
        }

        .swcs-nav-ai {
            font-size: 31px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )