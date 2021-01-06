import typing as t

from .config import CHUNKS


def get_current_percentage(state: int, total: int) -> float:
    """Calculates the percetage of completed tasks"""
    result = 0.0
    if state >= 0 and total:
        result = round((state / total) * 100, 2)
    return float(result)


def extract_info(results: t.List[t.Dict]) -> t.List[t.Dict]:
    """Extracts `temperature`, `humidity`, `city_id` from api results"""
    aggr = []
    for result in results:

        tmp = [
            {
                "city_id": tmp["id"],
                "temperature": tmp["main"]["temp"],
                "humidity": tmp["main"]["humidity"],
            }
            for tmp in result["list"]
        ]

        aggr.extend(tmp)
    return aggr


def load_cities_in_chunks(
    file_name: str, chunks: int = CHUNKS
) -> t.Generator[str, None, None]:
    """Yield n number of cities based on chunks specified"""

    if chunks > 20:
        raise ValueError(
            "openweathermap API can only process maximum 20 cities in one request"
        )

    CITIES = ""

    with open(file_name, "r") as file:
        for line in file:
            CITIES += "".join(line.split())
        CITIES_LIST = CITIES.split(",")

    for i in range(0, len(CITIES_LIST), chunks):
        yield ",".join(CITIES_LIST[i : i + chunks])


def parse_weather_request(weather_request: t.Dict) -> t.Dict:
    return {
        "request_id": weather_request["request_id"],
        "created_at": weather_request["created_at"],
        "status": weather_request["status"],
        "percentage_completed": weather_request["percentage_completed"],
        "data": weather_request["data"],
    }
