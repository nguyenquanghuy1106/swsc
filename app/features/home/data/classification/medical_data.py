def get_medical_categories():
    return [
        {
            "code": "Cao su",
            "number": "1",
            "years": "450 – 500 năm",
            "bar_class": "bar-green",
            "emoji": "🧤",
            "image": "assets/medical/rubber_gloves.png",
            "description": "Găng tay, ống cao su và một số vật tư y tế bằng cao su cần thu gom đúng cách."
        },
        {
            "code": "Nhựa PP, PE",
            "number": "2",
            "years": "600 – 1000 năm",
            "bar_class": "bar-green",
            "emoji": "🧪",
            "image": "assets/medical/sample_tubes.png",
            "description": "Ống nghiệm, cốc mẫu, hộp đựng bằng PP hoặc PE có thời gian phân hủy rất dài."
        },
        {
            "code": "Nhựa PET, PVC",
            "number": "3",
            "years": "600 – 1000 năm",
            "bar_class": "bar-green",
            "emoji": "💉",
            "image": "assets/medical/syringe_vials.png",
            "description": "Chai lọ, ống truyền, một số vật tư PET hoặc PVC cần phân loại riêng sau sử dụng."
        },
        {
            "code": "Polypropylene",
            "number": "4",
            "years": "400 – 1000 năm",
            "bar_class": "bar-green",
            "emoji": "🩺",
            "image": "assets/medical/polypropylene_medical.png",
            "description": "Một số ống tiêm, vỏ dụng cụ và vật tư y tế polypropylene tồn tại lâu trong môi trường."
        },
    ]


def get_medical_summary_items():
    return [
        "Dụng cụ có dính máu, dịch, kim tiêm, bông băng → rác lây nhiễm (thùng màu vàng).",
        "Dụng cụ bằng nhựa, thủy tinh sạch → có thể tái chế hoặc thu gom riêng.",
        "Dụng cụ chứa hóa chất, thuốc, pin, thủy ngân → rác nguy hại.",
        "Không trộn lẫn rác y tế với rác sinh hoạt thông thường.",
    ]


def get_medical_environment_notes():
    return [
        "Rác y tế cần được phân loại ngay từ nguồn phát sinh.",
        "Không tái sử dụng vật tư y tế đã nhiễm bẩn nếu không qua xử lý chuyên dụng.",
        "Kim tiêm, ống tiêm, vật sắc nhọn phải cho vào hộp an toàn.",
        "Rác y tế sai quy trình có thể gây lây nhiễm và ô nhiễm môi trường nghiêm trọng.",
    ]