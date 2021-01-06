import os
from urllib import parse

# from arq.connections import RedisSettings

STRICT_DEV = os.getenv("STRICT_DEV", False)

# Maximum number of cities to request per API call
# E.g CHUNKS=2 -> https://api.openweathermap.org/data/2.5/group?id=city1,city2
CHUNKS = 20

# Open Weaether Map API Secret Key
API_KEY = os.getenv("API_OPEN_WEATHER_MAP_KEY", "secret_key")

# MONGODB
username = os.getenv("MONGO_ROOT_USER", "devuser")
password = os.getenv("MONGO_ROOT_PASS", "devuser")
hostname = os.getenv("MONGO_HOST", "localhost")
port = os.getenv("MONGO_PORT", 27017)
MONGODB_URL = f"mongodb://{username}:{password}@{hostname}:{port}"

# use mongodb without authentication when working on local machine
if STRICT_DEV == "true":
    MONGODB_URL = "mongodb://127.0.0.1/27017"

MAX_CONNECTIONS_COUNT = int(os.getenv("MAX_CONNECTIONS_COUNT", 10))
MIN_CONNECTIONS_COUNT = int(os.getenv("MIN_CONNECTIONS_COUNT", 10))


"""
# REDISARQ
REDIS_IP: str = os.getenv("REDIS_IP", "127.0.0.1")
REDIS_PORT: int = os.getenv("REDIS_PORT", 6379)
redis_settings = RedisSettings(host=REDIS_IP, port=REDIS_PORT)


# REDIS
CELERY_BROKER_URL = os.getenv("REDISSERVER", "redis://127.0.0.1:6379/0")
CELERY_RESULT_BACKEND = os.getenv("REDISSERVER", "redis://127.0.0.1:6379/0")
"""
