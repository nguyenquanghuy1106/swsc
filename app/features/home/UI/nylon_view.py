import base64
from pathlib import Path
from urllib.parse import quote

import streamlit as st
from features.home.logic.nylon_service import get_nylon_data


def _page_url(page):
    user_id = st.session_state.get("user_id")
    user_name = st.session_state.get("user_name")

    if user_id and user_name:
        return f"?page={page}&uid={user_id}&uname={quote(str(user_name))}"

    return f"?page={page}"


def _render_bottom_nav():
    return (
        '<div class="swcs-bottom-nav">'
        f'<a class="swcs-nav-item" href="{_page_url("home")}" target="_top"><span class="swcs-nav-icon">🏠</span><span class="swcs-nav-label">Trang chủ</span></a>'
        f'<a class="swcs-nav-item" href="{_page_url("post")}" target="_top"><span class="swcs-nav-icon">📚</span><span class="swcs-nav-label">Bài đăng</span></a>'
        f'<a class="swcs-scan-btn" href="{_page_url("ai")}" target="_top"><span class="swcs-nav-ai">🤖</span></a>'
        f'<a class="swcs-nav-item" href="{_page_url("news")}" target="_top"><span class="swcs-nav-icon">📰</span><span class="swcs-nav-label">Tin tức</span></a>'
        f'<a class="swcs-nav-item" href="{_page_url("profile")}" target="_top"><span class="swcs-nav-icon">👤</span><span class="swcs-nav-label">Profile</span></a>'
        "</div>"
    )


def load_nylon_view_model():
    data = get_nylon_data()
    return {
        "page_title": "Rác hữu cơ",
        "hero_desc": (
            "Tìm hiểu các loại rác hữu cơ thường gặp, cách phân loại, "
            "tác động đến môi trường và phương pháp xử lý phù hợp."
        ),
        "categories": data["categories"],
        "summary_items": [
            "Rác hữu cơ gồm thức ăn thừa, rau củ quả, lá cây, vỏ trái cây và các chất dễ phân hủy.",
            "Nhóm rác này có thể được ủ thành phân compost để cải tạo đất.",
            "Cần tách riêng rác hữu cơ với nhựa, kim loại, pin và rác nguy hại.",
            "Không nên để rác hữu cơ lẫn dầu mỡ, hóa chất hoặc vật liệu khó phân hủy.",
        ],
        "environment_notes": [
            "Phân loại rác hữu cơ giúp giảm mùi hôi và giảm lượng rác đưa ra bãi chôn lấp.",
            "Ủ rác hữu cơ đúng cách giúp tạo phân bón tự nhiên cho cây trồng.",
            "Tách rác hữu cơ giúp nâng cao hiệu quả tái chế các nhóm rác khác.",
            "Rác hữu cơ nếu xử lý sai có thể gây mùi, thu hút côn trùng và phát sinh khí nhà kính.",
        ],
    }


def _image_to_base64(image_path: str) -> str:
    base_dir = Path(__file__).resolve().parents[4]
    path = base_dir / image_path

    if not path.exists():
        print(f"[IMAGE NOT FOUND] {path}")
        return ""

    suffix = path.suffix.lower()
    mime_map = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }

    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")

    return f"data:{mime_map.get(suffix, 'image/png')};base64,{encoded}"


def _get_bar_width(years: str) -> str:
    text = str(years).lower()

    if "vài ngày" in text or "1 tuần" in text:
        return "25%"
    if "2 tuần" in text or "1 tháng" in text:
        return "40%"
    if "3 tháng" in text or "6 tháng" in text:
        return "60%"

    return "45%"


def _get_bar_color(bar_class: str) -> str:
    mapping = {
        "bar-green": "#6fcf97",
        "bar-yellow": "#f2c94c",
        "bar-orange": "#f2994a",
        "bar-red": "#eb5757",
    }
    return mapping.get(bar_class, "#6fcf97")


def _render_sidebar():
    sidebar_html = (
        '<div class="nylon-sidebar-wrapper">'
        '<input type="checkbox" id="nylonSidebarToggle" class="nylon-sidebar-checkbox">'
        '<label for="nylonSidebarToggle" class="nylon-sidebar-toggle">☰</label>'
        '<label for="nylonSidebarToggle" class="nylon-sidebar-overlay"></label>'
        '<div class="nylon-sidebar">'
        '<div class="nylon-logo">🌱 SWCS</div>'
        '<div class="nylon-menu">'
        '<div class="nylon-menu-item">🏠 Tổng quan</div>'
        '<div class="nylon-menu-item active">🍃 Rác hữu cơ</div>'
        '<div class="nylon-menu-item">📷 Nhận diện rác</div>'
        '<div class="nylon-menu-item">🌿 Ủ phân compost</div>'
        '<div class="nylon-menu-item">📊 Thống kê</div>'
        '<div class="nylon-menu-item">⚙️ Cài đặt</div>'
        '</div></div></div>'
    )
    st.markdown(sidebar_html, unsafe_allow_html=True)


def _render_topbar():
    topbar_html = (
        '<div class="nylon-topbar">'
        '<div class="nylon-topbar-title">Rác hữu cơ</div>'
        '<div class="nylon-topbar-right">'
        '<div class="nylon-topbar-search-mini">🔍 Tìm kiếm</div>'
        '<div class="nylon-topbar-icon-wrap"><div class="nylon-topbar-badge">3</div><div class="nylon-topbar-icon">🔔</div></div>'
        '<div class="nylon-topbar-icon-wrap"><div class="nylon-topbar-badge">1</div><div class="nylon-topbar-icon">📩</div></div>'
        '<div class="nylon-topbar-avatar">👨🏻</div>'
        '</div></div>'
    )
    st.markdown(topbar_html, unsafe_allow_html=True)


