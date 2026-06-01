import streamlit as st


def load_post_composer_css():
    st.markdown(
        """
        <style>
        .stApp {
            background:
                linear-gradient(rgba(245, 255, 236, 0.88), rgba(245, 255, 236, 0.88)),
                radial-gradient(circle at 20% 20%, #dff5c8 0 12%, transparent 13%),
                radial-gradient(circle at 80% 30%, #d9f4cc 0 10%, transparent 11%),
                radial-gradient(circle at 30% 80%, #e5f8d7 0 14%, transparent 15%);
            background-color: #f4ffe9;
        }

        header[data-testid="stHeader"] {
            display: none;
        }

        .block-container {
            max-width: 1180px;
            padding-top: 20px;
            padding-bottom: 110px;
        }

        .swsc-topbar {
            height: 58px;
            background: rgba(255, 255, 255, 0.92);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 32px;
            border-radius: 0 0 24px 24px;
            box-shadow: 0 4px 18px rgba(57, 100, 38, 0.12);
            margin: -20px -20px 22px -20px;
            position: sticky;
            top: 0;
            z-index: 20;
        }

        .swsc-logo {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 28px;
            font-weight: 900;
            color: #2f7d32;
        }

        .swsc-menu {
            display: flex;
            gap: 18px;
            align-items: center;
        }

        .swsc-menu a {
            text-decoration: none;
            color: #202020;
            font-size: 15px;
            padding: 10px 18px;
            border-radius: 24px;
        }

        .swsc-menu a.active {
            background: #c9edbc;
            color: #346b29;
            font-weight: 700;
        }

        .swsc-user-icons {
            display: flex;
            align-items: center;
            gap: 18px;
            font-size: 20px;
        }

        .swsc-layout {
            display: grid;
            grid-template-columns: minmax(0, 1fr) 270px;
            gap: 22px;
            align-items: start;
        }

        .composer-card {
            background: rgba(255, 255, 255, 0.92);
            border: 1.5px solid #84b96f;
            border-radius: 24px;
            box-shadow: 0 8px 24px rgba(54, 100, 37, 0.18);
            padding: 22px;
        }

        .composer-title {
            color: #2e7d32;
            font-size: 31px;
            font-weight: 900;
            margin-bottom: 18px;
            line-height: 1.25;
        }

        .field-label {
            font-weight: 800;
            color: #111;
            margin-bottom: 7px;
            font-size: 16px;
        }

        .title-input {
            width: 100%;
            border: 1.6px solid #6da85d;
            border-radius: 18px;
            padding: 13px 18px;
            font-size: 16px;
            outline: none;
            background: white;
            margin-bottom: 18px;
        }

        .category-row {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 18px;
        }

        .category-pill {
            padding: 10px 18px;
            border-radius: 24px;
            border: 1.4px solid rgba(0,0,0,.2);
            font-weight: 700;
            font-size: 15px;
            box-shadow: 0 3px 8px rgba(0,0,0,.08);
        }

        .category-pill.organic {
            background: linear-gradient(180deg, #eaffdf, #bdf2aa);
        }

        .category-pill.recycle {
            background: linear-gradient(180deg, #e6f3ff, #afd6ff);
        }

        .category-pill.danger {
            background: linear-gradient(180deg, #ffe8e4, #ffb9b0);
        }

        .category-pill.tips {
            background: linear-gradient(180deg, #fff8d8, #ffe999);
        }

        .editor-box {
            border: 1.8px solid #73a961;
            border-radius: 18px;
            overflow: hidden;
            background: #fffdf5;
            margin-bottom: 18px;
        }

        .editor-toolbar {
            display: flex;
            gap: 16px;
            padding: 12px 16px;
            font-size: 21px;
            font-weight: 900;
            border-bottom: 1px solid #e5e0be;
            background: #fff8d8;
        }

        .editor-content {
            padding: 16px;
            min-height: 92px;
            font-size: 17px;
            line-height: 1.65;
            color: #222;
        }

        .upload-box {
            border: 2px dashed #9c945d;
            background: #fff9df;
            border-radius: 18px;
            height: 135px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 8px;
            margin-bottom: 18px;
            color: #222;
            font-size: 16px;
            text-align: center;
        }

        .upload-icon {
            font-size: 48px;
        }

        .composer-actions {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .draft-btn {
            background: white;
            color: #222;
            border: 1.5px solid #d4d4d4;
            padding: 12px 22px;
            border-radius: 25px;
            font-size: 16px;
            text-decoration: none;
            box-shadow: 0 3px 10px rgba(0,0,0,.08);
        }

        .post-btn {
            background: linear-gradient(135deg, #69c798, #24aaa3);
            color: white;
            border: none;
            padding: 14px 27px;
            border-radius: 26px;
            font-weight: 900;
            font-size: 16px;
            text-decoration: none;
            box-shadow: 0 8px 20px rgba(36, 170, 163, .35);
        }

        .sidebar-card {
            border-radius: 18px;
            padding: 18px;
            margin-bottom: 18px;
            box-shadow: 0 5px 16px rgba(54, 100, 37, 0.18);
            border: 1.3px solid rgba(74, 126, 58, .35);
            font-size: 16px;
        }

        .sidebar-card h3 {
            margin: 0 0 12px 0;
            font-size: 18px;
            color: #111;
        }

        .challenge-card {
            background: #dff3cf;
        }

        .hashtag-card {
            background: #d9efff;
        }

        .tip-card {
            background: #fff1b8;
        }

        .hashtag {
            display: inline-block;
            background: rgba(255,255,255,.55);
            padding: 8px 12px;
            border-radius: 10px;
            margin: 5px 0;
            font-weight: 700;
        }

        .swcs-bottom-nav {
            position: fixed;
            left: 50%;
            bottom: 18px;
            transform: translateX(-50%);
            width: min(560px, calc(100% - 24px));
            height: 72px;
            background: rgba(255, 255, 255, 0.96);
            border: 1.5px solid #a6d995;
            border-radius: 28px;
            box-shadow: 0 10px 32px rgba(47, 125, 50, 0.25);
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
            font-weight: 700;
            gap: 3px;
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
            box-shadow: 0 8px 24px rgba(26, 166, 166, 0.42);
            border: 5px solid white;
        }

        .swcs-nav-ai {
            font-size: 31px;
        }

        @media (max-width: 900px) {
            .swsc-layout {
                grid-template-columns: 1fr;
            }

            .swsc-menu {
                display: none;
            }

            .composer-title {
                font-size: 25px;
            }

            .swsc-topbar {
                padding: 0 16px;
            }
        }
        .composer-card-title {
    background: rgba(255, 255, 255, 0.95);
    border: 1.5px solid #84b96f;
    border-radius: 24px;
    box-shadow: 0 8px 24px rgba(54, 100, 37, 0.18);
    padding: 24px;
    margin-bottom: 18px;
}

.stTextInput label,
.stTextArea label,
.stRadio label,
.stFileUploader label {
    color: #111 !important;
    font-weight: 800 !important;
}

.stTextInput input,
.stTextArea textarea {
    background: #ffffff !important;
    color: #111 !important;
    border-radius: 14px !important;
}

.stButton button {
    border-radius: 18px !important;
    font-weight: 800 !important;
}

.stRadio div[role="radiogroup"] label {
    color: #111 !important;
}
/* Hiện chữ rõ hơn */
.stTextInput label,
.stTextArea label,
.stRadio label,
.stFileUploader label {
    color: #163b16 !important;
    font-size: 16px !important;
    font-weight: 800 !important;
}

.stTextInput input,
.stTextArea textarea {
    background: #ffffff !important;
    color: #1f1f1f !important;
    font-size: 16px !important;
    font-weight: 500 !important;
    border: 1.8px solid #6da85d !important;
    border-radius: 14px !important;
}

.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #5f6f5f !important;
    opacity: 1 !important;
}

.stRadio div[role="radiogroup"] label p {
    color: #1f1f1f !important;
    font-weight: 700 !important;
    font-size: 15px !important;
}

.stFileUploader section {
    background: #ffffff !important;
    border: 2px dashed #6da85d !important;
    border-radius: 16px !important;
}

.stFileUploader section * {
    color: #1f1f1f !important;
}

.sidebar-card,
.sidebar-card h3,
.sidebar-card div,
.hashtag {
    color: #1f1f1f !important;
}

.hashtag {
    background: rgba(255, 255, 255, 0.75) !important;
}

.stButton button {
    background: linear-gradient(135deg, #69c798, #24aaa3) !important;
    color: white !important;
    border-radius: 18px !important;
    font-weight: 900 !important;
    font-size: 16px !important;
    border: none !important;
}
/* Làm giao diện đẹp hơn */
.block-container {
    padding-top: 50px !important;
}

.composer-card-title {
    background: linear-gradient(135deg, #ffffff, #f4fff1);
}

.composer-title::before {
    content: "🌍 ";
}

.composer-title::after {
    content: " ✨♻️";
}

.stTextInput label::before {
    content: "📝 ";
}

.stRadio > label::before {
    content: "🏷️ ";
}

.stTextArea label::before {
    content: "💬 ";
}

.stFileUploader label::before {
    content: "📸 ";
}

.stRadio div[role="radiogroup"] label:nth-child(1) p::before {
    content: "🍃 ";
}

.stRadio div[role="radiogroup"] label:nth-child(2) p::before {
    content: "♻️ ";
}

.stRadio div[role="radiogroup"] label:nth-child(3) p::before {
    content: "⚠️ ";
}

.stRadio div[role="radiogroup"] label:nth-child(4) p::before {
    content: "💡 ";
}

.stTextInput input,
.stTextArea textarea {
    box-shadow: 0 4px 14px rgba(47, 125, 50, 0.12) !important;
}

.stFileUploader section {
    background: linear-gradient(135deg, #ffffff, #f8fff2) !important;
    box-shadow: 0 4px 14px rgba(47, 125, 50, 0.12) !important;
}

.stButton button {
    height: 50px !important;
    box-shadow: 0 8px 22px rgba(36, 170, 163, 0.28) !important;
}

.stButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 26px rgba(36, 170, 163, 0.38) !important;
}

.challenge-card h3::after {
    content: " 🌱";
}

.hashtag-card h3::after {
    content: " 🔥";
}

.tip-card h3::after {
    content: " ✅";
}

.sidebar-card {
    transition: 0.25s ease;
}

.sidebar-card:hover {
    transform: translateY(-4px);
}

.hashtag::before {
    content: "🔖 ";
}

.swcs-bottom-nav {
    backdrop-filter: blur(14px);
}

.swcs-nav-item:hover {
    transform: translateY(-3px);
}

.swcs-scan-btn {
    animation: swcsPulse 1.8s infinite;
}

@keyframes swcsPulse {
    0% {
        box-shadow: 0 0 0 0 rgba(36, 170, 163, 0.45);
    }
    70% {
        box-shadow: 0 0 0 16px rgba(36, 170, 163, 0);
    }
    100% {
        box-shadow: 0 0 0 0 rgba(36, 170, 163, 0);
    }
}
        </style>
        """,
        unsafe_allow_html=True,
    )