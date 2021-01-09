import typing as t
import pytest

import tests.data as data


@pytest.fixture
def open_wm_response_data():
    return data.weather_map_multi_response


@pytest.fixture
def get_response_data() -> t.Any:
    return {
        "request_id": "1",
        "created_at": "2020-12-05T07:59:01.986863",
        "status": "COMPLETE",
        "percentage_completed": "100.0%",
        "data": [
            {
                "city_id": data.city_id_1,
                "temperature": data.city_temp_1,
                "humidity": data.city_humidity_1,
            },
            {
                "city_id": data.city_id_2,
                "temperature": data.city_temp_2,
                "humidity": data.city_humidity_2,
            },
        ],
    }
