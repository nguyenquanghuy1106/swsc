def get_setting_user_branding():
    return {
        "app_name": "SWCS",
        "nav_items": [
            {"label": "Trang chủ", "href": "?page=home"},
            {"label": "Khám phá", "href": "?page=explore"},
            {"label": "Thông điệp", "href": "?page=message"},
            {"label": "Lợi ích", "href": "?page=benefits"},
            {"label": "Thông tin", "href": "?page=about"},
        ],
        "search_icon": "🔍",
        "page_title": "Cài đặt",
        "logout_text": "Đăng xuất",
    }


def get_setting_user_profile():
    return {
        "name": "Linh Chi",
        "email": "linhchi@gmail.com",
        "avatar_url": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=300&auto=format&fit=crop",
    }


def get_setting_user_theme_items():
    return [
        {
            "key": "dark_mode",
            "icon": "✳️",
            "title": "Giao diện tối",
            "subtitle": "Chế độ ban đêm  •  Đỡ mỏi mắt",
            "default": False,
        },
        {
            "key": "light_mode",
            "icon": "☀️",
            "title": "Giao diện sáng",
            "subtitle": "Chế độ ban ngày  •  Rõ ràng, sáng sủa",
            "default": True,
        },
    ]


def get_setting_user_notification_items():
    return [
        {
            "key": "sound_vibration",
            "icon": "🔊",
            "title": "Âm thanh và rung",
            "subtitle": "Chế độ âm thanh  •  Nhạc chuông",
        },
        {
            "key": "notification_status",
            "icon": "📄",
            "title": "Thông báo",
            "subtitle": "Thông tin trạng  •  Không làm phiền",
        },
    ]


def get_setting_user_account_items():
    return [
        {"key": "change_password", "icon": "🔒", "title": "Thay đổi mật khẩu"},
        {"key": "edit_profile", "icon": "👤", "title": "Sửa thông tin cá nhân"},
        {"key": "login_history", "icon": "🕘", "title": "Lịch sử đăng nhập"},
        {"key": "pin_setup", "icon": "🛡️", "title": "Thiết lập mật mã"},
    ]