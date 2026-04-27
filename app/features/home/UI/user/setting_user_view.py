import streamlit as st

from features.home.logic.user.setting_user_service import (
    build_setting_action_message,
    get_setting_user_view_model,
    handle_theme_toggle,
    initialize_setting_state,
)


def _render_navbar(vm: dict):
    nav_items_html = "".join(
        f'<a href="{item["href"]}">{item["label"]}</a>'
        for item in vm["branding"]["nav_items"]
    )

    navbar_html = (
        '<div class="swcs-setting-nav">'
        '  <div class="swcs-setting-brand">'
        '    <span class="swcs-setting-brand-icon">🌿</span>'
        f'    <span>{vm["branding"]["app_name"]}</span>'
        '  </div>'
        f'  <div class="swcs-setting-links">{nav_items_html}</div>'
        f'  <div class="swcs-setting-search">{vm["branding"]["search_icon"]}</div>'
        '</div>'
    )
    st.markdown(navbar_html, unsafe_allow_html=True)


def _render_message():
    message = st.session_state.get("setting_user_message", "")
    message_type = st.session_state.get("setting_user_message_type", "")

    if not message:
        return

    css_class = "swcs-setting-success" if message_type == "success" else "swcs-setting-info"
    st.markdown(
        f'<div class="swcs-setting-message {css_class}">{message}</div>',
        unsafe_allow_html=True,
    )


def _ensure_setting_state():
    defaults = initialize_setting_state()
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def _render_profile_card(vm: dict):
    profile = vm["profile"]
    html = (
        '<div class="swcs-setting-card">'
        '  <div class="swcs-setting-profile-head">'
        '    <div class="swcs-setting-profile-left">'
        '      <div class="swcs-setting-avatar">'
        f'        <img src="{profile["avatar_url"]}" alt="avatar">'
        '      </div>'
        '      <div>'
        f'        <div class="swcs-setting-title">{vm["branding"]["page_title"]}</div>'
        f'        <div class="swcs-setting-email">{profile["email"]}</div>'
        '      </div>'
        '    </div>'
        '    <div class="swcs-setting-gear">⚙️</div>'
        '  </div>'
        '</div>'
    )
    st.markdown(html, unsafe_allow_html=True)


def _render_theme_block(vm: dict):
    items = vm["theme_items"]


    row1_col1, row1_col2 = st.columns([8, 2], gap="small")
    with row1_col1:
        st.markdown(
            (
                '<div class="swcs-setting-row">'
                '  <div class="swcs-setting-row-left">'
                '    <div class="swcs-setting-row-icon theme-dark">✳️</div>'
                '    <div>'
                f'      <div class="swcs-setting-row-title">{items[0]["title"]}</div>'
                f'      <div class="swcs-setting-row-subtitle">{items[0]["subtitle"]}</div>'
                '    </div>'
                '  </div>'
                '</div>'
            ),
            unsafe_allow_html=True,
        )
    with row1_col2:
        dark_mode = st.toggle(
            "",
            value=st.session_state["dark_mode"],
            key="dark_mode_toggle",
            label_visibility="collapsed",
        )

    st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)

    row2_col1, row2_col2 = st.columns([8, 2], gap="small")
    with row2_col1:
        st.markdown(
            (
                '<div class="swcs-setting-row">'
                '  <div class="swcs-setting-row-left">'
                '    <div class="swcs-setting-row-icon theme-light">☀️</div>'
                '    <div>'
                f'      <div class="swcs-setting-row-title">{items[1]["title"]}</div>'
                f'      <div class="swcs-setting-row-subtitle">{items[1]["subtitle"]}</div>'
                '    </div>'
                '  </div>'
                '</div>'
            ),
            unsafe_allow_html=True,
        )
    with row2_col2:
        light_mode = st.toggle(
            "",
            value=st.session_state["light_mode"],
            key="light_mode_toggle",
            label_visibility="collapsed",
        )

    new_dark, new_light = handle_theme_toggle(
        changed_key="light_mode" if light_mode != st.session_state["light_mode"] else "dark_mode",
        dark_mode=dark_mode,
        light_mode=light_mode,
    )
    st.session_state["dark_mode"] = new_dark
    st.session_state["light_mode"] = new_light

    st.markdown('</div></div>', unsafe_allow_html=True)


