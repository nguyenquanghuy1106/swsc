import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="swsc",
        port=3306,
    )


def get_all_posted_news(user_id=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    sql = """
        SELECT 
            p.*,
            r.userName AS user_name,
            r.phone AS user_phone,

            (SELECT COUNT(*) 
             FROM post_likes l 
             WHERE l.post_id = p.id) AS like_count,

            (SELECT COUNT(*) 
             FROM post_comments c 
             WHERE c.post_id = p.id) AS comment_count,

            EXISTS(
                SELECT 1 
                FROM post_likes l2 
                WHERE l2.post_id = p.id 
                AND (
                    (l2.user_id = %s) 
                    OR (l2.user_id IS NULL AND %s IS NULL)
                )
            ) AS liked_by_me

        FROM posts p
        LEFT JOIN register r ON p.user_id = r.id
        WHERE p.status = 'posted'
        ORDER BY p.created_at DESC
    """

    cursor.execute(sql, (user_id, user_id))
    posts = cursor.fetchall()

    cursor.close()
    conn.close()
    return posts


def toggle_like(post_id, user_id=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT id FROM post_likes
        WHERE post_id = %s AND (
            (user_id = %s) OR (user_id IS NULL AND %s IS NULL)
        )
        LIMIT 1
        """,
        (post_id, user_id, user_id),
    )

    liked = cursor.fetchone()

    if liked:
        cursor.execute("DELETE FROM post_likes WHERE id = %s", (liked["id"],))
        message = "Đã bỏ thích bài viết."
    else:
        cursor.execute(
            "INSERT INTO post_likes (post_id, user_id) VALUES (%s, %s)",
            (post_id, user_id),
        )
        message = "Đã thích bài viết."

    conn.commit()
    cursor.close()
    conn.close()

    return {"success": True, "message": message}


def add_comment(post_id, comment_text, user_id=None):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO post_comments (post_id, user_id, comment_text)
        VALUES (%s, %s, %s)
        """,
        (post_id, user_id, comment_text),
    )

    conn.commit()
    cursor.close()
    conn.close()

    return {"success": True, "message": "Đã gửi bình luận."}


def get_comments_by_post(post_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT 
            c.id,
            c.post_id,
            c.user_id,
            c.comment_text,
            c.created_at,
            r.userName AS user_name
        FROM post_comments c
        LEFT JOIN register r ON c.user_id = r.id
        WHERE c.post_id = %s
        ORDER BY c.created_at DESC
        """,
        (post_id,),
    )
    comments = cursor.fetchall()

    cursor.close()
    conn.close()
    return comments