import base64
from pathlib import Path
from textwrap import dedent
from urllib.parse import quote, unquote

import streamlit as st

from features.home.logic.home_service import get_home_data
from features.home.logic.AI.ai_history_service import get_user_total_score


def _restore_user_from_query():
    uid = st.query_params.get("uid")
    uname = st.query_params.get("uname")

    if isinstance(uid, list):
        uid = uid[0]

    if isinstance(uname, list):
        uname = uname[0]

    if uid:
        st.session_state["user_id"] = int(uid)
        st.session_state["is_login"] = True

    if uname:
        st.session_state["user_name"] = unquote(str(uname))
        st.session_state["is_login"] = True


def _auth_query():
    user_id = st.session_state.get("user_id")
    user_name = st.session_state.get("user_name")

    if user_id and user_name:
        return f"&uid={user_id}&uname={quote(str(user_name))}"

    return ""


def _page_link(page):
    return f"?page={page}{_auth_query()}"


def load_home_view_model():
    _restore_user_from_query()

    data = get_home_data()

    user_id = st.session_state.get("user_id")
    user_name = st.session_state.get("user_name", "Healing")

    total_score = get_user_total_score(user_id) if user_id else 0
    st.session_state["total_score"] = total_score

    return {
        "page_title": "SWCS",
        "user_name": user_name,
        "points": f"{total_score} Point",
        "hero": data["hero"],
        "categories": data["categories"],
        "environment_messages": data["environment_messages"],
        "benefits": data["benefits"],
        "footer": data["footer"],
        "images": data["images"],
    }


def _image_to_base64(image_path):
    if not image_path:
        return ""

    base_dir = Path(__file__).resolve().parents[4]
    path = base_dir / image_path

    if not path.exists():
        print(f"[IMAGE NOT FOUND] {path}")
        return ""

    mime_map = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
        ".svg": "image/svg+xml",
    }

    mime_type = mime_map.get(path.suffix.lower(), "image/png")

    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")

    return f"data:{mime_type};base64,{encoded}"


def _safe_image(path, css_class, alt=""):
    src = _image_to_base64(path)

    if src:
        return f'<img src="{src}" class="{css_class}" alt="{alt}">'

    return '<div class="swcs-img-fallback">♻</div>'


def _category_icon_by_code(code):
    code = str(code).lower().strip()

    icons = {
        "plastic": "♻️",
        "nylon": "🍃",
        "battery": "☣️",
        "medical": "🗑️",
    }

    return icons.get(code, "♻️")


def _category_color_class(index):
    colors = ["yellow", "blue", "pink", "green"]
    return colors[index % len(colors)]


def _fix_href(href):
    href = str(href or "?page=home")
    page = href.replace("?page=", "").split("&")[0]

    return _page_link(page or "home")


def _render_categories(categories):
    html = ""

    for index, item in enumerate(categories[:4]):
        title = item.get("title", "Loại rác")
        href = _fix_href(item.get("href", "?page=home"))
        code = item.get("code", "")

        icon = item.get("icon", "") or _category_icon_by_code(code)
        color_class = _category_color_class(index)

        html += f"""
        <a href="{href}" target="_top" class="swcs-web-category">
            <div class="swcs-category-circle {color_class}">
                <span>{icon}</span>
            </div>
            <div class="swcs-web-category-name">{title}</div>
        </a>
        """

    return html


def _render_bottom_nav() -> str:
    return f"""
    <div class="swcs-bottom-nav">

        <a class="swcs-nav-item active" href="{_page_link("home")}" target="_top">
            <span class="swcs-nav-icon">🏠</span>
            <span class="swcs-nav-label">Trang chủ</span>
        </a>

        <a class="swcs-nav-item" href="{_page_link("post")}" target="_top">
            <span class="swcs-nav-icon">📚</span>
            <span class="swcs-nav-label">Bài đăng</span>
        </a>

        <a class="swcs-scan-btn" href="{_page_link("camera")}" target="_top" title="Quét camera">
            <span class="swcs-nav-ai">🤖</span>
        </a>

        <a class="swcs-nav-item" href="{_page_link("news")}" target="_top">
            <span class="swcs-nav-icon">📰</span>
            <span class="swcs-nav-label">Tin tức</span>
        </a>

        <a class="swcs-nav-item" href="{_page_link("profile")}" target="_top">
            <span class="swcs-nav-icon">👤</span>
            <span class="swcs-nav-label">Profile</span>
        </a>

    </div>
    """


