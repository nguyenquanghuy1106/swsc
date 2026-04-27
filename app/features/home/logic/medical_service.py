from features.home.data.classification.medical_data import (
    get_medical_categories,
    get_medical_summary_items,
    get_medical_environment_notes,
)


def get_medical_data():
    return {
        "categories": get_medical_categories(),
        "summary_items": get_medical_summary_items(),
        "environment_notes": get_medical_environment_notes(),
    }