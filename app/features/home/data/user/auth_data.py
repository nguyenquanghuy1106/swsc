def get_auth_branding():
    return {
        "app_name": "SWCS",
        "login_title": "Đăng nhập",
        "register_title": "Đăng ký",
        "login_subtitle": "Chào mừng bạn quay trở lại với hệ thống phân loại rác thông minh.",
        "register_subtitle": "Tạo tài khoản mới để bắt đầu trải nghiệm SWCS.",
        "background_image": "assets/auth/login.png",
        "google_button_text": "Đăng nhập với Google",
        "footer_text": "SWCS – Hệ Thống Phân Loại Rác Thải Thông Minh",
    }


def get_login_defaults():
    return {
        "email": "",
        "password": "",
        "remember": True,
    }


def get_register_defaults():
    return {
        "full_name": "",
        "email": "",
        "password": "",
        "confirm_password": "",
        "agree_terms": False,
    }