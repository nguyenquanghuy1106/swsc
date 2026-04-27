def get_plastic_categories():
    return [
        {
            "code": "PET",
            "number": "1",
            "years": "450 – 500 năm",
            "bar_class": "bar-green",
            "emoji": "🧴",
            "image": "assets/plastic/pet.png",
            "description": "Chai nước, chai nước ngọt, bao bì thực phẩm."
        },
        {
            "code": "HDPE",
            "number": "2",
            "years": "500 – 1000 năm",
            "bar_class": "bar-yellow",
            "emoji": "🧼",
            "image": "assets/plastic/hdpe.png",
            "description": "Can nhựa, chai chất tẩy rửa, bình sữa."
        },
        {
            "code": "PVC",
            "number": "3",
            "years": "600 – 1000 năm",
            "bar_class": "bar-orange",
            "emoji": "🧪",
            "image": "assets/plastic/pvc.png",
            "description": "Ống nhựa, vật liệu xây dựng, áo mưa."
        },
        {
            "code": "LDPE",
            "number": "4",
            "years": "400 – 1000 năm",
            "bar_class": "bar-yellow",
            "emoji": "🛍️",
            "image": "assets/plastic/ldpe.png",
            "description": "Túi nilon, màng bọc thực phẩm, bao gói mềm."
        },
        {
            "code": "PP",
            "number": "5",
            "years": "250 – 500 năm",
            "bar_class": "bar-green",
            "emoji": "🍱",
            "image": "assets/plastic/pp.png",
            "description": "Hộp đựng thức ăn, cốc nhựa, nắp chai."
        },
        {
            "code": "OTHER / PS",
            "number": "6",
            "years": "Có thể trên 1000 năm",
            "bar_class": "bar-red",
            "emoji": "🥤",
            "image": "assets/plastic/ps.png",
            "description": "Ly xốp, hộp xốp, nhựa hỗn hợp khó tái chế."
        },
    ]


def get_summary_items():
    return [
        "Chai PET: khoảng 450 – 500 năm",
        "HDPE, PVC: 500 – 1000 năm",
        "Túi nilon (LDPE): 400 – 1000 năm",
        "PP: 250 – 500 năm",
        "Nhựa OTHER / PS có thể tồn tại hơn 1000 năm",
    ]


def get_environment_notes():
    return [
        "Nhựa phân hủy rất chậm trong môi trường tự nhiên.",
        "Cần phân loại đúng để hỗ trợ tái chế hiệu quả.",
        "Một số loại nhựa không nên đốt trực tiếp vì có thể sinh khí độc.",
        "Nên ưu tiên tái sử dụng hoặc thu gom đúng nơi quy định.",
    ]