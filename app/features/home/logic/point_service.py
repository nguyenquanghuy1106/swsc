from features.database.connection import get_connection


POINT_TABLES = [
    "recyclable_waste_history",
    "organic_waste_history",
    "other_waste_history",
    "hazardous_waste_history",
]


def get_user_total_points(user_id):
    if not user_id:
        return 0

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    total_points = 0

    for table in POINT_TABLES:
        cursor.execute(
            f"""
            SELECT COALESCE(SUM(score), 0) AS total
            FROM {table}
            WHERE user_id = %s
            """,
            (user_id,),
        )

        row = cursor.fetchone()
        total_points += int(row["total"] or 0)

    cursor.close()
    conn.close()

    return total_points