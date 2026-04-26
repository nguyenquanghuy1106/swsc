def get_post_composer_branding():
    return {
        "app_name": "SWCS",
        "nav_items": [
            {"label": "Trang chủ", "href": "?page=home"},
            {"label": "Khám phá", "href": "?page=explore"},
            {"label": "Thông điệp", "href": "?page=message"},
            {"label": "Lợi ích", "href": "?page=benefits"},
            {"label": "Thông tin", "href": "?page=about"},
        ],
        "search_placeholder": "Tìm kiếm...",
        "post_placeholder": "Hi, bạn đang nghĩ gì?.....",
        "post_button_text": "Đăng",
        "visibility_options": ["Công khai", "Bạn bè", "Riêng tư"],
        "action_items": [
            {"key": "media", "icon": "🖼️", "label": "Ảnh/Video"},
            {"key": "checkin", "icon": "📍", "label": "Check in"},
            {"key": "camera", "icon": "📷", "label": "Camera"},
            {"key": "feeling", "icon": "😊", "label": "Cảm xúc"},
        ],
    }


def get_post_composer_user():
    return {
        "name": "Healing",
        "avatar_url": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=300&auto=format&fit=crop",
        "default_visibility": "Công khai",
    }


def get_post_composer_defaults():
    return {
        "post_text": "",
        "visibility": "Công khai",
        "location": "",
        "feeling": "",
    }