def get_home_categories():
    return [
        {
            "code": "plastic",
            "title": "Tái Chế",
            "years": "450~500 năm",
            "bar_class": "bar-green",
            "image": "assets/home/category_plastic.png",
            "href": "?page=plastic",
            "description": "Chai nhựa, hộp nhựa, lọ nhựa và các vật dụng nhựa cần được phân loại riêng để tái chế hiệu quả.",
        },
        {
            "code": "nylon",
            "title": "Hữu Cơ",
            "years": "~1000 năm",
            "bar_class": "bar-pink",
            "image": "assets/home/category_bag.png",
            "href": "?page=nylon",
            "description": "Túi ni lông rất khó phân hủy trong tự nhiên, gây ảnh hưởng lớn đến đất, nước và sinh vật.",
        },
        {
            "code": "battery",
            "title": "Nguy Hại",
            "years": "400~1000 năm",
            "bar_class": "bar-orange",
            "image": "assets/home/category_battery.png",
            "href": "?page=battery",
            "description": "Pin cũ chứa kim loại nặng và hóa chất độc hại, không được bỏ chung với rác sinh hoạt.",
        },
        {
            "code": "medical",
            "title": "Khác",
            "years": "250~1000 năm",
            "bar_class": "bar-red",
            "image": "assets/home/category_medical.png",
            "href": "?page=medical",
            "description": "Rác y tế như khẩu trang, chai lọ thuốc, vật dụng nhiễm bẩn cần xử lý theo quy trình riêng để bảo đảm an toàn.",
        },
    ]


def get_home_environment_messages():
    return [
        "Vì một Trái Đất xanh sạch đẹp",
        "Khuyến khích phân loại và tái chế",
        "Giảm thiểu rác thải ô nhiễm",
        "Chung tay vì thế hệ tương lai",
    ]


def get_home_benefits():
    return [
        "Tiết kiệm tài nguyên thiên nhiên",
        "Giảm thiểu ô nhiễm môi trường",
        "Tái chế, giảm tải bãi chôn lấp",
        "Tránh nguy hại từ rác độc hại",
    ]


def get_home_footer_info():
    return {
        "title": "SWCS – Hệ Thống Phân Loại Rác Thải Thông Minh",
        "subtitle": "Hỗ trợ nâng cao nhận thức và phân loại rác đúng cách.",
        "copyright": "© 2024 SWCS. Tất cả quyền được bảo lưu.",
        "links": [
            "Điều khoản",
            "Liên hệ 2024",
            "Điều khoản sử dụng",
        ],
    }


def get_home_hero_data():
    return {
        "title_line_1": "Phân loại hôm nay,",
        "title_line_2": "Xanh mãi ngày mai",
        "subtitle": "Phân loại rác – thói quen của người văn minh",
        "button_text": "Bắt đầu hành trình",
        "button_href": "?page=plastic",
        "image": "assets/home/hero_1.jpg",
    }


def get_home_banner_images():
    return {
        "left_info_bg": "assets/home/hero_3.jpg",
        "right_info_bg": "assets/home/hero_2.jpg",
        "avatar": "assets/home/d5fbee7c-1737-4522-9147-fe934f39454b.png",
    }