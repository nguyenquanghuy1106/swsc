import subprocess
import sys
from pathlib import Path
from urllib.parse import quote

import streamlit as st


def _clean_html(html: str) -> str:
    return "".join(line.strip() for line in html.splitlines() if line.strip())


def _page_url(page):
    user_id = st.session_state.get("user_id")
    user_name = st.session_state.get("user_name")

    if user_id and user_name:
        return f"?page={page}&uid={user_id}&uname={quote(str(user_name))}"

    return f"?page={page}"


def _render_bottom_nav():
    return (
        '<div class="swcs-bottom-nav">'
        f'<a class="swcs-nav-item" href="{_page_url("home")}" target="_top"><span class="swcs-nav-icon">🏠</span><span>Trang chủ</span></a>'
        f'<a class="swcs-nav-item" href="{_page_url("post")}" target="_top"><span class="swcs-nav-icon">📚</span><span>Bài đăng</span></a>'
        f'<a class="swcs-scan-btn active-ai" href="{_page_url("camera")}" target="_top"><span class="swcs-nav-ai">🤖</span></a>'
        f'<a class="swcs-nav-item" href="{_page_url("news")}" target="_top"><span class="swcs-nav-icon">📰</span><span>Tin tức</span></a>'
        f'<a class="swcs-nav-item" href="{_page_url("profile")}" target="_top"><span class="swcs-nav-icon">👤</span><span>Profile</span></a>'
        "</div>"
    )


