import base64
from pathlib import Path
import streamlit as st

from features.home.logic.user.profile_service import (
    get_current_login_user,
    get_user_by_id,
    get_total_score,
    get_user_posts,
    count_user_posts,
    update_password,
)

from shared.styles.user.profile_css import load_profile_css


def _clean_html(html: str) -> str:
    return "".join(line.strip() for line in html.splitlines() if line.strip())


def _image_to_base64(image_path):
    if not image_path:
        return ""

    path = Path(image_path)

    if not path.exists():
        return ""

    suffix = path.suffix.lower().replace(".", "")
    if suffix == "jpg":
        suffix = "jpeg"

    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    return f"data:image/{suffix};base64,{encoded}"


def _page_url(page):
    user_id = st.session_state.get("user_id")
    user_name = st.session_state.get("user_name")

    if user_id and user_name:
        return f"?page={page}&uid={user_id}&uname={user_name}"

    return f"?page={page}"


def _render_bottom_nav():
    return (
        '<div class="swcs-bottom-nav">'
        f'<a class="swcs-nav-item" href="{_page_url("home")}" target="_top"><span class="swcs-nav-icon">🏠</span><span>Trang chủ</span></a>'
        f'<a class="swcs-nav-item" href="{_page_url("post")}" target="_top"><span class="swcs-nav-icon">📚</span><span>Bài đăng</span></a>'
        f'<a class="swcs-scan-btn" href="{_page_url("camera")}" target="_top"><span class="swcs-nav-ai">📸</span></a>'
        f'<a class="swcs-nav-item" href="{_page_url("news")}" target="_top"><span class="swcs-nav-icon">📰</span><span>Tin tức</span></a>'
        f'<a class="swcs-nav-item active" href="{_page_url("profile")}" target="_top"><span class="swcs-nav-icon">👤</span><span>Profile</span></a>'
        "</div>"
    )


def render_profile_page():
    load_profile_css()

    login_user = get_current_login_user()

    if not login_user:
        st.error("Bạn cần đăng nhập để xem hồ sơ.")
        if st.button("Đăng nhập ngay"):
            st.query_params["page"] = "login"
            st.rerun()
        return

    user_id = login_user["user_id"]
    user = get_user_by_id(user_id)
    score_data = get_total_score(user_id)
    post_count = count_user_posts(user_id)
    posts = get_user_posts(user_id)

    left_col, main_col, right_col = st.columns([0.9, 3.2, 1.4])

    with left_col:
        st.markdown(
            _clean_html(
                """
                <div class="profile-menu">
                    <a href="?page=news">📰 Tin Tức</a>
                    <a class="active" href="?page=profile">🍀 Hoạt Động</a>
                    <a href="?page=profile">🏆 Thành Tích</a>
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

    with main_col:
        st.markdown(
            _clean_html(
                f"""
                <div class="profile-hero">
                    <div class="profile-avatar">👤</div>
                    <div>
                        <h2>{user["userName"]}</h2>
                        <p>🌱 Yêu môi trường, đam mê sống xanh</p>
                        <small>ID: {user["id"]} | Phone: {user["phone"]}</small>
                    </div>
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

        st.markdown('<div class="section-title">📝 Bài Viết Của Tôi</div>', unsafe_allow_html=True)

        if not posts:
            st.info("Bạn chưa có bài viết nào.")
        else:
            for post in posts:
                img_src = _image_to_base64(post.get("image_path"))
                img_html = f'<img class="my-post-img" src="{img_src}">' if img_src else ""

                st.markdown(
                    _clean_html(
                        f"""
                        <div class="my-post-card">
                            {img_html}
                            <div class="my-post-info">
                                <h4>{post["title"]}</h4>
                                <p>{post["content"]}</p>
                                <div>
                                    <span>{post["category"]}</span>
                                    <small>🕒 {post["created_at"]} | {post["status"]}</small>
                                </div>
                            </div>
                        </div>
                        """
                    ),
                    unsafe_allow_html=True,
                )

        st.markdown('<div class="section-title">🔐 Đổi Mật Khẩu</div>', unsafe_allow_html=True)

        with st.container():
            st.markdown(
    """
    <div class="password-box">
        <h3 style="
            color:#173d18;
            margin-bottom:15px;
            font-weight:900;
        ">
            🔐 Thay đổi mật khẩu
        </h3>
    </div>
    """,
    unsafe_allow_html=True,
            )

            old_password = st.text_input(
                "Mật khẩu cũ",
                placeholder="Nhập mật khẩu cũ",
                type="password",
                key="old_password",
            )

            new_password = st.text_input(
                "Mật khẩu mới",
                placeholder="Nhập mật khẩu mới",
                type="password",
                key="new_password",
            )

            confirm_password = st.text_input(
                "Nhập lại mật khẩu mới",
                placeholder="Nhập lại mật khẩu mới",
                type="password",
                key="confirm_password",
            )

            if st.button("🔐 Cập nhật mật khẩu", use_container_width=True):
                if not old_password or not new_password or not confirm_password:
                    st.error("Vui lòng nhập đầy đủ thông tin.")
                elif new_password != confirm_password:
                    st.error("Mật khẩu mới nhập lại không khớp.")
                else:
                    result = update_password(user_id, old_password, new_password)

                    if result["success"]:
                        st.success(result["message"])
                    else:
                        st.error(result["message"])

            st.markdown("</div>", unsafe_allow_html=True)

    with right_col:
        st.markdown(
            _clean_html(
                f"""
                <div class="data-card">
                    <h3>Dữ Liệu Người Dùng</h3>
                    <div class="stat-box">⭐ <b>Tổng Điểm Tích Lũy</b><br>{score_data["total_score"]} XP</div>
                    <div class="stat-box">♻️ <b>Rác Đã Phân Loại</b><br>{score_data["total_weight"]} kg</div>
                    <div class="stat-box">📋 <b>Nhiệm Vụ Hoàn Thành</b><br>{score_data["total_scans"]}</div>
                    <div class="stat-box">📝 <b>Bài Đã Đăng</b><br>{post_count["posted_count"]}</div>
                    <div class="stat-box">📌 <b>Bài Nháp</b><br>{post_count["draft_count"]}</div>
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

    st.markdown(_render_bottom_nav(), unsafe_allow_html=True)