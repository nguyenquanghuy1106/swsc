def get_battery_categories():
    return [
        {
            "code": "Zn + MnO₂",
            "number": "1",
            "years": "100 – 500 năm",
            "bar_class": "bar-green",
            "emoji": "🔋",
            "image": "assets/battery/zinc_carbon.png",
            "description": "Pin tiểu than thông dụng, dùng cho điều khiển, đồng hồ, đồ chơi nhỏ."
        },
        {
            "code": "Zn + MnO₂ (kiềm)",
            "number": "2",
            "years": "100 – 300 năm",
            "bar_class": "bar-green",
            "emoji": "🔋",
            "image": "assets/battery/alkaline.png",
            "description": "Pin alkaline bền hơn pin thường, phổ biến trong thiết bị điện tử gia đình."
        },
        {
            "code": "Nickel + Cadmium",
            "number": "3",
            "years": "500 – 1000 năm",
            "bar_class": "bar-yellow",
            "emoji": "🪫",
            "image": "assets/battery/nicd.png",
            "description": "Pin sạc Ni-Cd, có chứa cadmium độc hại, cần thu gom riêng."
        },
        {
            "code": "Pb + H₂SO₄",
            "number": "4",
            "years": "400 – 1000 năm",
            "bar_class": "bar-orange",
            "emoji": "🔋",
            "image": "assets/battery/lead_acid.png",
            "description": "Ắc quy chì dùng cho xe máy, ô tô; chứa chì và axit sunfuric nguy hại."
        },
    ]


def get_battery_summary_items():
    return [
        "Pin tiểu thông thường: 100 – 500 năm",
        "Pin alkaline: 100 – 300 năm",
        "Pin sạc Ni-Cd: 500 – 1000 năm",
        "Ắc quy chì: 400 – 1000 năm, độc hại cao",
    ]


def get_battery_environment_notes():
    return [
        "Pin tiêu tốn ở pin phân loại riêng, không bỏ lẫn rác sinh hoạt.",
        "Không bán pin ra môi trường vì kim loại nặng có thể rò rỉ.",
        "Thẻ sinh hoạt pin sạc hay ắc quy có nguy cơ ô nhiễm đất và nước.",
        "Pin cũ nên mang đến điểm thu gom hoặc đơn vị xử lý chuyên dụng.",
    ]