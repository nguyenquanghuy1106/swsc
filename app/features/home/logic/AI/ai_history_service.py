import streamlit as st
from features.database.connection import get_connection


def _get_login_user():
    user_id = st.session_state.get("user_id")
    user_name = st.session_state.get("user_name")

    if user_id is None:
        uid = st.query_params.get("uid")
        if isinstance(uid, list):
            uid = uid[0]

        if uid:
            user_id = int(uid)
            st.session_state["user_id"] = user_id

    if not user_name:
        uname = st.query_params.get("uname")
        if isinstance(uname, list):
            uname = uname[0]

        if uname:
            user_name = uname
            st.session_state["user_name"] = user_name

    return user_id, user_name


def save_ai_history(
    user_id=None,
    user_name=None,
    waste_type=None,
    predicted_class=None,
    confidence=None,
    image_name=None
):
    if user_id is None or not user_name:
        user_id, user_name = _get_login_user()

    if user_id is None or not user_name:
        raise ValueError("Chưa có thông tin đăng nhập, không thể lưu lịch sử AI.")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO ai_history
        (
            user_id,
            user_name,
            waste_type,
            predicted_class,
            confidence,
            image_name
        )
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (
            user_id,
            user_name,
            waste_type,
            predicted_class,
            confidence,
            image_name,
        )
    )

    conn.commit()
    cursor.close()
    conn.close()