def _render_notification_block(vm: dict):
    items = vm["notification_items"]

    st.markdown('<div class="swcs-setting-card"><div class="swcs-setting-item-card">', unsafe_allow_html=True)

    row1_col1, row1_col2 = st.columns([8, 2], gap="small")
    with row1_col1:
        st.markdown(
            (
                '<div class="swcs-setting-row">'
                '  <div class="swcs-setting-row-left">'
                '    <div class="swcs-setting-row-icon sound">🔊</div>'
                '    <div>'
                f'      <div class="swcs-setting-row-title">{items[0]["title"]}</div>'
                f'      <div class="swcs-setting-row-subtitle">{items[0]["subtitle"]}</div>'
                '    </div>'
                '  </div>'
                '</div>'
            ),
            unsafe_allow_html=True,
        )
    with row1_col2:
        if st.button("›", key="sound_vibration_btn", use_container_width=True):
            st.session_state["setting_user_message"] = build_setting_action_message("sound_vibration")
            st.session_state["setting_user_message_type"] = "info"
            st.rerun()

    row2_col1, row2_col2 = st.columns([8, 2], gap="small")
    with row2_col1:
        st.markdown(
            (
                '<div class="swcs-setting-row">'
                '  <div class="swcs-setting-row-left">'
                '    <div class="swcs-setting-row-icon notice">📄</div>'
                '    <div>'
                f'      <div class="swcs-setting-row-title">{items[1]["title"]}</div>'
                f'      <div class="swcs-setting-row-subtitle">{items[1]["subtitle"]}</div>'
                '    </div>'
                '  </div>'
                '</div>'
            ),
            unsafe_allow_html=True,
        )
    with row2_col2:
        if st.button("›", key="notification_status_btn", use_container_width=True):
            st.session_state["setting_user_message"] = build_setting_action_message("notification_status")
            st.session_state["setting_user_message_type"] = "info"
            st.rerun()

    st.markdown('</div></div>', unsafe_allow_html=True)


def _render_account_block(vm: dict):
    items = vm["account_items"]

    st.markdown('<div class="swcs-setting-card"><div class="swcs-setting-item-card">', unsafe_allow_html=True)

    for item in items:
        left, right = st.columns([8, 2], gap="small")
        with left:
            st.markdown(
                (
                    '<div class="swcs-setting-row">'
                    '  <div class="swcs-setting-row-left">'
                    '    <div class="swcs-setting-row-icon account">'
                    f'      {item["icon"]}'
                    '    </div>'
                    '    <div>'
                    f'      <div class="swcs-setting-row-title">{item["title"]}</div>'
                    '    </div>'
                    '  </div>'
                    '</div>'
                ),
                unsafe_allow_html=True,
            )
        with right:
            if item["key"] != "pin_setup":
                if st.button("›", key=f'{item["key"]}_btn', use_container_width=True):
                    st.session_state["setting_user_message"] = build_setting_action_message(item["key"])
                    st.session_state["setting_user_message_type"] = "info"
                    st.rerun()

    logout_col = st.columns([3, 5])[0]
    with logout_col:
        if st.button("⏻  Đăng xuất", key="logout_btn", use_container_width=True):
            st.session_state["setting_user_message"] = build_setting_action_message("logout")
            st.session_state["setting_user_message_type"] = "success"
            st.query_params["page"] = "login"
            st.rerun()

    st.markdown('</div></div>', unsafe_allow_html=True)


def render_setting_user_page():
    vm = get_setting_user_view_model()
    _ensure_setting_state()

    _render_navbar(vm)
    _render_message()
    _render_profile_card(vm)
    _render_theme_block(vm)
    _render_notification_block(vm)
    _render_account_block(vm)