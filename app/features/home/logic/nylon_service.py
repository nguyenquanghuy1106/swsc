from features.home.data.classification.nylon_data import (
    get_nylon_categories,
    get_nylon_summary_items,
    get_nylon_environment_notes,
)


def get_nylon_data():
    return {
        "categories": get_nylon_categories(),
        "summary_items": get_nylon_summary_items(),
        "environment_notes": get_nylon_environment_notes(),
    }