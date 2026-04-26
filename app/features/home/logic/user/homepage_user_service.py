from features.home.data.user.homepage_user_data import (
    get_homepage_user_branding,
    get_homepage_user_posts,
    get_homepage_user_profile,
)


def get_homepage_user_view_model():
    return {
        "branding": get_homepage_user_branding(),
        "profile": get_homepage_user_profile(),
        "posts": get_normalized_posts(),
    }


def normalize_post(post: dict) -> dict:
    return {
        "post_id": post.get("post_id", ""),
        "author": {
            "id": post.get("author", {}).get("id", ""),
            "name": post.get("author", {}).get("name", "Người dùng"),
            "avatar_url": post.get("author", {}).get("avatar_url", ""),
        },
        "time_text": post.get("time_text", ""),
        "content": post.get("content", ""),
        "images": post.get("images", []),
        "stats": {
            "likes": post.get("stats", {}).get("likes", 0),
            "comments": post.get("stats", {}).get("comments", 0),
            "share_label": post.get("stats", {}).get("share_label", "Chia sẻ"),
        },
    }


def get_normalized_posts():
    return [normalize_post(post) for post in get_homepage_user_posts()]


def filter_posts_by_keyword(posts: list[dict], keyword: str) -> list[dict]:
    keyword = (keyword or "").strip().lower()
    if not keyword:
        return posts

    filtered_posts = []
    for post in posts:
        author_name = post.get("author", {}).get("name", "").lower()
        content = post.get("content", "").lower()

        if keyword in author_name or keyword in content:
            filtered_posts.append(post)

    return filtered_posts


def build_feed_message(total_posts: int, keyword: str) -> str:
    keyword = (keyword or "").strip()
    if keyword:
        return f"Tìm thấy {total_posts} bài viết phù hợp với từ khóa “{keyword}”."
    return f"Đang hiển thị {total_posts} bài viết trong cộng đồng."