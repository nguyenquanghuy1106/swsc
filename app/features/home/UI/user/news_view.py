import base64
from pathlib import Path
import streamlit as st

from features.home.data.user.post_composer_data import get_right_sidebar_data
from features.home.logic.user.news_service import (
    get_all_posted_news,
    toggle_like,
    add_comment,
    get_comments_by_post,
)
from shared.styles.user.news_css import load_news_css


def _render_bottom_nav() -> str:
    return (
        '<div class="swcs-bottom-nav">'
        '<a class="swcs-nav-item" href="?page=home" target="_top"><span class="swcs-nav-icon">🏠</span><span class="swcs-nav-label">Trang chủ</span></a>'
        '<a class="swcs-nav-item" href="?page=post" target="_top"><span class="swcs-nav-icon">📚</span><span class="swcs-nav-label">Bài đăng</span></a>'
        '<a class="swcs-scan-btn" href="?page=ai" target="_top" title="AI nhận diện"><span class="swcs-nav-ai">🤖</span></a>'
        '<a class="swcs-nav-item active" href="?page=news" target="_top"><span class="swcs-nav-icon">📰</span><span class="swcs-nav-label">Tin tức</span></a>'
        '<a class="swcs-nav-item" href="?page=profile" target="_top"><span class="swcs-nav-icon">👤</span><span class="swcs-nav-label">Profile</span></a>'
        "</div>"
    )


def _get_user_id():
    return st.session_state.get("user_id")


def _category_icon(category):
    return {
        "Rác Hữu Cơ": "🍃",
        "Rác Tái Chế": "♻️",
        "Rác Nguy Hại": "⚠️",
        "Mẹo Sống Xanh": "💡",
    }.get(category, "🌱")


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


def _clean_html(html: str) -> str:
    return "".join(line.strip() for line in html.splitlines() if line.strip())


def _render_comments(post_id):
    comments = get_comments_by_post(post_id)

    st.markdown(
        """
        <div class="comment-panel-title">
            💬 Khu vực bình luận
        </div>
        """,
        unsafe_allow_html=True,
    )

    comment_text = st.text_area(
        "Viết bình luận của bạn",
        placeholder="Nhập bình luận tích cực của bạn tại đây...",
        key=f"comment_input_{post_id}",
        height=80,
        label_visibility="collapsed",
    )

    if st.button("🚀 Gửi bình luận", key=f"send_comment_{post_id}", use_container_width=True):
        if comment_text.strip():
            add_comment(post_id, comment_text.strip(), _get_user_id())
            st.success("Đã gửi bình luận.")
            st.rerun()
        else:
            st.warning("Vui lòng nhập bình luận.")

    if comments:
        for cmt in comments:
            st.markdown(
                _clean_html(
                    f"""
                    <div class="comment-item">
                        <div class="comment-avatar">👤</div>
                        <div class="comment-content-box">
                            <div class="comment-author">{cmt.get("user_name") or "Người dùng"}</div>
                            <div class="comment-text">{cmt["comment_text"]}</div>
                            <div class="comment-time">🕒 {cmt["created_at"]}</div>
                        </div>
                    </div>
                    """
                ),
                unsafe_allow_html=True,
            )
    else:
        st.markdown(
            '<div class="empty-comment">🌱 Chưa có bình luận nào. Hãy là người đầu tiên bình luận!</div>',
            unsafe_allow_html=True,
        )


def _render_post(post):
    post_id = post["id"]
    title = post.get("title") or "Bài viết xanh"
    user_name = post.get("user_name") or "Thành viên SWSC"
    content = post.get("content") or ""
    category = post.get("category") or "Cộng đồng xanh"
    created_at = post.get("created_at") or ""
    like_count = post.get("like_count", 0)
    comment_count = post.get("comment_count", 0)
    liked_by_me = bool(post.get("liked_by_me"))
    img_src = _image_to_base64(post.get("image_path"))

    image_html = ""
    if img_src:
        image_html = f'<div class="news-image-wrap"><img class="news-image" src="{img_src}" /></div>'

    like_label = "💔 Bỏ thích" if liked_by_me else "❤️ Like"

    card_html = f"""
    <div class="news-post-card">
        <div class="post-header">
            <div class="avatar-circle">👤</div>
            <div>
                <div class="author-name">{user_name}</div>
                <div class="post-time">🕒 {created_at}</div>
            </div>
            <div class="post-more">•••</div>
        </div>

        <div class="post-title">{title}</div>
        <div class="post-content">{content}</div>

        <div class="post-category">
            <span>{_category_icon(category)}</span>
            <span>{category}</span>
        </div>

        {image_html}

        <div class="post-stats">
            <span>❤️ {like_count} lượt thích</span>
            <span>💬 {comment_count} bình luận</span>
        </div>
    </div>
    """

    st.markdown(_clean_html(card_html), unsafe_allow_html=True)

    action_col1, action_col2, action_col3 = st.columns([1, 1.2, 2])

    with action_col1:
        if st.button(like_label, key=f"like_{post_id}", use_container_width=True):
            toggle_like(post_id, _get_user_id())
            st.rerun()

    with action_col2:
        show_key = f"show_comment_{post_id}"

        if show_key not in st.session_state:
            st.session_state[show_key] = False

        if st.button("💬 Bình luận", key=f"open_comment_{post_id}", use_container_width=True):
            st.session_state[show_key] = not st.session_state[show_key]

    with action_col3:
        st.markdown(
            '<div class="share-text">🔗 Chia sẻ hành động xanh này với cộng đồng</div>',
            unsafe_allow_html=True,
        )

    if st.session_state.get(f"show_comment_{post_id}"):
        st.markdown('<div class="comment-panel">', unsafe_allow_html=True)
        _render_comments(post_id)
        st.markdown("</div>", unsafe_allow_html=True)


def render_news_page():
    load_news_css()

    sidebar = get_right_sidebar_data()
    user_id = _get_user_id()

    try:
        posts = get_all_posted_news(user_id)
    except Exception as e:
        st.error(f"Lỗi tải bài viết: {e}")
        posts = []

    left_col, right_col = st.columns([3.2, 1])

    with left_col:
        st.markdown(
            _clean_html(
                """
                <div class="news-title-card">
                    <div>
                        <h1>🌿 Cộng Đồng</h1>
                        <p>Community Feed - nơi chia sẻ hành động xanh của mọi người</p>
                    </div>
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

        if not posts:
            st.info("Chưa có bài đăng nào. Hãy sang trang Bài đăng để tạo bài viết đầu tiên.")
        else:
            for post in posts:
                _render_post(post)

    with right_col:
        hashtag_html = "".join(
            f'<div class="hashtag">📌 {tag}</div>' for tag in sidebar["hashtags"]
        )

        st.markdown(
            _clean_html(
                f"""
                <div class="sidebar-card challenge-card">
                    <h3>{sidebar["challenge"]["title"]}</h3>
                    <div>Thử thách hôm nay:</div>
                    <b>Đăng ảnh phân loại rác thải nhựa tích điểm xanh!</b>
                    <div class="progress-bar"><div class="progress-fill"></div></div>
                </div>

                <div class="sidebar-card hashtag-card">
                    <h3>Popular hashtags 🔥</h3>
                    {hashtag_html}
                </div>

                <div class="sidebar-card tip-card">
                    <h3>{sidebar["tip"]["title"]}</h3>
                    <div>{sidebar["tip"]["content"]}</div>
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

    st.markdown(_render_bottom_nav(), unsafe_allow_html=True)