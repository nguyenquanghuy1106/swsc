def get_nylon_categories():
    return [
        {
            "code": "Polyethylene (PE)",
            "number": "1",
            "years": "100 – 500 năm",
            "bar_class": "bar-green",
            "emoji": "🛍️",
            "image": "assets/nylon/pe_bag.png",
            "description": "Túi nilon PE phổ biến trong mua sắm hằng ngày, rất khó phân hủy."
        },
        {
            "code": "Polyethylene TTC",
            "number": "2",
            "years": "> 1000 năm",
            "bar_class": "bar-red",
            "emoji": "🧴",
            "image": "assets/nylon/ttc_bag.png",
            "description": "Loại nilon tổng hợp bền cao, tồn tại rất lâu trong môi trường."
        },
        {
            "code": "PE",
            "number": "3",
            "years": "2 – 5 năm",
            "bar_class": "bar-green",
            "emoji": "📦",
            "image": "assets/nylon/pe_roll.png",
            "description": "Màng PE hoặc nilon mỏng dùng đóng gói, bọc thực phẩm và hàng hóa."
        },
        {
            "code": "100% từ tinh bột, mía, bắp",
            "number": "4",
            "years": "6 tháng – 1 năm",
            "bar_class": "bar-yellow",
            "emoji": "🌿",
            "image": "assets/nylon/bio_bag.png",
            "description": "Túi sinh học có nguồn gốc tự nhiên, phân hủy nhanh hơn nilon thông thường."
        },
    ]


def get_nylon_summary_items():
    return [
        "Túi PE thông thường: 100 – 500 năm",
        "Nilon tổng hợp bền cao: trên 1000 năm",
        "Màng PE mỏng: 2 – 5 năm",
        "Túi sinh học từ tinh bột, mía, bắp: 6 tháng – 1 năm",
    ]


def get_nylon_environment_notes():
    return [
        "Túi nilon gây ô nhiễm đất và nước nếu thải bỏ không đúng cách.",
        "Nilon có thể làm hại động vật khi bị ăn nhầm hoặc mắc kẹt.",
        "Nilon phân rã thành vi nhựa, ảnh hưởng lâu dài đến môi trường.",
        "Nên ưu tiên tái sử dụng hoặc thay bằng túi sinh học, túi vải.",
    ]