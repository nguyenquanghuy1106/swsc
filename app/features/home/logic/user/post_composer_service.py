from features.home.data.user.post_composer_data import (
    get_post_composer_branding,
    get_post_composer_defaults,
    get_post_composer_user,
)


def get_post_composer_view_model():
    return {
        "branding": get_post_composer_branding(),
        "user": get_post_composer_user(),
        "defaults": get_post_composer_defaults(),
    }


def validate_post_content(
    post_text: str,
    uploaded_media_count: int = 0,
    location: str = "",
    feeling: str = "",
) -> tuple[bool, str]:
    has_text = bool((post_text or "").strip())
    has_media = uploaded_media_count > 0
    has_location = bool((location or "").strip())
    has_feeling = bool((feeling or "").strip())

    if not (has_text or has_media or has_location or has_feeling):
        return False, "Bạn chưa nhập nội dung để đăng."

    if len((post_text or "").strip()) > 1500:
        return False, "Nội dung bài đăng quá dài. Vui lòng rút gọn dưới 1500 ký tự."

    return True, "Bài đăng hợp lệ."


def create_post_payload(
    author_name: str,
    visibility: str,
    post_text: str,
    uploaded_files: list | None = None,
    location: str = "",
    feeling: str = "",
) -> dict:
    return {
        "author_name": author_name,
        "visibility": visibility,
        "post_text": (post_text or "").strip(),
        "uploaded_files": uploaded_files or [],
        "location": (location or "").strip(),
        "feeling": (feeling or "").strip(),
    }