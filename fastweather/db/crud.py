import typing as t
from bson.objectid import ObjectId

from .mongodb_setup import weather_request_collection
from fastweather.models.weather_request import WeatherRequestSchema
from fastweather.utils import parse_weather_request


# Retrieve all weather request information in the database
async def retrieve_all_weather_requests(
    collection=weather_request_collection,
) -> t.List:
    weather_requests = []
    async for weather in collection.find():
        weather_requests.append(parse_weather_request(weather))
    return weather_requests


# Add a new weather request to db
async def add_weather_request(
    w_request_data: dict, collection=weather_request_collection
) -> t.Dict:
    weather_request = await collection.insert_one(w_request_data)
    new_request = await collection.find_one({"_id": weather_request.inserted_id})
    return parse_weather_request(new_request)


# Retrieve a weather_request
async def retrieve_weather_request(
    id: str, collection=weather_request_collection
) -> t.Optional[t.Dict]:
    weather_request = await collection.find_one({"request_id": id})
    if weather_request:
        return parse_weather_request(weather_request)
    return None


# Update a weather_request
async def update_weather_request(
    id: str, data: dict, collection=weather_request_collection
) -> bool:
    if len(data) < 1:
        return False

    weather_request = await collection.find_one({"request_id": id})
    if weather_request:
        updated_weather_req = await collection.update_one(
            {"request_id": id}, {"$set": data}
        )

        if updated_weather_req:
            return True
        return False
    return False


# Delete a weather request from the database
async def delete_weather_request(
    id: str, collection=weather_request_collection
) -> bool:
    weather_request = await collection.find_one({"request_id": id})
    if weather_request:
        await collection.delete_one({"request_id": id})
        return True
    return False
