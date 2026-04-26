def get_homepage_user_branding():
    return {
        "app_name": "SWCS",
        "page_title": "Cộng đồng",
        "search_placeholder": "Tìm kiếm ...",
        "composer_placeholder": "Hôm nay bạn nghĩ gì ?",
        "nav_items": [
            {"label": "Trang chủ", "href": "?page=home"},
            {"label": "Khám phá", "href": "?page=explore"},
            {"label": "Thông điệp", "href": "?page=message"},
            {"label": "Lợi ích", "href": "?page=benefits"},
            {"label": "Thông tin", "href": "?page=about"},
        ],
    }


def get_homepage_user_profile():
    return {
        "id": "user_001",
        "display_name": "Healing",
        "avatar_url": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=300&auto=format&fit=crop",
    }


def get_homepage_user_posts():
    return [
        {
            "post_id": "post_001",
            "author": {
                "id": "user_101",
                "name": "Healing",
                "avatar_url": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=300&auto=format&fit=crop",
            },
            "time_text": "Vừa xong",
            "content": "Tôi vừa phân loại xong rác hôm nay! Cảm giác thật nhẹ lòng 💚",
            "images": [
                "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?q=80&w=1200&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=1200&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1611284446314-60a58ac0deb9?q=80&w=1200&auto=format&fit=crop",
            ],
            "stats": {
                "likes": 209,
                "comments": 15,
                "share_label": "Cao",
            },
        },
        {
            "post_id": "post_002",
            "author": {
                "id": "user_102",
                "name": "Save",
                "avatar_url": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=300&auto=format&fit=crop",
            },
            "time_text": "10 phút trước",
            "content": "Tôi vừa phân loại xong rác hôm nay! Cảm giác thật nhẹ lòng 💚",
            "images": [
                "assets/auth/login.png",
            ],
            "stats": {
                "likes": 102,
                "comments": 8,
                "share_label": "Cao",
            },
        },
    ]