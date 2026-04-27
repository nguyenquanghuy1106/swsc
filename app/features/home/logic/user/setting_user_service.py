from features.home.data.user.setting_user_data import (
    get_setting_user_account_items,
    get_setting_user_branding,
    get_setting_user_notification_items,
    get_setting_user_profile,
    get_setting_user_theme_items,
)


def get_setting_user_view_model():
    return {
        "branding": get_setting_user_branding(),
        "profile": get_setting_user_profile(),
        "theme_items": get_setting_user_theme_items(),
        "notification_items": get_setting_user_notification_items(),
        "account_items": get_setting_user_account_items(),
    }


def initialize_setting_state():
    defaults = {
        "dark_mode": False,
        "light_mode": True,
        "sound_vibration": True,
        "notification_status": True,
    }
    return defaults


def normalize_theme_state(
    dark_mode: bool,
    light_mode: bool,
) -> tuple[bool, bool]:
    # Chỉ cho phép 1 giao diện active
    if dark_mode and light_mode:
        return False, True

    if not dark_mode and not light_mode:
        return False, True

    return dark_mode, light_mode


def handle_theme_toggle(changed_key: str, dark_mode: bool, light_mode: bool) -> tuple[bool, bool]:
    if changed_key == "dark_mode":
        if dark_mode:
            return True, False
        return False, True

    if changed_key == "light_mode":
        if light_mode:
            return False, True
        return True, False

    return normalize_theme_state(dark_mode, light_mode)


def build_setting_action_message(action_key: str) -> str:
    mapping = {
        "sound_vibration": "Đã mở phần cài đặt âm thanh và rung.",
        "notification_status": "Đã mở phần cài đặt thông báo.",
        "change_password": "Đã chọn thay đổi mật khẩu.",
        "edit_profile": "Đã chọn sửa thông tin cá nhân.",
        "login_history": "Đã chọn xem lịch sử đăng nhập.",
        "pin_setup": "Đã chọn thiết lập mật mã.",
        "logout": "Đã đăng xuất.",
    }
    return mapping.get(action_key, "Đã thực hiện thao tác.")