import re

from features.home.data.user.register_data import (
    get_register_branding,
    get_register_defaults,
)


def get_register_view_model():
    return {
        "branding": get_register_branding(),
        "defaults": get_register_defaults(),
    }


def validate_register(
    full_name: str,
    email: str,
    password: str,
    confirm_password: str,
    agree_terms: bool,
) -> tuple[bool, str]:
    full_name = (full_name or "").strip()
    email = (email or "").strip()

    if not full_name:
        return False, "Vui lòng nhập họ và tên."

    if not email:
        return False, "Vui lòng nhập email."

    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    if not re.match(pattern, email):
        return False, "Email chưa đúng định dạng."

    if not password:
        return False, "Vui lòng nhập mật khẩu."

    if len(password) < 6:
        return False, "Mật khẩu cần có ít nhất 6 ký tự."

    if password != confirm_password:
        return False, "Mật khẩu xác nhận không khớp."

    if not agree_terms:
        return False, "Bạn cần đồng ý với điều khoản để đăng ký."

    return True, "Đăng ký hợp lệ."


def register_user(
    full_name: str,
    email: str,
    password: str,
    confirm_password: str,
    agree_terms: bool,
) -> tuple[bool, str]:
    ok, message = validate_register(
        full_name=full_name,
        email=email,
        password=password,
        confirm_password=confirm_password,
        agree_terms=agree_terms,
    )
    if not ok:
        return False, message

    return True, "Tạo tài khoản thành công."