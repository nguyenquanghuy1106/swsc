import streamlit as st

from features.home.data.user.post_composer_data import (
    get_post_composer_branding,
    get_post_categories,
    get_right_sidebar_data,
)

from features.home.logic.user.post_composer_service import (
    create_post_data,
    save_draft_data,
)

from shared.styles.user.post_composer_css import load_post_composer_css


def _get_login_user():
    user_id = st.session_state.get("user_id")
    user_name = st.session_state.get("user_name")

    if user_id is not None:
        return user_id, user_name

    try:
        from features.database.connection import get_connection

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT user_id, userName
            FROM current_login
            WHERE id = 1
            """
        )

        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:
            st.session_state["user_id"] = user["user_id"]
            st.session_state["user_name"] = user["userName"]
            return user["user_id"], user["userName"]

    except Exception:
        pass

    return None, None


def _page_url(page):
    user_id, user_name = _get_login_user()

    if user_id and user_name:
        return f"?page={page}&uid={user_id}&uname={user_name}"

    return f"?page={page}"


def _render_bottom_nav() -> str:
    return (
        '<div class="swcs-bottom-nav">'
        f'<a class="swcs-nav-item" href="{_page_url("home")}" target="_top"><span class="swcs-nav-icon">🏠</span><span class="swcs-nav-label">Trang chủ</span></a>'
        f'<a class="swcs-nav-item active" href="{_page_url("post")}" target="_top"><span class="swcs-nav-icon">📚</span><span class="swcs-nav-label">Bài đăng</span></a>'
        f'<a class="swcs-scan-btn" href="{_page_url("ai")}" target="_top"><span class="swcs-nav-ai">🤖</span></a>'
        f'<a class="swcs-nav-item" href="{_page_url("news")}" target="_top"><span class="swcs-nav-icon">📰</span><span class="swcs-nav-label">Tin tức</span></a>'
        f'<a class="swcs-nav-item" href="{_page_url("profile")}" target="_top"><span class="swcs-nav-icon">👤</span><span class="swcs-nav-label">Profile</span></a>'
        "</div>"
    )


def _validate_post(title, content):
    if not title.strip():
        st.error("Vui lòng nhập phụ tiêu đề.")
        return False

    if not content.strip():
        st.error("Vui lòng nhập nội dung bài viết.")
        return False

    return True


def render_post_composer_page():
    load_post_composer_css()

    user_id, user_name = _get_login_user()

    if user_id is None:
        st.error("Bạn cần đăng nhập trước khi đăng bài.")
        if st.button("Đăng nhập ngay"):
            st.query_params["page"] = "login"
            st.rerun()
        return

    branding = get_post_composer_branding()
    categories = get_post_categories()
    sidebar = get_right_sidebar_data()
    category_labels = [item["label"] for item in categories]

    left_col, right_col = st.columns([3.2, 1])

    with left_col:
        st.markdown(
            f"""
            <div class="composer-card-title">
                <div class="composer-title">{branding["title"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.success(f"👤 Đang đăng nhập: {user_name} | ID: {user_id}")

        title = st.text_input(
            branding["subtitle_label"],
            placeholder=branding["subtitle_placeholder"],
            key="post_title",
        )

        category = st.radio(
            "Chọn Chủ đề Phân Loại",
            category_labels,
            horizontal=True,
            key="post_category",
        )

        content = st.text_area(
            "Nội dung bài viết",
            placeholder=branding["content_placeholder"],
            height=170,
            key="post_content",
        )

        uploaded_image = st.file_uploader(
            "Kéo thả hình ảnh hoặc bấm vào đây để tải ảnh",
            type=["jpg", "jpeg", "png", "webp"],
            key="post_image",
        )

        if uploaded_image is not None:
            st.image(uploaded_image, caption="Ảnh đã chọn", use_container_width=True)

        btn1, btn2 = st.columns(2)

        with btn1:
            if st.button(branding["draft_button"], use_container_width=True):
                result = save_draft_data(
                    title=title,
                    category=category,
                    content=content,
                    image=uploaded_image,
                    user_id=user_id,
                )
                st.success(result["message"])

        with btn2:
            if st.button(branding["post_button"], use_container_width=True):
                if _validate_post(title, content):
                    result = create_post_data(
                        title=title,
                        category=category,
                        content=content,
                        image=uploaded_image,
                        user_id=user_id,
                    )
                    st.success(result["message"])
                    st.balloons()

    with right_col:
        hashtag_html = "".join(
            f'<div class="hashtag">{tag}</div>' for tag in sidebar["hashtags"]
        )

        st.markdown(
            f"""
            <div class="sidebar-card challenge-card">
                <h3>{sidebar["challenge"]["title"]}</h3>
                <div>{sidebar["challenge"]["content"]}</div>
            </div>

            <div class="sidebar-card hashtag-card">
                <h3>Popular hashtags</h3>
                {hashtag_html}
            </div>

            <div class="sidebar-card tip-card">
                <h3>{sidebar["tip"]["title"]}</h3>
                <div>{sidebar["tip"]["content"]}</div>
            </div>
            """,
unsafe_allow_html=True,
        )

    st.markdown(_render_bottom_nav(), unsafe_allow_html=True)
