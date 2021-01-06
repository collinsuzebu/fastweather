import motor.motor_asyncio
from fastweather.config import MONGODB_URL

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
database = client.weather_requests
weather_request_collection = database.get_collection("weather_requests_collection")
