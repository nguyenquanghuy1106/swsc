from ..data.home_data import get_home_data


def load_home_view_model():
    data = get_home_data()
    return {
        **data,
        "points_text": data.get("points", 0),
    }
