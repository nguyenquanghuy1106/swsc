from features.home.data.classification.battery_data import (
    get_battery_categories,
    get_battery_summary_items,
    get_battery_environment_notes,
)


def get_battery_data():
    return {
        "categories": get_battery_categories(),
        "summary_items": get_battery_summary_items(),
        "environment_notes": get_battery_environment_notes(),
    }