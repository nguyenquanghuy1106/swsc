from features.home.data.home_data import (
    get_home_categories,
    get_home_environment_messages,
    get_home_benefits,
    get_home_footer_info,
    get_home_hero_data,
    get_home_banner_images,
)


def get_home_data():
    return {
        "hero": get_home_hero_data(),
        "categories": get_home_categories(),
        "environment_messages": get_home_environment_messages(),
        "benefits": get_home_benefits(),
        "footer": get_home_footer_info(),
        "images": get_home_banner_images(),
    }


def get_home_categories_data():
    return get_home_categories()


def get_home_environment_data():
    return get_home_environment_messages()


def get_home_benefits_data():
    return get_home_benefits()


def get_home_footer_data():
    return get_home_footer_info()


def get_home_hero_view_data():
    return get_home_hero_data()


def get_home_images_data():
    return get_home_banner_images()