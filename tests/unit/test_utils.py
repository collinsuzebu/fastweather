import itertools
import pytest
from fastweather.utils import (
    get_current_percentage,
    extract_info,
    load_cities_in_chunks,
    parse_weather_request,
)


def test_get_current_percentage():
    current = 2
    total = 100
    result = get_current_percentage(current, total)

    assert type(result) is float
    assert result == 2.00


def test_extract_info():
    mock_results = [
        {"city_id": 3439525, "temperature": 22.78, "humidity": 58},
        {"city_id": 3439526, "temperature": 5.78, "humidity": 58},
    ]
    mock_data = [
        {
            "list": [
                {"id": 3439525, "main": {"temp": 22.78, "humidity": 58}},
                {"id": 3439526, "main": {"temp": 5.78, "humidity": 58}},
            ]
        },
    ]

    result = extract_info(mock_data)
    assert result == mock_results


def test_load_cities_in_chunks_raises_error():
    """Raises error when `chunks` value is larger than range(1, 20 <inclusive>)"""
    with pytest.raises(ValueError):
        generator = load_cities_in_chunks("tests/test_cities_id.txt", chunks=30)
        next(generator)


def test_load_cities_in_chunks():
    generator = load_cities_in_chunks("tests/unit/test_cities_id.txt", chunks=3)

    first_value = next(generator)
    second_value = next(generator)
    n_values = itertools.islice(generator, 2)

    assert first_value == "3439525,3439781,3440645"
    assert second_value == "3442098,3442778,3443341"
    assert list(n_values) == ["3442233,3440781,3441572", "3441575,3443207,3442546"]


def test_parse_weather_request():
    expected = {
        "request_id": "15",
        "created_at": "2020-12-06T06:13:22.676352",
        "status": "PENDING",
        "percentage_completed": "0%",
        "data": None,
    }
    w_request_data = {**expected, "_id": {"$oid": "5fcc768c3f38fd7e9f84db17"}}

    result = parse_weather_request(w_request_data)

    assert type(result) == dict
    assert result == expected
