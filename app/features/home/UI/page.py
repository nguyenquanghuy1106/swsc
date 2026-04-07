import streamlit as st
import base64
from pathlib import Path
from ..logic.service import load_home_view_model
from ....shared.components.header import render_top_icons
from ....shared.components.bottom_nav import render_bottom_nav


def _to_data_uri(image_path: str) -> str:
    project_root = Path(__file__).resolve().parents[4]
    full_path = (project_root / image_path).resolve()

    if not full_path.exists():
        return ""

    suffix = full_path.suffix.lower()
    mime = "image/png" if suffix == ".png" else "image/jpeg"
    encoded = base64.b64encode(full_path.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{encoded}"


def render_home_page():
    vm = load_home_view_model()


    render_top_icons()

    profile_left, profile_right = st.columns([3, 2])

    with profile_left:
        avatar_col, name_col = st.columns([1, 2.5])
        with avatar_col:
            st.image("assets/images/avatar.png", width=64)
        with name_col:
            st.markdown(
                f'<div class="user-name" style="margin-top:14px;">Hi, {vm["user_name"]}</div>',
                unsafe_allow_html=True
            )

    with profile_right:
        st.markdown(
            f'<div style="display:flex;justify-content:flex-end;margin-top:12px;"><div class="point-badge">🎁 {vm["points_text"]}</div></div>',
            unsafe_allow_html=True
        )

    hero_top = _to_data_uri(vm["hero_images"][0])
    hero_middle = _to_data_uri(vm["hero_images"][1])
    hero_bottom = _to_data_uri(vm["hero_images"][2])

    st.markdown(
        f"""
        <div class="hero-layout">
            <div class="hero-left-content">
                <div class="hero-title">
                    {vm["hero_title_line_1"]}<br>
                    {vm["hero_title_line_3"]}, <span class="green-text">Xanh mãi</span><br>
                    ngày mai
                </div>
                <div class="hero-sub">{vm["hero_subtitle"]}</div>
                <a class="main-btn" href="#">Bắt đầu hành trình</a>
            </div>
            <div class="hero-right-stack">
                <img class="hero-card hero-card-top" src="{hero_top}" />
                <img class="hero-card hero-card-middle" src="{hero_middle}" />
                <img class="hero-card hero-card-bottom" src="{hero_bottom}" />
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("""
    <div class="section-title-row">
        <div class="section-title">Rác Cần Phân Loại</div>
        <div class="see-all">Tất cả</div>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(4)
    for col, item in zip(cols, vm["categories"]):
        with col:
            image_data_uri = _to_data_uri(item["image"])
            st.markdown(
                f"""
                <div class="category-card">
                    <div class="category-circle" style="background:{item['bg']};">
                        <img src="{image_data_uri}" style="width:42px;height:42px;object-fit:contain;display:block;" />
                    </div>
                    <div class="category-name">{item['name']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown('<div class="promo-banner">', unsafe_allow_html=True)
    st.image(vm["banner_image"], use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br><h3>Hoạt động nổi bật</h3>", unsafe_allow_html=True)
    st.write("Sau này bạn có thể thêm mục kiến thức, bài đăng, thống kê ở đây.")

    render_bottom_nav()
    st.markdown('</div>', unsafe_allow_html=True)