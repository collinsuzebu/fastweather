import typing as t

city_id_1 = "3443207"
city_id_2 = "3442546"
city_temp_1 = 15
city_temp_2 = 18
city_humidity_1 = 27
city_humidity_2 = 25


def gen_data(city_id=city_id_1, temp=city_temp_1, humidity=city_humidity_1) -> t.Dict:
    return {
        "cnt": 1,
        "list": [
            {
                "coord": {"lon": -57.63, "lat": -32.68},
                "sys": {
                    "country": "UY",
                    "timezone": -10800,
                    "sunrise": 1608799278,
                    "sunset": 1608850755,
                },
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01n",
                    }
                ],
                "main": {
                    "temp": temp,
                    "feels_like": 16.49,
                    "temp_min": 30.01,
                    "temp_max": 30.01,
                    "pressure": 1013,
                    "sea_level": 1013,
                    "grnd_level": 1004,
                    "humidity": humidity,
                },
                "visibility": 10000,
                "wind": {"speed": 4.26, "deg": 59},
                "clouds": {"all": 0},
                "dt": 1608782971,
                "id": city_id,
                "name": "Young",
            }
        ],
    }


weather_map_multi_response = [
    gen_data(city_id_1, city_temp_1, city_humidity_1),
    gen_data(city_id_2, city_temp_2, city_humidity_2),
]
