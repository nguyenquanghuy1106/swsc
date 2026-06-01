import base64
from pathlib import Path

import streamlit as st
from features.home.logic.medical_service import get_medical_data


def load_medical_view_model():
    data = get_medical_data()
    return {
        "page_title": "Dụng cụ Y Tế",
        "hero_desc": (
            "Tìm hiểu về các dụng cụ y tế phổ biến, thời gian phân hủy "
            "và phân loại đúng cách."
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

    if "450 – 500" in text or "450-500" in text:
        return "58%"
    if "600 – 1000" in text or "600-1000" in text:
        return "82%"
    if "400 – 1000" in text or "400-1000" in text:
        return "75%"
    return "65%"


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
        '<div class="medical-sidebar-wrapper">'
        '  <input type="checkbox" id="medicalSidebarToggle" class="medical-sidebar-checkbox">'
        '  <label for="medicalSidebarToggle" class="medical-sidebar-toggle">☰</label>'
        '  <label for="medicalSidebarToggle" class="medical-sidebar-overlay"></label>'
        '  <div class="medical-sidebar">'
        '    <div class="medical-logo">♻ SWCS</div>'
        '    <div class="medical-menu">'
        '      <div class="medical-menu-item">🏠 Tổng quan</div>'
        '      <div class="medical-menu-item">🗂️ Phân loại rác</div>'
        '      <div class="medical-menu-item">📷 Nhận diện rác</div>'
        '      <div class="medical-menu-item active">🏥 Dụng cụ y tế</div>'
        '      <div class="medical-menu-item">📊 Thống kê</div>'
        '      <div class="medical-menu-item">⚙️ Cài đặt</div>'
        '    </div>'
        '  </div>'
        '</div>'
    )
    st.markdown(sidebar_html, unsafe_allow_html=True)


def _render_topbar():
    topbar_html = (
        '<div class="medical-topbar">'
        '  <div class="medical-topbar-title">Dụng cụ Y Tế</div>'
        '  <div class="medical-topbar-right">'
        '    <div class="medical-topbar-search-mini">🔍 Tìm kiếm</div>'
        '    <div class="medical-topbar-icon-wrap">'
        '      <div class="medical-topbar-badge">5</div>'
        '      <div class="medical-topbar-icon">🔔</div>'
        '    </div>'
        '    <div class="medical-topbar-icon-wrap">'
        '      <div class="medical-topbar-badge">1</div>'
        '      <div class="medical-topbar-icon">📩</div>'
        '    </div>'
        '    <div class="medical-topbar-avatar">👨🏻</div>'
        '  </div>'
        '</div>'
    )
    st.markdown(topbar_html, unsafe_allow_html=True)


def _render_search():
    search_html = (
        '<div class="medical-banner-search">'
        '  <span class="medical-banner-search-icon">🔍</span>'
        '  <span class="medical-banner-search-text">'
        '    Tìm dụng cụ y tế, chất liệu, thời gian phân hủy...'
        '  </span>'
        '</div>'
    )
    st.markdown(search_html, unsafe_allow_html=True)


def _render_hero():
    banner_src = _image_to_base64("assets/medical/medical_banner.png")

    if banner_src:
        right_html = (
            f'<div class="medical-hero-right">'
            f'<img src="{banner_src}" class="medical-hero-banner-image" alt="Medical banner">'
            f'</div>'
        )
    else:
        right_html = (
            '<div class="medical-hero-right">'
            '<div class="medical-hero-banner-missing">Chưa tìm thấy ảnh banner</div>'
            '</div>'
        )

    hero_html = (
        '<div class="medical-hero-banner">'
        '  <div class="medical-hero-left">'
        '    <div class="medical-hero-big-title">Khám phá các Dụng cụ Y Tế</div>'
        '    <div class="medical-hero-big-desc">'
        '      Tìm hiểu về các dụng cụ y tế phổ biến, thời gian phân hủy '
        '      và phân loại đúng cách.'
        '    </div>'
        '    <div class="medical-hero-actions">'
        '      <div class="medical-hero-btn primary">Tìm hiểu về y tế</div>'
        '      <div class="medical-hero-btn secondary">Chi tiết</div>'
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
            f'<div class="medical-card-image-wrap">'
            f'<img src="{image_src}" class="medical-card-image" alt="{item["code"]}">'
            f'</div>'
        )
    else:
        media_html = (
            f'<div class="medical-card-image-wrap medical-card-image-fallback">'
            f'<div class="medical-card-emoji">{item["emoji"]}</div>'
            f'</div>'
        )

    card_html = (
        f'<div class="medical-card">'
        f'  <div class="medical-card-head">'
        f'    <div class="medical-card-title">♻ {item["code"]}</div>'
        f'    <div class="medical-card-badge">{item["number"]}</div>'
        f'  </div>'
        f'  {media_html}'
        f'  <div class="medical-card-years">{item["years"]}</div>'
        f'  <div class="medical-progress">'
        f'    <div class="medical-progress-fill" '
        f'         style="width:{bar_width}; background:{bar_color};"></div>'
        f'  </div>'
        f'  <div class="medical-card-desc">{item["description"]}</div>'
        f'  <div class="medical-card-button-row">'
        f'    <button class="medical-card-detail-btn" disabled>Chi tiết</button>'
        f'  </div>'
        f'</div>'
    )
    st.markdown(card_html, unsafe_allow_html=True)


def _render_info(title: str, items: list[str]):
    list_html = "".join(f"<li>{x}</li>" for x in items)
    info_html = (
        f'<div class="medical-info-box">'
        f'  <div class="medical-info-title">{title}</div>'
        f'  <ul class="medical-list">{list_html}</ul>'
        f'</div>'
    )
    st.markdown(info_html, unsafe_allow_html=True)


def _render_actions():
    actions_html = (
        '<div class="medical-action-grid">'
        '  <div class="medical-action-card">'
        '    <button class="medical-action-btn red" disabled>🩺 Tìm hiểu về y tế</button>'
        '  </div>'
        '  <div class="medical-action-card">'
        '    <button class="medical-action-btn green" disabled>♻ Hướng dẫn phân loại</button>'
        '  </div>'
        '  <div class="medical-action-card">'
        '    <a href="?page=ai_medical" class="medical-action-btn blue medical-ai-link">'
        '      🤖 Nhận diện rác bằng AI'
        '    </a>'
        '  </div>'
        '</div>'
    )
    st.markdown(actions_html, unsafe_allow_html=True)


def render_medical_page():
    vm = load_medical_view_model()

    _render_topbar()

    left, right = st.columns([1, 4], gap="large")

    with left:
        _render_sidebar()

    with right:
        _render_search()
        _render_hero()

        st.markdown(
            '<div class="medical-section-title">Các loại dụng cụ y tế phổ biến</div>',
            unsafe_allow_html=True
        )

        row1 = st.columns(2, gap="medium")
        row2 = st.columns(2, gap="medium")

        for i, item in enumerate(vm["categories"]):
            cols = row1 if i < 2 else row2
            col = cols[i % 2]
            with col:
                _render_card(item)

        st.markdown('<div class="medical-space-16"></div>', unsafe_allow_html=True)

        c1, c2 = st.columns(2, gap="large")
        with c1:
            _render_info("⚠ Lưu ý khi phân loại rác y tế", vm["summary_items"])
        with c2:
            _render_info("🌍 Lưu ý môi trường", vm["environment_notes"])

        st.markdown('<div class="medical-space-16"></div>', unsafe_allow_html=True)
        _render_actions()