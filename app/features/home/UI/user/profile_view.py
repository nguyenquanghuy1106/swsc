import base64
from pathlib import Path
from urllib.parse import quote
import streamlit as st

from features.home.logic.user.profile_service import (
    get_current_login_user,
    get_user_by_id,
    get_total_score,
    get_user_posts,
    count_user_posts,
    update_password,
    hide_post,
    restore_post,
    delete_post,
    logout_current_user,
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
        return f"?page={page}&uid={user_id}&uname={quote(str(user_name))}"

    return f"?page={page}"


def _render_bottom_nav():
    return (
        '<div class="swcs-bottom-nav">'
        f'<a class="swcs-nav-item" href="{_page_url("home")}" target="_top"><span class="swcs-nav-icon">🏠</span><span>Trang chủ</span></a>'
        f'<a class="swcs-nav-item" href="{_page_url("post")}" target="_top"><span class="swcs-nav-icon">📚</span><span>Bài đăng</span></a>'
        f'<a class="swcs-scan-btn" href="{_page_url("camera")}" target="_top"><span class="swcs-nav-ai">🤖</span></a>'
        f'<a class="swcs-nav-item" href="{_page_url("news")}" target="_top"><span class="swcs-nav-icon">📰</span><span>Tin tức</span></a>'
        f'<a class="swcs-nav-item active" href="{_page_url("profile")}" target="_top"><span class="swcs-nav-icon">👤</span><span>Profile</span></a>'
        "</div>"
    )


def _status_label(status):
    labels = {
        "posted": "Đang hiển thị",
        "hidden": "Đã ẩn",
        "draft": "Bản nháp",
        "deleted": "Đã xóa",
    }
    return labels.get(status, status)


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
                f"""
                <div class="profile-menu">
                    <a href="{_page_url("news")}">📰 Tin Tức</a>
                    <a class="active" href="{_page_url("profile")}">🍀 Hoạt Động</a>
                    <a href="{_page_url("profile")}">🏆 Thành Tích</a>
                    <a href="{_page_url("post")}">📝 Đăng Bài</a>
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

        if st.button("🚪 Đăng xuất", use_container_width=True):
            logout_current_user()
            st.session_state.clear()
            st.query_params.clear()
            st.query_params["page"] = "login"
            st.rerun()

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

        st.markdown(
            _clean_html(
                f"""
                <div class="profile-summary-grid">
                    <div class="summary-card">⭐<b>{score_data["total_score"]}</b><span>XP tích lũy</span></div>
                    <div class="summary-card">♻️<b>{score_data["total_scans"]}</b><span>Lần phân loại</span></div>
                    <div class="summary-card">📝<b>{post_count["posted_count"]}</b><span>Bài đang hiện</span></div>
                    <div class="summary-card">🙈<b>{post_count["hidden_count"]}</b><span>Bài đã ẩn</span></div>
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
                post_id = post["id"]
                status = post.get("status")
                img_src = _image_to_base64(post.get("image_path"))
                img_html = f'<img class="my-post-img" src="{img_src}">' if img_src else ""

                st.markdown(
                    _clean_html(
                        f"""
                        <div class="my-post-card">
                            {img_html}
                            <div class="my-post-info">
                                <div class="post-topline">
                                    <h4>{post["title"]}</h4>
                                    <div class="status-pill status-{status}">{_status_label(status)}</div>
                                </div>
                                <p>{post["content"]}</p>
                                <div class="my-post-meta">
                                    <span>{post["category"]}</span>
                                    <small>🕒 {post["created_at"]}</small>
                                </div>
                            </div>
                        </div>
                        """
                    ),
                    unsafe_allow_html=True,
                )

                c1, c2, c3 = st.columns([1, 1, 1])

                with c1:
                    if status == "posted":
                        if st.button("🙈 Ẩn bài", key=f"hide_{post_id}", use_container_width=True):
                            result = hide_post(post_id, user_id)
                            st.success(result["message"])
                            st.rerun()
                    elif status == "hidden":
                        if st.button("👁️ Hiện lại", key=f"restore_{post_id}", use_container_width=True):
                            result = restore_post(post_id, user_id)
                            st.success(result["message"])
                            st.rerun()
                    else:
                        st.button("🙈 Ẩn bài", key=f"hide_disable_{post_id}", disabled=True, use_container_width=True)

                with c2:
                    if st.button("🗑️ Xóa bài", key=f"delete_{post_id}", use_container_width=True):
                        st.session_state[f"confirm_delete_{post_id}"] = True

                with c3:
                    st.markdown(
                        f'<a class="go-news-btn" href="{_page_url("news")}" target="_top">📰 Xem Tin tức</a>',
                        unsafe_allow_html=True,
                    )

                if st.session_state.get(f"confirm_delete_{post_id}"):
                    st.warning("Bạn chắc chắn muốn xóa bài này? Bài sẽ biến mất khỏi Profile và Tin tức.")
                    yes_col, no_col = st.columns(2)

                    with yes_col:
                        if st.button("✅ Xác nhận xóa", key=f"yes_delete_{post_id}", use_container_width=True):
                            result = delete_post(post_id, user_id)
                            st.success(result["message"])
                            st.session_state[f"confirm_delete_{post_id}"] = False
                            st.rerun()

                    with no_col:
                        if st.button("❌ Hủy", key=f"no_delete_{post_id}", use_container_width=True):
                            st.session_state[f"confirm_delete_{post_id}"] = False
                            st.rerun()

        st.markdown('<div class="password-title">🔐 Đổi Mật Khẩu</div>', unsafe_allow_html=True)

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
                    <div class="stat-box">🙈 <b>Bài Đã Ẩn</b><br>{post_count["hidden_count"]}</div>
                    <div class="stat-box">📌 <b>Bài Nháp</b><br>{post_count["draft_count"]}</div>
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

    st.markdown(_render_bottom_nav(), unsafe_allow_html=True)