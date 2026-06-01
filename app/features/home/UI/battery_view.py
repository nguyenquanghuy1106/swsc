import base64
from pathlib import Path

import streamlit as st
from features.home.logic.battery_service import get_battery_data


def load_battery_view_model():
    data = get_battery_data()
    return {
        "page_title": "Phân loại Pin",
        "hero_desc": (
            "Tìm hiểu các loại pin phổ biến, thời gian phân hủy "
            "và mức độ ảnh hưởng đến môi trường."
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

    if "100 – 300" in text or "100-300" in text:
        return "45%"
    if "100 – 500" in text or "100-500" in text:
        return "60%"
    if "500 – 1000" in text or "500-1000" in text:
        return "75%"
    if "400 – 1000" in text or "400-1000" in text:
        return "70%"
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
        '<div class="battery-sidebar-wrapper">'
        '  <input type="checkbox" id="batterySidebarToggle" class="battery-sidebar-checkbox">'
        '  <label for="batterySidebarToggle" class="battery-sidebar-toggle">☰</label>'
        '  <label for="batterySidebarToggle" class="battery-sidebar-overlay"></label>'
        '  <div class="battery-sidebar">'
        '    <div class="battery-logo">♻ SWCS</div>'
        '    <div class="battery-menu">'
        '      <div class="battery-menu-item">🏠 Tổng quan</div>'
        '      <div class="battery-menu-item">🗂️ Phân loại rác</div>'
        '      <div class="battery-menu-item">📷 Nhận diện rác</div>'
        '      <div class="battery-menu-item active">📍 Kiến thức tái chế</div>'
        '      <div class="battery-menu-item">📊 Thống kê</div>'
        '      <div class="battery-menu-item">⚙️ Cài đặt</div>'
        '    </div>'
        '  </div>'
        '</div>'
    )
    st.markdown(sidebar_html, unsafe_allow_html=True)


def _render_topbar():
    topbar_html = (
        '<div class="battery-topbar">'
        '  <div class="battery-topbar-title">Pin</div>'
        '  <div class="battery-topbar-right">'
        '    <div class="battery-topbar-search-mini">🔍 Tìm kiếm</div>'
        '    <div class="battery-topbar-icon-wrap">'
        '      <div class="battery-topbar-badge">3</div>'
        '      <div class="battery-topbar-icon">🔔</div>'
        '    </div>'
        '    <div class="battery-topbar-icon-wrap">'
        '      <div class="battery-topbar-badge">1</div>'
        '      <div class="battery-topbar-icon">📩</div>'
        '    </div>'
        '    <div class="battery-topbar-avatar">👨🏻</div>'
        '  </div>'
        '</div>'
    )
    st.markdown(topbar_html, unsafe_allow_html=True)


def _render_search():
    search_html = (
        '<div class="battery-banner-search">'
        '  <span class="battery-banner-search-icon">🔍</span>'
        '  <span class="battery-banner-search-text">'
        '    Tìm pin, vật liệu, thời gian phân hủy...'
        '  </span>'
        '</div>'
    )
    st.markdown(search_html, unsafe_allow_html=True)


def _render_hero():
    banner_src = _image_to_base64("assets/battery/battery_banner.png")

    if banner_src:
        right_html = (
            f'<div class="battery-hero-right">'
            f'<img src="{banner_src}" class="battery-hero-banner-image" alt="Battery banner">'
            f'</div>'
        )
    else:
        right_html = (
            '<div class="battery-hero-right">'
            '<div class="battery-hero-banner-missing">Chưa tìm thấy ảnh banner</div>'
            '</div>'
        )

    hero_html = (
        '<div class="battery-hero-banner">'
        '  <div class="battery-hero-left">'
        '    <div class="battery-hero-big-title">Khám phá các loại Pin phổ biến</div>'
        '    <div class="battery-hero-big-desc">'
        '      Tìm hiểu các loại pin phổ biến, thời gian phân hủy '
        '      và mức độ ảnh hưởng đến môi trường.'
        '    </div>'
        '    <div class="battery-hero-actions">'
        '      <div class="battery-hero-btn primary">Tìm hiểu về Pin</div>'
        '      <div class="battery-hero-btn secondary">Chi tiết</div>'
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
            f'<div class="battery-card-image-wrap">'
            f'<img src="{image_src}" class="battery-card-image" alt="{item["code"]}">'
            f'</div>'
        )
    else:
        media_html = (
            f'<div class="battery-card-image-wrap battery-card-image-fallback">'
            f'<div class="battery-card-emoji">{item["emoji"]}</div>'
            f'</div>'
        )

    card_html = (
        f'<div class="battery-card">'
        f'  <div class="battery-card-head">'
        f'    <div class="battery-card-title">♻ {item["code"]}</div>'
        f'    <div class="battery-card-badge">{item["number"]}</div>'
        f'  </div>'
        f'  {media_html}'
        f'  <div class="battery-card-years">{item["years"]}</div>'
        f'  <div class="battery-progress">'
        f'    <div class="battery-progress-fill" '
        f'         style="width:{bar_width}; background:{bar_color};"></div>'
        f'  </div>'
        f'  <div class="battery-card-desc">{item["description"]}</div>'
        f'  <div class="battery-card-button-row">'
        f'    <button class="battery-card-detail-btn" disabled>Chi tiết</button>'
        f'  </div>'
        f'</div>'
    )
    st.markdown(card_html, unsafe_allow_html=True)


def _render_info(title: str, items: list[str]):
    list_html = "".join(f"<li>{x}</li>" for x in items)
    info_html = (
        f'<div class="battery-info-box">'
        f'  <div class="battery-info-title">{title}</div>'
        f'  <ul class="battery-list">{list_html}</ul>'
        f'</div>'
    )
    st.markdown(info_html, unsafe_allow_html=True)


def _render_actions():
    actions_html = (
        '<div class="battery-action-grid">'
        '  <div class="battery-action-card">'
        '    <button class="battery-action-btn red" disabled>🔍 Tìm hiểu về Pin</button>'
        '  </div>'
        '  <div class="battery-action-card">'
        '    <button class="battery-action-btn green" disabled>♻ Hướng dẫn phân loại</button>'
        '  </div>'
        '  <div class="battery-action-card">'
        '    <a href="?page=ai_battery" class="battery-action-btn blue battery-ai-link">'
        '      🤖 AI nhận diện'
        '    </a>'
        '  </div>'
        '</div>'
    )
    st.markdown(actions_html, unsafe_allow_html=True)


def render_battery_page():
    vm = load_battery_view_model()

    _render_topbar()

    left, right = st.columns([1, 4], gap="large")

    with left:
        _render_sidebar()

    with right:
        _render_search()
        _render_hero()

        st.markdown(
            '<div class="battery-section-title">Các loại pin phổ biến</div>',
            unsafe_allow_html=True
        )

        row1 = st.columns(2, gap="medium")
        row2 = st.columns(2, gap="medium")

        for i, item in enumerate(vm["categories"]):
            cols = row1 if i < 2 else row2
            col = cols[i % 2]
            with col:
                _render_card(item)

        st.markdown('<div class="battery-space-16"></div>', unsafe_allow_html=True)

        c1, c2 = st.columns(2, gap="large")
        with c1:
            _render_info("📘 Tóm tắt nhanh", vm["summary_items"])
        with c2:
            _render_info("🌍 Lưu ý môi trường", vm["environment_notes"])

        st.markdown('<div class="battery-space-16"></div>', unsafe_allow_html=True)
        _render_actions()