def _render_home_html(vm):
    avatar_src = _image_to_base64(vm["images"].get("avatar", ""))

    avatar_html = (
        f'<img src="{avatar_src}" class="swcs-user-avatar" alt="avatar">'
        if avatar_src
        else '<div class="swcs-user-avatar fallback">♻</div>'
    )

    hero_img = _image_to_base64(vm["hero"].get("image", ""))
    banner_bg = _image_to_base64(vm["images"].get("left_info_bg", "")) or hero_img

    categories = vm.get("categories", [])
    categories_html = _render_categories(categories)

    img_1 = categories[0].get("image", "") if len(categories) > 0 else vm["hero"].get("image", "")
    img_2 = categories[1].get("image", "") if len(categories) > 1 else vm["hero"].get("image", "")
    img_3 = categories[2].get("image", "") if len(categories) > 2 else vm["hero"].get("image", "")

    collage_1 = _safe_image(img_1, "swcs-collage-img", "collage")
    collage_2 = _safe_image(img_2, "swcs-collage-img", "collage")
    collage_3 = _safe_image(img_3, "swcs-collage-img", "collage")

    hero_subtitle = vm["hero"].get(
        "subtitle",
"Phân loại rác – thói quen của người văn minh",
    )

    hero_button_text = vm["hero"].get("button_text", "Bắt đầu hành trình")
    hero_button_href = _fix_href(vm["hero"].get("button_href", "?page=plastic"))

    html = f"""
    <div class="swcs-page-bg">
        <section class="swcs-home-web-card">

            <div class="swcs-home-top">
                <a href="{_page_link("home")}" target="_top" class="swcs-menu-btn">☰</a>

                <div class="swcs-top-right">
                    <a href="{_page_link("home")}" target="_top" class="swcs-bell">
                        <span class="swcs-bell-dot"></span>
                        🔔
                    </a>

                    <div class="swcs-point-pill">
                        <span class="swcs-gift">🎁</span>
                        <span>{vm["points"]}</span>
                    </div>
                </div>
            </div>

            <div class="swcs-user-row">
                <div class="swcs-user-left">
                    {avatar_html}
                    <div>
                        <div class="swcs-hi">Hi, <b>{vm["user_name"]}</b></div>
                        <div class="swcs-user-sub">Cùng phân loại rác thông minh hôm nay</div>
                    </div>
                </div>
            </div>

            <div class="swcs-hero-web">
                <div class="swcs-hero-text">
                    <div class="swcs-hero-badge">Smart Waste Classification System</div>

                    <h1>
                        Phân loại hôm<br>
                        nay, <span>Xanh mãi</span><br>
                        ngày mai
                    </h1>

                    <p>{hero_subtitle}</p>

                    <div class="swcs-hero-actions">
                        <a href="{hero_button_href}" target="_top" class="swcs-start-btn">
                            {hero_button_text}
                        </a>

                        <a href="{_page_link("ai")}" target="_top" class="swcs-outline-btn">
                            Phân Loại Rác Ngay
                        </a>
                    </div>
                </div>

                <div class="swcs-hero-visual">
                    <div class="swcs-blob one"></div>
                    <div class="swcs-blob two"></div>
                    <div class="swcs-blob three"></div>

                    <div class="swcs-collage big">{collage_1}</div>
                    <div class="swcs-collage small top">{collage_2}</div>
                    <div class="swcs-collage small bottom">{collage_3}</div>
                </div>
            </div>

            <div class="swcs-section-head">
                <div class="swcs-section-title">Rác Cần Phân Loại</div>
                <a href="{_page_link("plastic")}" target="_top" class="swcs-section-link">Tất cả</a>
            </div>

            <div class="swcs-category-grid">
{categories_html}
            </div>

            <a href="{_page_link("home")}" target="_top" class="swcs-banner-card" style="background-image: url('{banner_bg}');">
                <div class="swcs-banner-overlay">
                    <div class="swcs-banner-brand">Healing</div>
                    <div class="swcs-banner-title">Bảo vệ môi trường · Kiến tạo tương lai</div>
                </div>
            </a>

            <div class="swcs-slider-dots">
                <span class="active"></span>
                <span></span>
                <span></span>
            </div>

            <div class="swcs-info-row">
                <div class="swcs-info-card">
                    <div class="swcs-info-icon">♻️</div>
                    <div>
                        <h3>Phân loại chính xác</h3>
                        <p>Nhận biết từng nhóm rác và xử lý đúng cách.</p>
                    </div>
                </div>

                <div class="swcs-info-card">
                    <div class="swcs-info-icon">🌱</div>
                    <div>
                        <h3>Sống xanh mỗi ngày</h3>
                        <p>Xây dựng thói quen bảo vệ môi trường bền vững.</p>
                    </div>
                </div>

                <div class="swcs-info-card">
                    <div class="swcs-info-icon">🎁</div>
                    <div>
                        <h3>Tích điểm đổi quà</h3>
                        <p>Hoàn thành nhiệm vụ xanh để nhận điểm thưởng.</p>
                    </div>
                </div>
            </div>

            <div class="swcs-bottom-space"></div>

            <a href="{_page_link("home")}" target="_top" class="swcs-floating-recycle">♻</a>

            {_render_bottom_nav()}
        </section>
    </div>
    """

    return dedent(html).strip()


def render_home_page():
    vm = load_home_view_model()
    html = _render_home_html(vm)

    if hasattr(st, "html"):
        st.html(html)
    else:
        st.components.v1.html(html, height=1200, scrolling=True)