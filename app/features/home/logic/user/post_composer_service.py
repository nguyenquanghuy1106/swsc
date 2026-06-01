from datetime import datetime
from pathlib import Path
import mysql.connector


BASE_DIR = Path(__file__).resolve().parents[4]
UPLOAD_DIR = BASE_DIR / "assets" / "posts"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="swsc",
        port=3306,
    )


def save_uploaded_image(image):
    if image is None:
        return None, None

    image_name = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{image.name}"
    image_path = UPLOAD_DIR / image_name

    with open(image_path, "wb") as f:
        f.write(image.getbuffer())

    return image_name, str(image_path)


def save_post_to_database(title, category, content, image=None, status="posted", user_id=None):
    if user_id is None:
        raise Exception("Không tìm thấy id tài khoản đăng nhập. Vui lòng đăng nhập lại.")

    image_name, image_path = save_uploaded_image(image)

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
        INSERT INTO posts (
            user_id, title, category, content,
            image_name, image_path, status, created_at
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        user_id,
        title,
        category,
        content,
        image_name,
        image_path,
        status,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )

    cursor.execute(sql, values)
    conn.commit()

    post_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return post_id


def create_post_data(title, category, content, image=None, user_id=None):
    post_id = save_post_to_database(
        title=title,
        category=category,
        content=content,
        image=image,
        status="posted",
        user_id=user_id,
    )

    return {
        "success": True,
        "message": "Đăng bài thành công và đã lưu vào database!",
        "post_id": post_id,
    }


def save_draft_data(title, category, content, image=None, user_id=None):
    post_id = save_post_to_database(
        title=title,
        category=category,
        content=content,
        image=image,
        status="draft",
        user_id=user_id,
    )

    return {
        "success": True,
        "message": "Đã lưu nháp vào database!",
        "post_id": post_id,
    }