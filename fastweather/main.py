import asyncio

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from fastweather.routes.weather_request import router as weather_request_router
from fastweather.db.mongodb_utils import connect_to_mongo, close_mongo_connection


app = FastAPI(title="FastWeather", docs_url="/")

app.include_router(weather_request_router, tags=["Tasks"])
app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

# TODO request id must be unique
