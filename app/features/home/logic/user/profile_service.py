import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="swsc",
        port=3306,
    )


def get_current_login_user():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT user_id, userName
        FROM current_login
        WHERE id = 1
    """)

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user


def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT id, userName, phone, password
        FROM register
        WHERE id = %s
        """,
        (user_id,),
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user


def get_total_score(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    tables = [
        "organic_waste_history",
        "recyclable_waste_history",
        "hazardous_waste_history",
        "other_waste_history",
    ]

    total_score = 0
    total_scans = 0
    total_weight = 0

    for table in tables:
        cursor.execute(
            f"""
            SELECT 
                COALESCE(SUM(score), 0) AS total_score,
                COUNT(*) AS total_scans
            FROM {table}
            WHERE user_id = %s
            """,
            (user_id,),
        )

        row = cursor.fetchone()
        total_score += int(row["total_score"] or 0)
        total_scans += int(row["total_scans"] or 0)

    cursor.close()
    conn.close()

    return {
        "total_score": total_score,
        "total_scans": total_scans,
        "total_weight": total_scans * 5,
    }


def get_user_posts(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT id, title, category, content, image_path, status, created_at
        FROM posts
        WHERE user_id = %s
        ORDER BY created_at DESC
        """,
        (user_id,),
    )

    posts = cursor.fetchall()

    cursor.close()
    conn.close()

    return posts


def count_user_posts(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT
            SUM(CASE WHEN status = 'posted' THEN 1 ELSE 0 END) AS posted_count,
            SUM(CASE WHEN status = 'draft' THEN 1 ELSE 0 END) AS draft_count
        FROM posts
        WHERE user_id = %s
        """,
        (user_id,),
    )

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    return {
        "posted_count": int(row["posted_count"] or 0),
        "draft_count": int(row["draft_count"] or 0),
    }


def update_password(user_id, old_password, new_password):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT password
        FROM register
        WHERE id = %s
        """,
        (user_id,),
    )

    user = cursor.fetchone()

    if not user:
        cursor.close()
        conn.close()
        return {"success": False, "message": "Không tìm thấy tài khoản."}

    if user["password"] != old_password:
        cursor.close()
        conn.close()
        return {"success": False, "message": "Mật khẩu cũ không đúng."}

    cursor.execute(
        """
        UPDATE register
        SET password = %s
        WHERE id = %s
        """,
        (new_password, user_id),
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"success": True, "message": "Đổi mật khẩu thành công!"}