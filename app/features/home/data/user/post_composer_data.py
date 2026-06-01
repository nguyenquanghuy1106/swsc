def get_post_composer_branding():
    return {
        "app_name": "SWSC",
        "title": "Chia sẻ hành động xanh của bạn cùng SWSC! 🌱",
        "subtitle_label": "Phụ tiêu đề",
        "subtitle_placeholder": "Đặt một tiêu đề thật thu hút nào... (Ví dụ: Mẹo tái chế chai nhựa thành chậu cây)",
        "content_placeholder": "Hôm nay bạn đã phân loại rác như thế nào? Chia sẻ mẹo nhỏ hoặc hình ảnh để truyền cảm hứng cho cộng đồng nhé...",
        "draft_button": "Lưu Nháp",
        "post_button": "Đăng bài ngay 🚀",
    }


def get_post_categories():
    return [
        {"label": "Rác Hữu Cơ", "icon": "🟢", "class": "organic"},
        {"label": "Rác Tái Chế", "icon": "🔵", "class": "recycle"},
        {"label": "Rác Nguy Hại", "icon": "🔴", "class": "danger"},
        {"label": "Mẹo Sống Xanh", "icon": "🌟", "class": "tips"},
    ]


def get_right_sidebar_data():
    return {
        "challenge": {
            "title": "🏆 Thử Thách Xanh",
            "content": "Thử thách hôm nay:<br><b>Đăng ảnh phân loại rác thải nhựa tích ngay +50 điểm!</b>",
        },
        "hashtags": [
            "#SWSC_PhanLoaiRac",
            "#SongXanhMoiNgay",
            "#TaiCheSangTao",
        ],
        "tip": {
            "title": "💡 Mẹo Nhanh",
            "content": "Vỏ hộp sữa sau khi uống xong cần được súc sạch và làm phẳng trước khi bỏ vào thùng rác tái chế!",
        },
    }