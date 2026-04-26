import base64
from pathlib import Path
from textwrap import dedent

import streamlit as st
from features.home.logic.home_service import get_home_data


def load_home_view_model():
    data = get_home_data()
    return {
        "page_title": "SWCS – Hệ Thống Phân Loại Rác Thải Thông Minh",
        "hero": data["hero"],
        "categories": data["categories"],
        "environment_messages": data["environment_messages"],
        "benefits": data["benefits"],
        "footer": data["footer"],
        "images": data["images"],
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


def _render_sidebar():
    sidebar_html = (
        '<div class="swcs-sidebar-wrapper">'
        '  <input type="checkbox" id="swcsSidebarToggle" class="swcs-sidebar-checkbox">'
        '  <label for="swcsSidebarToggle" class="swcs-sidebar-toggle">☰</label>'
        '  <label for="swcsSidebarToggle" class="swcs-sidebar-overlay"></label>'

        '  <div class="swcs-sidebar">'
        '    <div class="swcs-logo-wrap">'
        '      <div class="swcs-logo-icon">♻</div>'
        '      <div class="swcs-logo-text">SWCS</div>'
        '    </div>'

        '    <div class="swcs-menu">'
        '      <a class="swcs-menu-item" href="?page=home">'
        '        <span>⦿</span>'
        '        <span>Tổng quan</span>'
        '      </a>'

        '      <a class="swcs-menu-item active" href="?page=home">'
        '        <span>🗂</span>'
        '        <span>Phân loại rác</span>'
        '      </a>'

        '      <a class="swcs-menu-item" href="?page=detect">'
        '        <span>⌲</span>'
        '        <span>Nhận diện rác</span>'
        '      </a>'

        '      <a class="swcs-menu-item" href="?page=recycle">'
        '        <span>⌘</span>'
        '        <span>Kiến thức tái chế</span>'
        '      </a>'

        '      <a class="swcs-menu-item" href="?page=stats">'
        '        <span>📈</span>'
        '        <span>Thống kê</span>'
        '      </a>'

        '      <a class="swcs-menu-item" href="?page=settings">'
        '        <span>⚙</span>'
        '        <span>Cài đặt</span>'
        '      </a>'
        '    </div>'

        '    <div class="swcs-sidebar-bottom">'
        '      <div class="swcs-bottom-icon">♻</div>'
        '      <div class="swcs-bottom-icon">👥</div>'
        '      <div class="swcs-bottom-icon">⚙</div>'
        '    </div>'
        '  </div>'
        '</div>'
    )
    st.markdown(sidebar_html, unsafe_allow_html=True)


def _render_topbar(vm: dict):
    avatar_path = vm["images"]["avatar"]
    avatar_src = _image_to_base64(avatar_path)

    avatar_html = (
        f'<img src="{avatar_src}" class="swcs-avatar-img" alt="avatar">'
        if avatar_src
        else '<div class="swcs-avatar-fallback">👤</div>'
    )

    topbar_html = (
        '<div class="swcs-topbar">'
        f'  <div class="swcs-topbar-title">{vm["page_title"]}</div>'
        '  <div class="swcs-topbar-right">'
        '    <div class="swcs-search-box">'
        '      <span class="swcs-search-icon">🔍</span>'
        '      <span class="swcs-search-text">Tìm kiếm...</span>'
        '    </div>'
        '    <div class="swcs-noti-wrap">'
        '      <div class="swcs-noti-badge">1</div>'
        '      <div class="swcs-noti-icon">🔔</div>'
        '    </div>'
        f'    <div class="swcs-avatar-wrap">{avatar_html}</div>'
        '  </div>'
        '</div>'
    )
    st.markdown(topbar_html, unsafe_allow_html=True)


def _render_hero(hero: dict):
    hero_src = _image_to_base64(hero["image"])

    hero_html = (
        f'<div class="swcs-hero" style="background-image: url(\'{hero_src}\');">'
        '  <div class="swcs-hero-overlay">'
        '    <div class="swcs-hero-content">'
        f'      <div class="swcs-hero-title">{hero["title_line_1"]}<br><span>{hero["title_line_2"]}</span></div>'
        f'      <div class="swcs-hero-sub">{hero["subtitle"]}</div>'
        f'      <a class="swcs-hero-btn" href="{hero["button_href"]}">{hero["button_text"]}</a>'
        '    </div>'
        '  </div>'
        '</div>'
    )
    st.markdown(hero_html, unsafe_allow_html=True)


def _render_category_card(item: dict):
    image_src = _image_to_base64(item["image"])

    image_html = (
        f'<img src="{image_src}" class="swcs-category-img" alt="{item["title"]}">'
        if image_src
        else '<div class="swcs-category-img-fallback">♻</div>'
    )

    card_html = dedent(f"""
    <a class="swcs-category-card" href="{item["href"]}">
        <div class="swcs-category-image-wrap">{image_html}</div>
        <div class="swcs-category-title">{item["title"]}</div>
        <div class="swcs-category-bar">
            <div class="swcs-category-bar-fill {item["bar_class"]}"></div>
        </div>
        <div class="swcs-category-years">{item["years"]}</div>
    </a>
    """).strip()
    st.markdown(card_html, unsafe_allow_html=True)


def _render_categories(categories: list[dict]):
    st.markdown(
        '<div class="swcs-section-title">Khám phá các loại rác ngay</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(4, gap="medium")
    for col, item in zip(cols, categories):
        with col:
            _render_category_card(item)


def _render_info_box(title: str, items: list[str], bg_path: str):
    bg_src = _image_to_base64(bg_path)
    items_html = "".join(f"<li>{item}</li>" for item in items)

    box_html = dedent(f"""
    <div class="swcs-info-box" style="background-image: url('{bg_src}');">
        <div class="swcs-info-overlay">
            <div class="swcs-info-title">{title}</div>
            <ul class="swcs-info-list">{items_html}</ul>
        </div>
    </div>
    """).strip()
    st.markdown(box_html, unsafe_allow_html=True)


def _render_footer(footer: dict):
    links_html = " <span>|</span> ".join(f"<span>{x}</span>" for x in footer["links"])

    footer_html = dedent(f"""
    <div class="swcs-footer">
        <div class="swcs-footer-title">{footer["title"]}</div>
        <div class="swcs-footer-sub">{footer["subtitle"]}</div>
        <div class="swcs-footer-bottom">
            <div>{footer["copyright"]}</div>
            <div class="swcs-footer-links">{links_html}</div>
        </div>
    </div>
    """).strip()
    st.markdown(footer_html, unsafe_allow_html=True)


def render_home_page():
    vm = load_home_view_model()

    _render_topbar(vm)

    left, right = st.columns([1.1, 4.4], gap="large")

    with left:
        _render_sidebar()

    with right:
        _render_hero(vm["hero"])
        _render_categories(vm["categories"])

        st.markdown('<div style="height:20px"></div>', unsafe_allow_html=True)

        c1, c2 = st.columns(2, gap="large")
        with c1:
            _render_info_box(
                "Thông điệp môi trường",
                vm["environment_messages"],
                vm["images"]["left_info_bg"],
            )
        with c2:
            _render_info_box(
                "Lợi ích phân loại rác",
                vm["benefits"],
                vm["images"]["right_info_bg"],
            )

        st.markdown('<div style="height:20px"></div>', unsafe_allow_html=True)
        _render_footer(vm["footer"])