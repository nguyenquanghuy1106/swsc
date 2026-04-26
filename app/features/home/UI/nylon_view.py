import base64
from pathlib import Path

import streamlit as st
from features.home.logic.nylon_service import get_nylon_data


def load_nylon_view_model():
    data = get_nylon_data()
    return {
        "page_title": "Nilon",
        "hero_desc": (
            "Tìm hiểu các loại túi nilon phổ biến, thời gian phân hủy "
            "và tác động xấu đến môi trường."
        ),
        "categories": data["categories"],
        "summary_items": data["summary_items"],
        "environment_notes": data["environment_notes"],
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
    mime_type = mime_map.get(suffix, "image/png")

    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")

    return f"data:{mime_type};base64,{encoded}"


def _get_bar_width(years: str) -> str:
    text = years.lower()

    if "> 1000" in text or "1000 năm" in text:
        return "100%"
    if "100 – 500" in text or "100-500" in text:
        return "60%"
    if "2 – 5 năm" in text or "2-5 năm" in text:
        return "70%"
    if "6 tháng – 1 năm" in text or "6 tháng-1 năm" in text:
        return "78%"
    return "60%"


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
        '  <input type="checkbox" id="nylonSidebarToggle" class="nylon-sidebar-checkbox">'
        '  <label for="nylonSidebarToggle" class="nylon-sidebar-toggle">☰</label>'
        '  <label for="nylonSidebarToggle" class="nylon-sidebar-overlay"></label>'
        '  <div class="nylon-sidebar">'
        '    <div class="nylon-logo">♻ SWCS</div>'
        '    <div class="nylon-menu">'
        '      <div class="nylon-menu-item">🏠 Tổng quan</div>'
        '      <div class="nylon-menu-item">🗂️ Phân loại rác</div>'
        '      <div class="nylon-menu-item">📷 Nhận diện rác</div>'
        '      <div class="nylon-menu-item active">📍 Kiến thức tái chế</div>'
        '      <div class="nylon-menu-item">📊 Thống kê</div>'
        '      <div class="nylon-menu-item">⚙️ Cài đặt</div>'
        '    </div>'
        '  </div>'
        '</div>'
    )
    st.markdown(sidebar_html, unsafe_allow_html=True)


def _render_topbar():
    topbar_html = (
        '<div class="nylon-topbar">'
        '  <div class="nylon-topbar-title">Nilon</div>'
        '  <div class="nylon-topbar-right">'
        '    <div class="nylon-topbar-search-mini">🔍 Tìm kiếm</div>'
        '    <div class="nylon-topbar-icon-wrap">'
        '      <div class="nylon-topbar-badge">3</div>'
        '      <div class="nylon-topbar-icon">🔔</div>'
        '    </div>'
        '    <div class="nylon-topbar-icon-wrap">'
        '      <div class="nylon-topbar-badge">1</div>'
        '      <div class="nylon-topbar-icon">📩</div>'
        '    </div>'
        '    <div class="nylon-topbar-avatar">👨🏻</div>'
        '  </div>'
        '</div>'
    )
    st.markdown(topbar_html, unsafe_allow_html=True)


def _render_search():
    search_html = (
        '<div class="nylon-banner-search">'
        '  <span class="nylon-banner-search-icon">🔍</span>'
        '  <span class="nylon-banner-search-text">'
        '    Tìm nilon, vật liệu, thời gian phân hủy...'
        '  </span>'
        '</div>'
    )
    st.markdown(search_html, unsafe_allow_html=True)


