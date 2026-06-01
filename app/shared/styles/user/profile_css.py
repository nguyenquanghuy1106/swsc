import streamlit as st


def load_profile_css():
    st.markdown(
        """
        <style>
        .stApp {
            background: #f1ffe9;
        }

        header[data-testid="stHeader"] {
            display: none;
        }

        .block-container {
            max-width: 1180px;
            padding-top: 28px;
            padding-bottom: 120px;
        }

        .profile-menu {
            background: rgba(255,255,255,.75);
            border-radius: 18px;
            padding: 14px;
            border: 1px solid #b7d9aa;
            box-shadow: 0 8px 24px rgba(54,100,37,.12);
        }

        .profile-menu a {
            display: block;
            text-decoration: none;
            color: #173d18;
            font-weight: 800;
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
                linear-gradient(90deg, rgba(20,70,32,.75), rgba(42,122,67,.45)),
                url("https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=900&q=80");
            background-size: cover;
            background-position: center;
            border-radius: 22px;
            padding: 24px;
            color: white;
            display: flex;
            align-items: center;
            gap: 18px;
            box-shadow: 0 10px 28px rgba(30,80,35,.25);
            margin-bottom: 16px;
        }

        .profile-avatar {
            width: 88px;
            height: 88px;
            background: rgba(255,255,255,.9);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 46px;
            border: 4px solid #d9ffd0;
        }

        .profile-hero h2 {
            margin: 0;
            font-size: 30px;
            font-weight: 900;
        }

        .profile-hero p {
            margin: 6px 0;
            font-weight: 700;
        }

        .section-title {
            background: white;
            border: 1px solid #b7d9aa;
            border-radius: 16px;
            padding: 14px 18px;
            color: #173d18;
            font-size: 20px;
            font-weight: 900;
            margin: 16px 0 12px;
            box-shadow: 0 5px 18px rgba(54,100,37,.10);
        }

        .badge-grid {
            background: white;
            border: 1px solid #b7d9aa;
            border-radius: 20px;
            padding: 18px;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 14px;
            box-shadow: 0 8px 24px rgba(54,100,37,.12);
        }

        .badge-card {
            background: linear-gradient(135deg, #e9ffe1, #bdf1ae);
            border-radius: 18px;
            min-height: 105px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 8px;
            font-size: 34px;
            color: #205c26;
            text-align: center;
            border: 1px solid #9fd68e;
        }

        .badge-card b {
            font-size: 13px;
        }

        .badge-card.locked {
            filter: grayscale(1);
            opacity: .55;
        }

        .data-card {
            background: white;
            border: 1px solid #b7d9aa;
            border-radius: 20px;
            padding: 16px;
            box-shadow: 0 8px 24px rgba(54,100,37,.12);
        }

        .data-card h3 {
            color: #173d18;
            font-size: 20px;
            font-weight: 900;
            margin-bottom: 14px;
        }

        .stat-box {
            background: #f4fff0;
            border: 1px solid #c4e8b8;
            border-radius: 14px;
            padding: 12px;
            margin-bottom: 10px;
            color: #173d18;
            font-weight: 700;
        }

        .my-post-card {
            background: white;
            border: 1px solid #b7d9aa;
            border-radius: 18px;
            padding: 12px;
            display: flex;
            gap: 12px;
            margin-bottom: 12px;
            box-shadow: 0 6px 18px rgba(54,100,37,.10);
        }

        .my-post-img {
            width: 110px;
            height: 90px;
            object-fit: cover;
            border-radius: 14px;
        }

        .my-post-card h4 {
            margin: 0 0 6px;
            color: #173d18;
            font-weight: 900;
        }

        .my-post-card p {
            color: #222;
            margin: 0 0 8px;
        }

        .my-post-card span {
            background: #dff1ff;
            color: #13517c;
            padding: 5px 10px;
            border-radius: 14px;
            font-weight: 800;
            display: inline-block;
            margin-right: 8px;
        }

        .my-post-card small {
            color: #55714e;
            font-weight: 700;
        }

        .stTextInput input {
            background: white !important;
            color: #111 !important;
            border: 1.7px solid #77b567 !important;
            border-radius: 14px !important;
        }

        .stButton button {
            background: linear-gradient(135deg, #69c798, #24aaa3) !important;
            color: white !important;
            border-radius: 18px !important;
            font-weight: 900 !important;
            border: none !important;
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
            text-decoration: none;
            color: #4a4a4a;
            display: flex;
            flex-direction: column;
            align-items: center;
            font-size: 13px;
            font-weight: 800;
        }

        .swcs-nav-item.active {
            color: #2e7d32;
        }

        .swcs-nav-icon {
            font-size: 22px;
        }

        .swcs-scan-btn {
            width: 68px;
            height: 68px;
            border-radius: 50%;
            background: linear-gradient(135deg, #42c96f, #1aa6a6);
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            margin-top: -34px;
            box-shadow: 0 8px 24px rgba(26,166,166,.42);
            border: 5px solid white;
        }

        .swcs-nav-ai {
            font-size: 31px;
        }
        .password-box {
    background:transparent;
    border:none;
    box-shadow:none;
    padding:0;
    margin:0 0 12px 0;
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
    font-weight: 600 !important;
}

.my-post-card {
    align-items: center;
}

.my-post-info h4,
.my-post-info p,


.my-post-info h4 {
    font-size: 22px;
}

.my-post-info p {
    font-size: 16px;
}
        </style>
        """,
        unsafe_allow_html=True,
    )