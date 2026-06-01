from features.database.connection import get_connection


WASTE_SAVE_MAP = {
    "plastic": {"table": "recyclable_waste_history", "group": "RÁC TÁI CHẾ", "score": 2},
    "paper": {"table": "recyclable_waste_history", "group": "RÁC TÁI CHẾ", "score": 2},
    "cardboard": {"table": "recyclable_waste_history", "group": "RÁC TÁI CHẾ", "score": 2},
    "glass": {"table": "recyclable_waste_history", "group": "RÁC TÁI CHẾ", "score": 2},
    "metal": {"table": "recyclable_waste_history", "group": "RÁC TÁI CHẾ", "score": 2},

    "biological": {"table": "organic_waste_history", "group": "RÁC HỮU CƠ", "score": 3},

    "clothes": {"table": "other_waste_history", "group": "RÁC KHÁC", "score": 4},
    "shoes": {"table": "other_waste_history", "group": "RÁC KHÁC", "score": 4},
    "trash": {"table": "other_waste_history", "group": "RÁC KHÁC", "score": 4},

    "battery": {"table": "hazardous_waste_history", "group": "RÁC NGUY HẠI", "score": 5},
}


POINT_TABLES = [
    "recyclable_waste_history",
    "organic_waste_history",
    "other_waste_history",
    "hazardous_waste_history",
]


def normalize_class_name(name):
    return str(name).strip().lower().replace(" ", "_")


def get_user_total_score(user_id):
    if not user_id:
        return 0

    conn = get_connection()
    cursor = conn.cursor()

    total_score = 0

    for table in POINT_TABLES:
        cursor.execute(
            f"SELECT COALESCE(SUM(score), 0) FROM {table} WHERE user_id = %s",
            (user_id,),
        )
        total_score += int(cursor.fetchone()[0] or 0)

    cursor.close()
    conn.close()

    return total_score


def save_ai_scan_result(user_id, user_name, predicted_class, confidence, image_name=None):
    waste_key = normalize_class_name(predicted_class)

    if waste_key not in WASTE_SAVE_MAP:
        return {
            "success": False,
            "message": f"Không tìm thấy nhóm rác cho loại: {predicted_class}",
        }

    info = WASTE_SAVE_MAP[waste_key]

    conn = get_connection()
    cursor = conn.cursor()

    sql = f"""
        INSERT INTO {info["table"]}
        (
            user_id,
            user_name,
            waste_type,
            waste_group,
            score,
            confidence,
            image_name
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(
        sql,
        (
            int(user_id),
            str(user_name),
            waste_key,
            info["group"],
            info["score"],
            round(float(confidence), 2),
            image_name,
        ),
    )

    conn.commit()
    cursor.close()
    conn.close()

    total_score = get_user_total_score(user_id)

    return {
        "success": True,
        "table": info["table"],
        "group": info["group"],
        "score": info["score"],
        "total_score": total_score,
    }