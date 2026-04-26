import streamlit as st


def load_homepage_user_css():
    st.markdown(
        """
        <style>
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(168, 208, 132, 0.14), transparent 24%),
                radial-gradient(circle at bottom right, rgba(186, 224, 160, 0.14), transparent 24%),
                linear-gradient(180deg, #f7fbf5 0%, #edf5ea 100%);
        }

        .main .block-container {
            max-width: 980px;
            padding-top: 0.28rem;
            padding-bottom: 4.2rem;
        }

        .swcs-home-user-nav {
            width: 100%;
            background: rgba(255, 255, 255, 0.94);
            border: 1px solid rgba(232, 239, 226, 0.94);
            border-radius: 18px;
            padding: 10px 18px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            box-shadow: 0 10px 22px rgba(78, 104, 62, 0.06);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            margin-bottom: 12px;
        }

        .swcs-home-user-brand {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 26px;
            font-weight: 900;
            color: #4e9432;
            flex-shrink: 0;
        }

        .swcs-home-user-brand-icon {
            font-size: 26px;
        }

        .swcs-home-user-links {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 18px;
            flex: 1;
            flex-wrap: wrap;
        }

        .swcs-home-user-links a {
            color: #2f3e2e;
            text-decoration: none;
            font-size: 14px;
            font-weight: 700;
        }

        .swcs-home-user-search-btn {
            width: 38px;
            height: 38px;
            border-radius: 50%;
            background: rgba(255,255,255,0.96);
            border: 1px solid #e5ebe1;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 17px;
            color: #243b1f;
            flex-shrink: 0;
        }

        .swcs-home-user-title {
            text-align: center;
            font-size: 38px;
            line-height: 1.08;
            font-weight: 900;
            color: #2b5c26;
            margin: 2px 0 10px 0;
            text-shadow: 0 1px 0 rgba(255,255,255,0.35);
        }

        .swcs-home-user-search-card {
            background: rgba(255,255,255,0.56);
            border: 1px solid rgba(233, 239, 227, 0.94);
            border-radius: 24px;
            padding: 10px;
            box-shadow: 0 10px 24px rgba(78, 104, 62, 0.06);
            backdrop-filter: blur(6px);
            -webkit-backdrop-filter: blur(6px);
            margin-bottom: 10px;
        }

        .swcs-home-user-search-inner {
            background: rgba(255,255,255,0.98);
            border: 1px solid rgba(232,239,226,0.96);
            border-radius: 999px;
            padding: 4px 10px;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.9);
        }

        .swcs-home-user-composer-card,
        .swcs-home-user-post-card {
            background: rgba(255,255,255,0.88);
            border: 1px solid rgba(232,239,226,0.96);
            border-radius: 20px;
            padding: 12px;
            box-shadow: 0 10px 22px rgba(78,104,62,0.06);
            backdrop-filter: blur(6px);
            -webkit-backdrop-filter: blur(6px);
            margin-bottom: 10px;
        }

        .swcs-home-user-composer-row,
        .swcs-post-head {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
        }

        .swcs-home-user-composer-left,
        .swcs-post-author {
            display: flex;
            align-items: center;
            gap: 10px;
            min-width: 0;
        }

        .swcs-home-user-avatar,
        .swcs-post-avatar {
            width: 48px;
            height: 48px;
            border-radius: 50%;
            overflow: hidden;
            border: 2px solid rgba(255,255,255,0.95);
            box-shadow: 0 6px 14px rgba(15,23,42,0.07);
            flex-shrink: 0;
        }

        .swcs-home-user-avatar img,
        .swcs-post-avatar img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        .swcs-home-user-composer-text {
            font-size: 16px;
            font-weight: 800;
            color: #1f2c1d;
            line-height: 1.2;
        }

        .swcs-home-user-camera-btn {
            width: 48px;
            height: 48px;
            border-radius: 16px;
            background: rgba(255,255,255,0.95);
            border: 1px solid rgba(232,239,226,0.95);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 22px;
            color: #496d3b;
            box-shadow: 0 6px 14px rgba(78,104,62,0.06);
            flex-shrink: 0;
        }

        .swcs-post-name {
            font-size: 17px;
            font-weight: 900;
            color: #1f2e1c;
            line-height: 1.1;
        }

        .swcs-post-time {
            font-size: 12px;
            color: #6f746b;
            line-height: 1.2;
            margin-top: 2px;
        }

        .swcs-post-menu {
            font-size: 24px;
            line-height: 1;
            color: #202020;
            padding: 0 2px;
            flex-shrink: 0;
        }

        .swcs-post-content {
            font-size: 14px;
            line-height: 1.5;
            color: #202720;
            margin: 8px 1px 8px 1px;
        }

        .swcs-post-images-grid {
            display: grid;
            grid-template-columns: 1.08fr 1fr;
            gap: 8px;
            margin-bottom: 10px;
        }

        .swcs-post-image-large {
            height: 158px;
            border-radius: 14px;
            overflow: hidden;
        }

        .swcs-post-image-stack {
            display: grid;
            grid-template-rows: 1fr 1fr;
            gap: 8px;
        }

        .swcs-post-image-small {
            height: 75px;
            border-radius: 14px;
            overflow: hidden;
        }

        .swcs-post-image-single {
            width: 100%;
            height: 165px;
            border-radius: 16px;
            overflow: hidden;
            margin-bottom: 10px;
        }

        .swcs-post-image-large img,
        .swcs-post-image-small img,
        .swcs-post-image-single img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        .swcs-post-footer {
            display: flex;
            align-items: center;
            gap: 18px;
            flex-wrap: wrap;
            padding: 2px 2px 0 2px;
        }

        .swcs-post-stat {
            display: inline-flex;
            align-items: center;
            gap: 7px;
            font-size: 14px;
            font-weight: 700;
            color: #1f2320;
        }

        .swcs-post-stat.like .icon {
            color: #ff2d2d;
        }

        .swcs-post-stat .icon {
            font-size: 15px;
            line-height: 1;
        }

        .swcs-home-user-feed-info {
            padding: 6px 10px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 700;
            margin-bottom: 8px;
            background: rgba(111, 190, 104, 0.14);
            color: #2f6d25;
            border: 1px solid rgba(111, 190, 104, 0.20);
        }

        /* ===== CAMERA FLOAT BUTTON ===== */

        .swcs-camera-fab-wrap {
            position: fixed;
            left: 50%;
            bottom: 18px;
            transform: translateX(-50%);
            z-index: 999;
        }

        .swcs-camera-fab {
            width: 78px;
            height: 78px;
            border-radius: 50%;
            background: linear-gradient(145deg, #ffffff, #eef5ea);
            border: 1px solid rgba(220, 230, 215, 0.95);
            box-shadow:
                0 10px 24px rgba(78, 104, 62, 0.18),
                0 4px 10px rgba(0,0,0,0.08);
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            text-decoration: none;
        }

        .swcs-camera-fab-inner {
            width: 42px;
            height: 42px;
            border: 3px solid #2f6d25;
            border-radius: 12px;
            position: relative;
            box-sizing: border-box;
        }

        /* 4 góc scan rõ hơn */
        .swcs-camera-fab-inner::before,
        .swcs-camera-fab-inner::after {
            content: "";
            position: absolute;
            width: 12px;
            height: 12px;
            border: 3px solid #2f6d25;
            box-sizing: border-box;
        }

        .swcs-camera-fab-inner::before {
            top: -7px;
            left: -7px;
            border-right: none;
            border-bottom: none;
            border-top-left-radius: 4px;
        }

        .swcs-camera-fab-inner::after {
            bottom: -7px;
            right: -7px;
            border-left: none;
            border-top: none;
            border-bottom-right-radius: 4px;
        }

        /* lõi icon ở giữa để dễ nhìn hơn */
        .swcs-camera-fab-core {
            position: absolute;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #2f6d25;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            box-shadow: 0 0 0 3px rgba(47, 109, 37, 0.14);
        }

        .swcs-camera-fab:hover {
            transform: translateY(-2px);
            box-shadow:
                0 14px 28px rgba(78, 104, 62, 0.24),
                0 6px 12px rgba(0,0,0,0.10);
        }

        /* mobile */
        @media (max-width: 640px) {
            .swcs-camera-fab-wrap {
                bottom: 14px;
            }

            .swcs-camera-fab {
                width: 66px;
                height: 66px;
            }

            .swcs-camera-fab-inner {
                width: 36px;
                height: 36px;
                border-radius: 10px;
            }

            .swcs-camera-fab-core {
                width: 10px;
                height: 10px;
            }
        }

        div[data-testid="stTextInput"] input {
            min-height: 42px !important;
            border-radius: 999px !important;
            border: none !important;
            box-shadow: none !important;
            background: transparent !important;
            font-size: 15px !important;
            color: #333 !important;
            padding-left: 8px !important;
        }

        div[data-testid="stTextInput"] input::placeholder {
            color: #6f746b !important;
            opacity: 1 !important;
        }

        @media (max-width: 900px) {
            .main .block-container {
                max-width: 100%;
            }

            .swcs-home-user-nav {
                flex-wrap: wrap;
                justify-content: center;
            }

            .swcs-home-user-links {
                order: 3;
                width: 100%;
                justify-content: center;
                gap: 14px;
            }

            .swcs-home-user-title {
                font-size: 34px;
            }

            .swcs-post-images-grid {
                grid-template-columns: 1fr;
            }

            .swcs-post-image-large,
            .swcs-post-image-single {
                height: 180px;
            }

            .swcs-post-image-stack {
                grid-template-rows: repeat(2, 110px);
            }

            .swcs-post-image-small {
                height: 110px;
            }
        }

        @media (max-width: 640px) {
            .main .block-container {
                max-width: 100%;
                padding-top: 0.35rem;
                padding-bottom: 5rem;
            }

            .swcs-home-user-nav {
                padding: 12px 12px;
                border-radius: 16px;
                margin-bottom: 12px;
            }

            .swcs-home-user-brand {
                font-size: 24px;
            }

            .swcs-home-user-brand-icon {
                font-size: 24px;
            }

            .swcs-home-user-links {
                display: none;
            }

            .swcs-home-user-title {
                font-size: 30px;
                margin-bottom: 10px;
            }

            .swcs-home-user-search-card {
                padding: 8px;
                border-radius: 18px;
            }

            .swcs-home-user-composer-card,
            .swcs-home-user-post-card {
                border-radius: 18px;
                padding: 10px;
            }

            .swcs-home-user-avatar,
            .swcs-post-avatar {
                width: 42px;
                height: 42px;
            }

            .swcs-home-user-composer-text {
                font-size: 14px;
            }

            .swcs-home-user-camera-btn {
                width: 42px;
                height: 42px;
                font-size: 18px;
                border-radius: 14px;
            }

            .swcs-post-name {
                font-size: 15px;
            }

            .swcs-post-time {
                font-size: 11px;
            }

            .swcs-post-content {
                font-size: 13px;
                margin-top: 8px;
            }

            .swcs-post-image-large,
            .swcs-post-image-single {
                height: 160px;
            }

            .swcs-post-image-stack {
                grid-template-rows: repeat(2, 90px);
            }

            .swcs-post-image-small {
                height: 90px;
            }

            .swcs-post-footer {
                gap: 12px;
            }

            .swcs-post-stat {
                font-size: 13px;
            }

            .swcs-camera-fab {
                width: 62px;
                height: 62px;
                font-size: 26px;
            }

            .swcs-camera-fab::after {
                inset: 8px;
                border-radius: 14px;
            }

            div[data-testid="stTextInput"] input {
                min-height: 40px !important;
                font-size: 14px !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )