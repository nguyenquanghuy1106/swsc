import streamlit as st


def load_news_css():
    st.markdown(
        """
        <style>
        .stApp {
            background:
                linear-gradient(rgba(245, 255, 236, 0.90), rgba(245, 255, 236, 0.90)),
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
            padding-top: 45px;
            padding-bottom: 120px;
        }

        .news-title-card {
            background: rgba(255,255,255,.96);
            border: 1.5px solid #8bc77a;
            border-radius: 24px;
            padding: 22px 26px;
            margin-bottom: 18px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 8px 24px rgba(54, 100, 37, 0.16);
        }

        .news-title-card h1 {
            margin: 0;
            font-size: 32px;
            color: #2e7d32;
            font-weight: 900;
        }

        .news-title-card p {
            margin: 6px 0 0 0;
            color: #456b3d;
            font-weight: 600;
        }

        .news-counter {
            width: 95px;
            height: 95px;
            border-radius: 24px;
            background: linear-gradient(135deg, #c7f5b9, #60c98d);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: #113f1d;
            box-shadow: 0 8px 20px rgba(47, 125, 50, .22);
        }

        .news-counter span {
            font-size: 26px;
        }

        .news-counter b {
            font-size: 24px;
        }

        .news-counter small {
            font-weight: 700;
        }

        .challenge-done-card {
            background: #ffffff;
            border: 1.5px solid #86bd70;
            border-radius: 22px;
            padding: 18px 22px;
            margin-bottom: 18px;
            box-shadow: 0 6px 18px rgba(54, 100, 37, 0.14);
        }

        .challenge-title {
            color: #2e7d32;
            font-size: 22px;
            font-weight: 900;
            margin-bottom: 8px;
        }

        .challenge-text {
            color: #1f1f1f;
            font-size: 16px;
            font-weight: 600;
        }

        .news-post-card {
            background: rgba(255,255,255,.97);
            border: 1.5px solid #8bc77a;
            border-radius: 24px;
            padding: 16px;
            margin-bottom: 18px;
            box-shadow: 0 8px 24px rgba(54, 100, 37, 0.16);
            transition: .25s ease;
        }

        .news-post-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 12px 28px rgba(54, 100, 37, 0.22);
        }

        .post-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 12px;
        }

        .avatar-circle {
            width: 45px;
            height: 45px;
            border-radius: 50%;
            background: linear-gradient(135deg, #dff8d4, #9ee28e);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            border: 2px solid white;
            box-shadow: 0 4px 10px rgba(0,0,0,.12);
        }

        .author-name {
            color: #111;
            font-weight: 900;
            font-size: 16px;
        }

        .post-time {
            color: #56734d;
            font-size: 13px;
            font-weight: 600;
        }

        .post-more {
            margin-left: auto;
            color: #333;
            font-weight: 900;
            font-size: 20px;
        }

        .post-title {
            color: #173d18;
            font-size: 20px;
            font-weight: 900;
            margin-bottom: 8px;
        }

        .post-content {
            color: #202020;
            font-size: 16px;
            line-height: 1.55;
            font-weight: 500;
        }

        .post-category {
            display: inline-flex;
            align-items: center;
            gap: 7px;
            background: #dff1ff;
            color: #13517c;
            padding: 7px 13px;
            border-radius: 20px;
            font-weight: 800;
            margin-top: 12px;
            margin-bottom: 10px;
        }

        .post-footer {
            border-top: 1px solid #e1edd9;
            padding-top: 12px;
            margin-top: 12px;
            display: flex;
            align-items: center;
            gap: 22px;
            color: #333;
            font-weight: 800;
        }

        .coin {
            margin-left: auto;
            color: #8a6b00;
        }

        .sidebar-card {
            border-radius: 20px;
            padding: 18px;
            margin-bottom: 18px;
            box-shadow: 0 5px 16px rgba(54, 100, 37, 0.18);
            border: 1.3px solid rgba(74, 126, 58, .35);
            font-size: 16px;
            color: #111;
            transition: .25s ease;
        }

        .sidebar-card:hover {
            transform: translateY(-4px);
        }

        .sidebar-card h3 {
            margin: 0 0 14px 0;
            font-size: 18px;
            color: #111;
            font-weight: 900;
        }

        .challenge-card {
            background: #dff3cf;
        }

        .member-card {
            background: #fff;
        }

        .member-row {
            display: flex;
            gap: 8px;
            font-size: 28px;
        }

        .hashtag-card {
            background: #d9efff;
        }

        .tip-card {
            background: #fff1b8;
        }

        .hashtag {
            display: inline-block;
            background: rgba(255,255,255,.75);
            padding: 8px 12px;
            border-radius: 12px;
            margin: 5px 0;
            font-weight: 900;
            color: #111;
        }

        .progress-bar {
            height: 11px;
            background: rgba(255,255,255,.7);
            border-radius: 20px;
            margin-top: 12px;
            overflow: hidden;
        }

        .progress-fill {
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, #53c765, #2ba64c);
            border-radius: 20px;
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
            backdrop-filter: blur(14px);
        }

        .swcs-nav-item {
            text-decoration: none;
            color: #4a4a4a;
            display: flex;
            flex-direction: column;
            align-items: center;
            font-size: 13px;
            font-weight: 800;
            gap: 3px;
            transition: .25s ease;
        }

        .swcs-nav-item.active {
            color: #2e7d32;
        }

        .swcs-nav-item:hover {
            transform: translateY(-3px);
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
            animation: swcsPulse 1.8s infinite;
        }

        .swcs-nav-ai {
            font-size: 31px;
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

        @media (max-width: 900px) {
            .news-title-card {
                flex-direction: column;
                align-items: flex-start;
                gap: 14px;
            }
        }
        .news-post-card {
    overflow: hidden;
}

.news-image {
    width: 100%;
    max-height: 360px;
    object-fit: cover;
    border-radius: 18px;
    margin-top: 14px;
    border: 1px solid #cfe8c7;
    box-shadow: 0 6px 18px rgba(0,0,0,.10);
}

.post-stats {
    margin-top: 12px;
    padding-top: 10px;
    border-top: 1px solid #e1edd9;
    display: flex;
    gap: 22px;
    font-weight: 800;
    color: #333;
}

.comment-item {
    background: #ffffff;
    border: 1px solid #d7ecd0;
    border-radius: 14px;
    padding: 10px 12px;
    margin: 8px 0;
    color: #111;
}

.comment-item p {
    margin: 5px 0;
}

.comment-item small {
    color: #5c7357;
}

.share-text {
    padding: 12px;
    color: #2e7d32;
    font-weight: 800;
}

.stButton button {
    border-radius: 18px !important;
    font-weight: 900 !important;
    background: linear-gradient(135deg, #69c798, #24aaa3) !important;
    color: white !important;
    border: none !important;
}
.news-image-wrap {
    width: 100%;
    max-height: 380px;
    overflow: hidden;
    border-radius: 18px;
    margin-top: 14px;
    background: #f5fff0;
    display: flex;
    align-items: center;
    justify-content: center;
}

.news-image {
    width: 100%;
    height: 100%;
    max-height: 380px;
    object-fit: contain;
    border-radius: 18px;
    border: 1px solid #cfe8c7;
    box-shadow: 0 6px 18px rgba(0,0,0,.10);
}

.comment-panel {
    background: rgba(255, 255, 255, 0.96);
    border: 1.5px solid #9bd98a;
    border-radius: 22px;
    padding: 18px;
    margin-top: 12px;
    margin-bottom: 24px;
    box-shadow: 0 8px 24px rgba(54, 100, 37, 0.16);
}

.comment-panel-title {
    color: #205c26;
    font-size: 18px;
    font-weight: 900;
    margin-bottom: 12px;
}

div[data-testid="stTextArea"] textarea {
    background: #ffffff !important;
    color: #1f1f1f !important;
    border: 1.8px solid #7fbd70 !important;
    border-radius: 16px !important;
    font-size: 15px !important;
    box-shadow: 0 4px 12px rgba(47, 125, 50, 0.12) !important;
}

div[data-testid="stTextArea"] textarea::placeholder {
    color: #64835e !important;
    opacity: 1 !important;
}

.comment-item {
    display: flex;
    gap: 12px;
    background: #f8fff4;
    border: 1px solid #d7ecd0;
    border-radius: 16px;
    padding: 12px;
    margin: 10px 0;
    color: #111;
}

.comment-avatar {
    width: 38px;
    height: 38px;
    border-radius: 50%;
    background: linear-gradient(135deg, #c8f5b8, #72d887);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    box-shadow: 0 4px 10px rgba(0,0,0,.12);
}

.comment-content-box {
    flex: 1;
}

.comment-author {
    font-weight: 900;
    color: #173d18;
    margin-bottom: 4px;
}

.comment-text {
    color: #222;
    font-size: 15px;
    line-height: 1.45;
    margin-bottom: 5px;
}

.comment-time {
    color: #5c7357;
    font-size: 12px;
    font-weight: 700;
}

.empty-comment {
    background: #f8fff4;
    border: 1px dashed #9bd98a;
    color: #2e7d32;
    font-weight: 800;
    border-radius: 14px;
    padding: 12px;
    margin-top: 12px;
}

.post-stats {
    margin-top: 14px;
    padding-top: 12px;
    border-top: 1px solid #e1edd9;
    display: flex;
    gap: 22px;
    font-weight: 900;
    color: #173d18;
}

.share-text {
    padding: 12px;
    color: #2e7d32;
    font-weight: 900;
}
        </style>
        """,
        unsafe_allow_html=True,
    )