def _render_hero():
    banner_src = _image_to_base64("assets/nylon/nylon_banner.png")

    if banner_src:
        right_html = (
            f'<div class="nylon-hero-right">'
            f'<img src="{banner_src}" class="nylon-hero-banner-image" alt="Nylon banner">'
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
        '  <div class="nylon-hero-left">'
        '    <div class="nylon-hero-big-title">Khám phá các loại Nilon</div>'
        '    <div class="nylon-hero-big-desc">'
        '      Tìm hiểu các loại túi nilon phổ biến, thời gian phân hủy '
        '      và tác động xấu đến môi trường.'
        '    </div>'
        '    <div class="nylon-hero-actions">'
        '      <div class="nylon-hero-btn primary">Tìm hiểu về Ni Lông</div>'
        '      <div class="nylon-hero-btn secondary">Chi tiết</div>'
        '    </div>'
        '  </div>'
        f'  {right_html}'
        '</div>'
    )
    st.markdown(hero_html, unsafe_allow_html=True)


def _render_card(item: dict):
    image_src = _image_to_base64(item.get("image", ""))
    bar_width = _get_bar_width(item.get("years", ""))
    bar_color = _get_bar_color(item.get("bar_class", "bar-green"))

    if image_src:
        media_html = (
            f'<div class="nylon-card-image-wrap">'
            f'<img src="{image_src}" class="nylon-card-image" alt="{item["code"]}">'
            f'</div>'
        )
    else:
        media_html = (
            f'<div class="nylon-card-image-wrap nylon-card-image-fallback">'
            f'<div class="nylon-card-emoji">{item["emoji"]}</div>'
            f'</div>'
        )

    card_html = (
        f'<div class="nylon-card">'
        f'  <div class="nylon-card-head">'
        f'    <div class="nylon-card-title">♻ {item["code"]}</div>'
        f'    <div class="nylon-card-badge">{item["number"]}</div>'
        f'  </div>'
        f'  {media_html}'
        f'  <div class="nylon-card-years">{item["years"]}</div>'
        f'  <div class="nylon-progress">'
        f'    <div class="nylon-progress-fill" '
        f'         style="width:{bar_width}; background:{bar_color};"></div>'
        f'  </div>'
        f'  <div class="nylon-card-desc">{item["description"]}</div>'
        f'  <div class="nylon-card-button-row">'
        f'    <button class="nylon-card-detail-btn" disabled>Chi tiết</button>'
        f'  </div>'
        f'</div>'
    )
    st.markdown(card_html, unsafe_allow_html=True)


def _render_info(title: str, items: list[str]):
    list_html = "".join(f"<li>{x}</li>" for x in items)
    info_html = (
        f'<div class="nylon-info-box">'
        f'  <div class="nylon-info-title">{title}</div>'
        f'  <ul class="nylon-list">{list_html}</ul>'
        f'</div>'
    )
    st.markdown(info_html, unsafe_allow_html=True)


def _render_actions():
    actions_html = (
        '<div class="nylon-action-grid">'
        '  <div class="nylon-action-card">'
        '    <button class="nylon-action-btn red" disabled>🛍️ Tìm hiểu về Nilon</button>'
        '  </div>'
        '  <div class="nylon-action-card">'
        '    <button class="nylon-action-btn green" disabled>♻ Hướng dẫn phân loại</button>'
        '  </div>'
        '  <div class="nylon-action-card">'
        '    <button class="nylon-action-btn blue" disabled>🤖 Nhận diện rác bằng AI</button>'
        '  </div>'
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
            '<div class="nylon-section-title">Các loại nilon phổ biến</div>',
            unsafe_allow_html=True
        )

        row1 = st.columns(2, gap="medium")
        row2 = st.columns(2, gap="medium")

        for i, item in enumerate(vm["categories"]):
            cols = row1 if i < 2 else row2
            col = cols[i % 2]
            with col:
                _render_card(item)

        st.markdown('<div class="nylon-space-16"></div>', unsafe_allow_html=True)

        c1, c2 = st.columns(2, gap="large")
        with c1:
            _render_info("🧬 Tác hại của túi nilon", vm["summary_items"])
        with c2:
            _render_info("🌍 Lưu ý môi trường", vm["environment_notes"])

        st.markdown('<div class="nylon-space-16"></div>', unsafe_allow_html=True)
        _render_actions()