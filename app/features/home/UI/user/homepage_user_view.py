import base64
from pathlib import Path

import streamlit as st

from features.home.logic.user.homepage_user_service import (
    build_feed_message,
    filter_posts_by_keyword,
    get_homepage_user_view_model,
)


def _resolve_image_src(path_or_url: str) -> str:
    if not path_or_url:
        return ""

    if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
        return path_or_url

    base_path = Path.cwd()
    possible_paths = [
        base_path / path_or_url,
        base_path / "app" / path_or_url,
    ]

    for path in possible_paths:
        if path.exists():
            suffix = path.suffix.lower()
            mime_map = {
                ".png": "image/png",
                ".jpg": "image/jpeg",
                ".jpeg": "image/jpeg",
                ".webp": "image/webp",
            }
            mime_type = mime_map.get(suffix, "image/png")
            encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
            return f"data:{mime_type};base64,{encoded}"

    return path_or_url


def _render_navbar(vm: dict):
    nav_items_html = "".join(
        f'<a href="{item["href"]}">{item["label"]}</a>'
        for item in vm["branding"]["nav_items"]
    )

    navbar_html = (
        '<div class="swcs-home-user-nav">'
        '  <div class="swcs-home-user-brand">'
        '    <span class="swcs-home-user-brand-icon">🌿</span>'
        f'    <span>{vm["branding"]["app_name"]}</span>'
        '  </div>'
        f'  <div class="swcs-home-user-links">{nav_items_html}</div>'
        '  <div class="swcs-home-user-search-btn">🔍</div>'
        '</div>'
    )
    st.markdown(navbar_html, unsafe_allow_html=True)


def _render_search_block(vm: dict):
    st.markdown(
        f'<div class="swcs-home-user-title">{vm["branding"]["page_title"]}</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="swcs-home-user-search-card"><div class="swcs-home-user-search-inner">', unsafe_allow_html=True)
    keyword = st.text_input(
        "Tìm kiếm bài viết",
        placeholder=vm["branding"]["search_placeholder"],
        label_visibility="collapsed",
        key="homepage_user_search_keyword",
    )
    st.markdown('</div></div>', unsafe_allow_html=True)
    return keyword


def _render_composer_card(vm: dict):
    profile = vm["profile"]
    avatar_src = _resolve_image_src(profile["avatar_url"])

    composer_html = (
        '<div class="swcs-home-user-composer-card">'
        '  <div class="swcs-home-user-composer-row">'
        '    <div class="swcs-home-user-composer-left">'
        '      <div class="swcs-home-user-avatar">'
        f'        <img src="{avatar_src}" alt="avatar">'
        '      </div>'
        f'      <div class="swcs-home-user-composer-text">{vm["branding"]["composer_placeholder"]}</div>'
        '    </div>'
        '    <div class="swcs-home-user-camera-btn">📷</div>'
        '  </div>'
        '</div>'
    )
    st.markdown(composer_html, unsafe_allow_html=True)


def _render_post_images(images: list[str]) -> str:
    resolved_images = [_resolve_image_src(img) for img in images]

    if not resolved_images:
        return ""

    if len(resolved_images) == 1:
        return (
            '<div class="swcs-post-image-single">'
            f'  <img src="{resolved_images[0]}" alt="post-image">'
            '</div>'
        )

    first_image = resolved_images[0]
    right_top = resolved_images[1] if len(resolved_images) > 1 else resolved_images[0]
    right_bottom = resolved_images[2] if len(resolved_images) > 2 else resolved_images[1]

    return (
        '<div class="swcs-post-images-grid">'
        '  <div class="swcs-post-image-large">'
        f'    <img src="{first_image}" alt="post-image-large">'
        '  </div>'
        '  <div class="swcs-post-image-stack">'
        '    <div class="swcs-post-image-small">'
        f'      <img src="{right_top}" alt="post-image-top">'
        '    </div>'
        '    <div class="swcs-post-image-small">'
        f'      <img src="{right_bottom}" alt="post-image-bottom">'
        '    </div>'
        '  </div>'
        '</div>'
    )


def _render_post_card(post: dict):
    avatar_src = _resolve_image_src(post["author"]["avatar_url"])
    images_html = _render_post_images(post["images"])

    post_html = (
        '<div class="swcs-home-user-post-card">'
        '  <div class="swcs-post-head">'
        '    <div class="swcs-post-author">'
        '      <div class="swcs-post-avatar">'
        f'        <img src="{avatar_src}" alt="avatar">'
        '      </div>'
        '      <div>'
        f'        <div class="swcs-post-name">{post["author"]["name"]}</div>'
        f'        <div class="swcs-post-time">{post["time_text"]}</div>'
        '      </div>'
        '    </div>'
        '    <div class="swcs-post-menu">⋮</div>'
        '  </div>'
        f'  <div class="swcs-post-content">{post["content"]}</div>'
        f'  {images_html}'
        '  <div class="swcs-post-footer">'
        f'    <div class="swcs-post-stat like"><span class="icon">❤</span><span>{post["stats"]["likes"]}</span></div>'
        f'    <div class="swcs-post-stat"><span class="icon">💬</span><span>{post["stats"]["comments"]}</span></div>'
        f'    <div class="swcs-post-stat"><span class="icon">↗</span><span>{post["stats"]["share_label"]}</span></div>'
        '  </div>'
        '</div>'
    )
    st.markdown(post_html, unsafe_allow_html=True)


def _render_camera_fab():
    st.markdown(
        """
        <div class="swcs-camera-fab-wrap">
            <a class="swcs-camera-fab" href="?page=detect" title="Quét camera">
                <div class="swcs-camera-fab-inner">
                    <div class="swcs-camera-fab-core"></div>
                </div>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_homepage_user_page():
    vm = get_homepage_user_view_model()

    _render_navbar(vm)
    keyword = _render_search_block(vm)
    _render_composer_card(vm)

    filtered_posts = filter_posts_by_keyword(vm["posts"], keyword)
    feed_message = build_feed_message(len(filtered_posts), keyword)

    st.markdown(
        f'<div class="swcs-home-user-feed-info">{feed_message}</div>',
        unsafe_allow_html=True,
    )

    for post in filtered_posts:
        _render_post_card(post)

    _render_camera_fab()