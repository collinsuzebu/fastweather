import logging

from motor.motor_asyncio import AsyncIOMotorClient
from fastweather.config import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT
from .mongodb import db
import asyncio


async def connect_to_mongo():
    logging.info("Connecting to database...")
    db.client = AsyncIOMotorClient(
        str(MONGODB_URL),
        maxPoolSize=MAX_CONNECTIONS_COUNT,
        minPoolSize=MIN_CONNECTIONS_COUNT,
        io_loop=asyncio.get_event_loop(),
    )
    logging.info("Connected！")


async def close_mongo_connection():
    logging.info("Disconnecting from database...")
    db.client.close()
    logging.info("Disconnected！")