def _load_camera_css():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #f3ffed, #e9f8e3) !important;
        }

        header[data-testid="stHeader"] {
            display: none;
        }

        .block-container {
            max-width: 1120px !important;
            padding-top: 36px !important;
            padding-bottom: 130px !important;
        }

        .camera-hero {
            background: linear-gradient(135deg, rgba(17,86,45,.92), rgba(32,160,116,.78));
            border-radius: 30px;
            padding: 34px;
            color: white;
            box-shadow: 0 18px 42px rgba(25,95,58,.28);
            margin-bottom: 22px;
        }

        .camera-hero h1 {
            margin: 0;
            font-size: 38px;
            font-weight: 950;
            color: white !important;
        }

        .camera-hero p {
            color: rgba(255,255,255,.94) !important;
            font-size: 17px;
            line-height: 1.6;
            font-weight: 700;
        }

        .camera-user-pill {
            margin-top: 16px;
            width: fit-content;
            background: rgba(255,255,255,.18);
            border: 1px solid rgba(255,255,255,.35);
            border-radius: 999px;
            padding: 10px 16px;
            font-weight: 900;
            color: white;
        }

        .camera-card {
            background: rgba(255,255,255,.94);
            border: 1px solid #bde4b6;
            border-radius: 26px;
            padding: 24px;
            box-shadow: 0 12px 30px rgba(47,125,50,.14);
        }

        .camera-preview {
            min-height: 290px;
            border-radius: 24px;
            background: linear-gradient(135deg, rgba(37,180,120,.12), rgba(32,178,170,.12));
            border: 2px dashed #7ccc74;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 24px;
        }

        .camera-preview-icon {
            width: 98px;
            height: 98px;
            border-radius: 28px;
            background: linear-gradient(135deg, #42c96f, #1aa6a6);
            color: white;
            font-size: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 12px 28px rgba(26,166,166,.35);
            margin-bottom: 16px;
        }

        .camera-preview h2 {
            color: #113b1b !important;
            font-size: 25px;
            font-weight: 950;
            margin: 0 0 8px;
        }

        .camera-preview p {
            color: #496c42 !important;
            font-size: 15px;
            font-weight: 700;
            line-height: 1.55;
            margin: 0;
        }

        .guide-title {
            font-size: 24px;
            font-weight: 950;
            color: #123f1c !important;
            margin-bottom: 16px;
        }

        .guide-item {
            display: flex;
            gap: 12px;
            align-items: flex-start;
            padding: 14px;
            border-radius: 18px;
            background: #f4fff0;
            border: 1px solid #d5efcb;
            margin-bottom: 12px;
            color: #173d18 !important;
            font-weight: 800;
            line-height: 1.45;
        }

        .guide-icon {
            width: 34px;
            height: 34px;
            flex: 0 0 34px;
            border-radius: 12px;
            background: #dbf7d6;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 900;
        }

        .camera-shortcuts {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            margin-top: 18px;
        }

        .shortcut-box {
            background: white;
            border: 1px solid #cce8c3;
            border-radius: 18px;
            padding: 14px;
            text-align: center;
            color: #123f1c;
            font-weight: 900;
            box-shadow: 0 8px 18px rgba(47,125,50,.08);
        }

        .shortcut-box b {
            display: block;
            color: #1aa06c;
            font-size: 24px;
            margin-bottom: 4px;
        }

        .stButton button {
            height: 58px !important;
            border-radius: 22px !important;
            background: linear-gradient(135deg, #62ce86, #19aaa3) !important;
            color: white !important;
            font-size: 18px !important;
            font-weight: 950 !important;
            border: none !important;
        }

        .status-ok {
            background: #e4ffe1;
            border: 1px solid #a8dd9a;
            color: #14532d;
            border-radius: 18px;
            padding: 14px 16px;
            font-weight: 850;
            margin-top: 14px;
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
            display: grid;
            grid-template-columns: 1fr 1fr 90px 1fr 1fr;
            align-items: center;
            justify-items: center;
            z-index: 9999;
        }

        .swcs-nav-item {
            width: 100%;
            height: 58px;
            text-decoration: none !important;
            color: #4a4a4a !important;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 4px;
            font-size: 13px;
            font-weight: 850;
            white-space: nowrap;
        }

        .swcs-nav-icon {
            font-size: 24px;
        }

        .swcs-scan-btn {
            width: 74px;
            height: 74px;
            border-radius: 50%;
            background: linear-gradient(135deg,#42c96f,#1aa6a6);
            display: flex;
            align-items: center;
            justify-content: center;
            margin-top: -36px;
            border: 5px solid #fff;
            box-shadow: 0 8px 24px rgba(26,166,166,.42);
            text-decoration: none !important;
        }

        .swcs-nav-ai {
            font-size: 32px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_camera_page():
    _load_camera_css()

    user_id = st.session_state.get("user_id", 0)
    user_name = st.session_state.get("user_name", "Guest")

    base_dir = Path(__file__).resolve().parents[5]
    camera_file = base_dir / "SWSC_camera" / "src" / "camera_predict.py"

    st.markdown(
        _clean_html(
            f"""
            <div class="camera-hero">
                <h1>📸 Quét rác thông minh bằng AI</h1>
                <p>Sử dụng camera realtime để nhận diện loại rác, lưu lịch sử phân loại, cộng điểm xanh và hỗ trợ người dùng phân loại rác chính xác hơn.</p>
                <div class="camera-user-pill">👤 Người dùng: {user_name} | ID: {user_id}</div>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

    left_col, right_col = st.columns([1.45, 1])

    with left_col:
        st.markdown(
            _clean_html(
                """
                <div class="camera-card">
                    <div class="camera-preview">
                        <div class="camera-preview-icon">🤖</div>
                        <h2>AI Camera Ready</h2>
                        <p>Nhấn nút bên dưới để mở cửa sổ camera realtime. Hệ thống sẽ tự động phân tích ảnh và dự đoán nhóm rác phù hợp.</p>
                    </div>
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

        if not camera_file.exists():
            st.error(f"Không tìm thấy file camera: {camera_file}")
        else:
            if st.button("🚀 Mở camera realtime", use_container_width=True):
                subprocess.Popen(
                    [
                        sys.executable,
                        str(camera_file),
                        "--user_id",
                        str(user_id),
                        "--user_name",
                        str(user_name),
                    ],
                    cwd=str(base_dir),
                )

                st.markdown(
                    '<div class="status-ok">✅ Đã mở camera. Hãy xem cửa sổ camera bên ngoài Streamlit.</div>',
                    unsafe_allow_html=True,
                )

        st.markdown(
            _clean_html(
                """
                <div class="camera-shortcuts">
                    <div class="shortcut-box"><b>P</b>Cố định vật</div>
                    <div class="shortcut-box"><b>S</b>Lưu database</div>
                    <div class="shortcut-box"><b>Q</b>Thoát camera</div>
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

    with right_col:
        st.markdown(
            _clean_html(
                """
                <div class="camera-card">
                    <div class="guide-title">🌱 Hướng dẫn sử dụng</div>
                    <div class="guide-item"><div class="guide-icon">1️⃣</div><div>Đưa vật cần phân loại vào trước camera, tránh che khuất bằng tay.</div></div>
                    <div class="guide-item"><div class="guide-icon">2️⃣</div><div>Nhấn <b>P</b> để cố định khung vật nếu muốn hệ thống đọc ổn định hơn.</div></div>
                    <div class="guide-item"><div class="guide-icon">3️⃣</div><div>Nhấn <b>S</b> để lưu kết quả vào database và cộng điểm xanh.</div></div>
                    <div class="guide-item"><div class="guide-icon">4️⃣</div><div>Nhấn <b>Q</b> để thoát cửa sổ camera sau khi hoàn tất.</div></div>
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

    st.markdown(_render_bottom_nav(), unsafe_allow_html=True)