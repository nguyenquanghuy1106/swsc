from features.home.data.classification.plastic_data import (
    get_plastic_categories,
    get_summary_items,
    get_environment_notes
)


def get_plastic_data():
    return {
        "categories": get_plastic_categories(),
        "summary_items": get_summary_items(),
        "environment_notes": get_environment_notes(),
    }