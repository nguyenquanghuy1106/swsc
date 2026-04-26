import re

from features.home.data.user.auth_data import (
    get_auth_branding,
    get_login_defaults,
    get_register_defaults,
)


def get_auth_view_model():
    return {
        "branding": get_auth_branding(),
        "login_defaults": get_login_defaults(),
        "register_defaults": get_register_defaults(),
    }


def validate_email(email: str) -> tuple[bool, str]:
    email = (email or "").strip()
    if not email:
        return False, "Vui lòng nhập email."

    pattern = r"^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$"
    if not re.match(pattern, email):
        return False, "Email chưa đúng định dạng."

    return True, ""


def validate_login(email: str, password: str) -> tuple[bool, str]:
    is_valid_email, message = validate_email(email)
    if not is_valid_email:
        return False, message

    if not password:
        return False, "Vui lòng nhập mật khẩu."

    if len(password) < 6:
        return False, "Mật khẩu cần có ít nhất 6 ký tự."

    return True, "Đăng nhập hợp lệ."


def validate_register(
    full_name: str,
    email: str,
    password: str,
    confirm_password: str,
    agree_terms: bool,
) -> tuple[bool, str]:
    if not (full_name or "").strip():
        return False, "Vui lòng nhập họ và tên."

    is_valid_email, message = validate_email(email)
    if not is_valid_email:
        return False, message

    if not password:
        return False, "Vui lòng nhập mật khẩu."

    if len(password) < 6:
        return False, "Mật khẩu cần có ít nhất 6 ký tự."

    if password != confirm_password:
        return False, "Mật khẩu xác nhận không khớp."

    if not agree_terms:
        return False, "Bạn cần đồng ý với điều khoản để đăng ký."

    return True, "Đăng ký hợp lệ."


def authenticate_user(email: str, password: str) -> tuple[bool, str]:
    """
    Tạm thời demo local.
    Sau này bạn thay bằng kiểm tra DB/API thật.
    """
    ok, message = validate_login(email, password)
    if not ok:
        return False, message

    return True, "Đăng nhập thành công."


def register_user(
    full_name: str,
    email: str,
    password: str,
    confirm_password: str,
    agree_terms: bool,
) -> tuple[bool, str]:
    """
    Tạm thời demo local.
    Sau này bạn thay bằng lưu DB/API thật.
    """
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