def _render_search():
    st.markdown(
        '<div class="nylon-banner-search">'
        '<span class="nylon-banner-search-icon">🔍</span>'
        '<span class="nylon-banner-search-text">Tìm rác hữu cơ, thức ăn thừa, rau củ, cách ủ phân...</span>'
        '</div>',
        unsafe_allow_html=True,
    )


def _render_hero():
    banner_src = _image_to_base64("assets/nylon/nylon_banner.png")

    if banner_src:
        right_html = (
            f'<div class="nylon-hero-right">'
            f'<img src="{banner_src}" class="nylon-hero-banner-image" alt="Organic waste banner">'
            f'</div>'
        )
    else:
        right_html = (
            '<div class="nylon-hero-right">'
            '<div class="nylon-hero-banner-missing">Chưa tìm thấy ảnh banner</div>'
            '</div>'
        )

    hero_html = (
        '<div class="nylon-hero-banner">'
        '<div class="nylon-hero-left">'
        '<div class="nylon-hero-big-title">Khám phá nhóm<br>rác hữu cơ</div>'
        '<div class="nylon-hero-big-desc">'
        'Rác hữu cơ là nhóm rác dễ phân hủy như thức ăn thừa, rau củ quả, lá cây, '
        'vỏ trái cây và có thể xử lý bằng phương pháp ủ phân compost.'
        '</div>'
        '<div class="nylon-hero-actions">'
        '<div class="nylon-hero-btn primary">Tìm hiểu rác hữu cơ</div>'
        '<div class="nylon-hero-btn secondary">Cách ủ phân</div>'
        '</div></div>'
        f'{right_html}'
        '</div>'
    )
    st.markdown(hero_html, unsafe_allow_html=True)


def _render_card(item: dict):
    image_src = _image_to_base64(item.get("image", ""))
    bar_width = _get_bar_width(item.get("years", ""))
    bar_color = _get_bar_color(item.get("bar_class", "bar-green"))

    title = item.get("code", "Rác hữu cơ")
    number = item.get("number", "01")
    years = item.get("years", "Vài ngày đến vài tháng")
    description = item.get("description", "Rác dễ phân hủy, phù hợp để ủ phân hữu cơ.")
    emoji = item.get("emoji", "🍃")

    if image_src:
        media_html = (
            f'<div class="nylon-card-image-wrap">'
            f'<img src="{image_src}" class="nylon-card-image" alt="{title}">'
            f'</div>'
        )
    else:
        media_html = (
            f'<div class="nylon-card-image-wrap nylon-card-image-fallback">'
            f'<div class="nylon-card-emoji">{emoji}</div>'
            f'</div>'
        )

    card_html = (
        f'<div class="nylon-card">'
        f'<div class="nylon-card-head">'
        f'<div class="nylon-card-title">🍃 {title}</div>'
        f'<div class="nylon-card-badge">{number}</div>'
        f'</div>'
        f'{media_html}'
        f'<div class="nylon-card-years">{years}</div>'
        f'<div class="nylon-progress">'
        f'<div class="nylon-progress-fill" style="width:{bar_width}; background:{bar_color};"></div>'
        f'</div>'
        f'<div class="nylon-card-desc">{description}</div>'
        f'<div class="nylon-card-button-row">'
        f'<button class="nylon-card-detail-btn" disabled>Chi tiết</button>'
        f'</div></div>'
    )
    st.markdown(card_html, unsafe_allow_html=True)


def _render_info(title: str, items: list[str]):
    list_html = "".join(f"<li>{x}</li>" for x in items)
    st.markdown(
        f'<div class="nylon-info-box">'
        f'<div class="nylon-info-title">{title}</div>'
        f'<ul class="nylon-list">{list_html}</ul>'
        f'</div>',
        unsafe_allow_html=True,
    )


def _render_actions():
    actions_html = (
        '<div class="nylon-action-grid">'
        '<div class="nylon-action-card">'
        '<button class="nylon-action-btn red" disabled>🍎 Tìm hiểu rác hữu cơ</button>'
        '</div>'
        '<div class="nylon-action-card">'
        '<button class="nylon-action-btn green" disabled>🌱 Hướng dẫn ủ phân</button>'
        '</div>'
        '<div class="nylon-action-card">'
        f'<a href="{_page_url("ai")}" class="nylon-action-btn blue nylon-ai-link">🤖 Nhận diện rác bằng AI</a>'
        '</div>'
        '</div>'
    )
    st.markdown(actions_html, unsafe_allow_html=True)


def render_nylon_page():
    vm = load_nylon_view_model()

    _render_topbar()

    left, right = st.columns([1, 4], gap="large")

    with left:
        _render_sidebar()

    with right:
        _render_search()
        _render_hero()

        st.markdown(
            '<div class="nylon-section-title">Các loại rác hữu cơ phổ biến</div>',
            unsafe_allow_html=True,
        )

        row1 = st.columns(2, gap="medium")
        row2 = st.columns(2, gap="medium")

        for i, item in enumerate(vm["categories"]):
            cols = row1 if i < 2 else row2
            with cols[i % 2]:
                _render_card(item)

        st.markdown('<div class="nylon-space-16"></div>', unsafe_allow_html=True)

        c1, c2 = st.columns(2, gap="large")
        with c1:
            _render_info("🍃 Đặc điểm rác hữu cơ", vm["summary_items"])
        with c2:
            _render_info("🌍 Lưu ý khi xử lý", vm["environment_notes"])

        st.markdown('<div class="nylon-space-16"></div>', unsafe_allow_html=True)
        _render_actions()

    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    st.markdown(_render_bottom_nav(), unsafe_allow_html=True)