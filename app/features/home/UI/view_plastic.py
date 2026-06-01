import base64
from pathlib import Path

import streamlit as st
from features.home.logic.plastic_service import get_plastic_data


def load_plastic_view_model():
    data = get_plastic_data()
    return {
        "page_title": "Phân loại rác thải nhựa",
        "hero_desc": (
            "Hệ thống hỗ trợ nhận biết vật liệu nhựa, "
            "thời gian phân hủy và định hướng xử lý phù hợp."
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


def _get_bar_gradient(bar_class: str) -> str:
    mapping = {
        "bar-green": "linear-gradient(90deg, #67c26f 0%, #9be15d 100%)",
        "bar-yellow": "linear-gradient(90deg, #f6d365 0%, #fda085 100%)",
        "bar-orange": "linear-gradient(90deg, #f2994a 0%, #f2c94c 100%)",
        "bar-red": "linear-gradient(90deg, #ff6a6a 0%, #ff3d3d 100%)",
    }
    return mapping.get(bar_class, "linear-gradient(90deg, #67c26f 0%, #9be15d 100%)")


def _get_bar_width(years: str) -> str:
    text = years.lower()

    if "1000" in text and "trên" in text:
        return "100%"
    if "600" in text:
        return "78%"
    if "500 – 1000" in text or "500-1000" in text:
        return "72%"
    if "400 – 1000" in text or "400-1000" in text:
        return "76%"
    if "450 – 500" in text or "450-500" in text:
        return "58%"
    if "250 – 500" in text or "250-500" in text:
        return "48%"

    return "60%"


def _render_sidebar():
    sidebar_html = (
        '<div class="plastic-sidebar-wrapper">'
        '  <input type="checkbox" id="plasticSidebarToggle" class="plastic-sidebar-checkbox">'
        '  <label for="plasticSidebarToggle" class="plastic-sidebar-toggle">☰</label>'
        '  <label for="plasticSidebarToggle" class="plastic-sidebar-overlay"></label>'
        '  <div class="plastic-sidebar">'
        '    <div class="plastic-logo">♻ SWCS</div>'
        '    <div class="plastic-menu">'
        '      <div class="plastic-menu-item">🏠 Tổng quan</div>'
        '      <div class="plastic-menu-item active">🗂️ Phân loại rác</div>'
        '      <div class="plastic-menu-item">📷 Nhận diện rác</div>'
        '      <div class="plastic-menu-item">📍 Kiến thức tái chế</div>'
        '      <div class="plastic-menu-item">📊 Thống kê</div>'
        '      <div class="plastic-menu-item">⚙️ Cài đặt</div>'
        '    </div>'
        '  </div>'
        '</div>'
    )
    st.markdown(sidebar_html, unsafe_allow_html=True)


def _render_top_bar():
    topbar_html = (
        '<div class="plastic-topbar">'
        '  <div class="plastic-topbar-title">Phân loại rác thải nhựa</div>'
        '  <div class="plastic-topbar-right">'
        '    <div class="plastic-topbar-search-mini">🔍 Tìm kiếm</div>'
        '    <div class="plastic-topbar-icon-wrap">'
        '      <div class="plastic-topbar-badge">3</div>'
        '      <div class="plastic-topbar-icon">🔔</div>'
        '    </div>'
        '    <div class="plastic-topbar-icon-wrap">'
        '      <div class="plastic-topbar-badge">1</div>'
        '      <div class="plastic-topbar-icon">📩</div>'
        '    </div>'
        '    <div class="plastic-topbar-avatar">👨🏻</div>'
        '  </div>'
        '</div>'
    )
    st.markdown(topbar_html, unsafe_allow_html=True)


def _render_banner_search():
    search_html = (
        '<div class="plastic-banner-search">'
        '  <span class="plastic-banner-search-icon">🔍</span>'
        '  <span class="plastic-banner-search-text">'
        '    Tìm loại rác, vật liệu, thời gian phân hủy...'
        '  </span>'
        '</div>'
    )
    st.markdown(search_html, unsafe_allow_html=True)


def _render_hero():
    hero_image = _image_to_base64("assets/plastic/plastic_banner.png")

    if hero_image:
        right_html = (
            f'<div class="plastic-hero-right">'
            f'<img src="{hero_image}" class="plastic-hero-banner-image" alt="Plastic Banner">'
            f'</div>'
        )
    else:
        right_html = (
            '<div class="plastic-hero-right">'
            '<div class="plastic-hero-banner-missing">Chưa tìm thấy ảnh banner</div>'
            '</div>'
        )

    hero_html = (
        '<div class="plastic-hero-banner">'
        '  <div class="plastic-hero-left">'
        '    <div class="plastic-hero-big-title">'
        '      Khám phá các loại rác<br>thải nhựa phổ biến'
        '    </div>'
        '    <div class="plastic-hero-big-desc">'
        '      Hệ thống hỗ trợ nhận biết vật liệu nhựa,<br>'
        '      thời gian phân hủy và định hướng xử lý phù hợp.'
        '    </div>'
        '    <div class="plastic-hero-actions">'
        '      <div class="plastic-hero-btn primary">Xem danh mục</div>'
        '      <div class="plastic-hero-btn secondary">Tìm hiểu về rác đặc biệt</div>'
        '    </div>'
        '  </div>'
        f'  {right_html}'
        '</div>'
    )

    st.markdown(hero_html, unsafe_allow_html=True)


def _render_card(item: dict):
    image_src = _image_to_base64(item.get("image", ""))
    bar_gradient = _get_bar_gradient(item.get("bar_class", "bar-green"))
    bar_width = _get_bar_width(item.get("years", ""))

    if image_src:
        media_html = (
            f'<div class="plastic-card-image-wrap">'
            f'<img src="{image_src}" class="plastic-card-image" alt="{item["code"]}">'
            f'</div>'
        )
    else:
        media_html = (
            f'<div class="plastic-card-image-wrap plastic-card-image-fallback">'
            f'<div class="plastic-card-emoji">{item["emoji"]}</div>'
            f'</div>'
        )

    card_html = (
        f'<div class="plastic-card">'
        f'  <div class="plastic-card-head">'
        f'    <div class="plastic-card-title">♻ {item["code"]}</div>'
        f'    <div class="plastic-card-badge">{item["number"]}</div>'
        f'  </div>'
        f'  {media_html}'
        f'  <div class="plastic-card-years">{item["years"]}</div>'
        f'  <div class="plastic-progress">'
        f'    <div class="plastic-progress-fill" '
        f'         style="width:{bar_width}; background:{bar_gradient};"></div>'
        f'  </div>'
        f'  <div class="plastic-card-desc">{item["description"]}</div>'
        f'  <div class="plastic-card-button-row">'
        f'    <button class="plastic-card-detail-btn" disabled>Chi tiết</button>'
        f'  </div>'
        f'</div>'
    )

    st.markdown(card_html, unsafe_allow_html=True)


def _render_info_box(title: str, items: list[str]):
    list_html = "".join(f"<li>{x}</li>" for x in items)
    info_html = (
        f'<div class="plastic-info-box">'
        f'  <div class="plastic-info-title">{title}</div>'
        f'  <ul class="plastic-list">{list_html}</ul>'
        f'</div>'
    )
    st.markdown(info_html, unsafe_allow_html=True)


def _render_bottom_actions():
    action_html = (
        '<div class="plastic-action-grid">'
        '  <div class="plastic-action-card">'
        '    <button class="plastic-action-btn red" disabled>🔋 Tìm hiểu về Nhựa</button>'
        '  </div>'

        '  <div class="plastic-action-card">'
        '    <button class="plastic-action-btn green" disabled>♻ Hướng dẫn phân loại</button>'
        '  </div>'

        '  <div class="plastic-action-card">'
        '    <a href="?page=ai" class="plastic-action-btn blue plastic-ai-link">'
        '      🤖 Nhận diện rác bằng AI'
        '    </a>'
        '  </div>'
        '</div>'
    )

    st.markdown(action_html, unsafe_allow_html=True)


def render_plastic_page():
    vm = load_plastic_view_model()

    _render_top_bar()

    left, right = st.columns([1.05, 4.25], gap="large")

    with left:
        _render_sidebar()

    with right:
        _render_banner_search()
        _render_hero()

        st.markdown(
            '<div class="plastic-section-title">Các loại nhựa phổ biến</div>',
            unsafe_allow_html=True
        )

        row1 = st.columns(3, gap="medium")
        row2 = st.columns(3, gap="medium")

        for i, item in enumerate(vm["categories"]):
            cols = row1 if i < 3 else row2
            col = cols[i % 3]
            with col:
                _render_card(item)

        st.markdown('<div class="plastic-space-16"></div>', unsafe_allow_html=True)

        info_left, info_right = st.columns(2, gap="large")

        with info_left:
            _render_info_box("📘 Tóm tắt dễ hiểu", vm["summary_items"])

        with info_right:
            _render_info_box("🌍 Lưu ý môi trường", vm["environment_notes"])

        st.markdown('<div class="plastic-space-16"></div>', unsafe_allow_html=True)

        _render_bottom_actions()

        st.markdown('<div class="plastic-space-16"></div>', unsafe_allow_html=True)

        back_col, _ = st.columns([1.2, 4])
        with back_col:
            if st.button("⬅️ Quay lại trang chủ", use_container_width=True):
                st.query_params["page"] = "home"
                st.rerun()

        st.markdown(
            '<div class="plastic-note"></div>',
            unsafe_allow_html=True
        )