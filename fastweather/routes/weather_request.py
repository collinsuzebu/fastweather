from fastapi import APIRouter, BackgroundTasks, Path, status
from fastapi.encoders import jsonable_encoder

from fastweather.db.crud import retrieve_weather_request, add_weather_request
from fastweather.models.weather_request import WeatherRequestSchema
from fastweather.models.responses import MongoResponse, ErrorResponse
from fastweather.tasks import fetch_data_task

# from fastweather.celery.celery_app import celery

# from arq.connections import ArqRedis, create_pool
# from fastweather.config import redis_settings

router = APIRouter()


@router.post("/tasks")
async def weather_post(
    weather: WeatherRequestSchema, background_tasks: BackgroundTasks
):
    """Endpoint receives request id and Starts a new background task"""

    wr = jsonable_encoder(weather)
    new_wr = await add_weather_request(wr)
    background_tasks.add_task(fetch_data_task, new_wr["request_id"])
    return MongoResponse(new_wr, status_code=status.HTTP_202_ACCEPTED)


@router.get("/tasks/{request_id}")
async def weather_get(request_id: str = Path(...)):
    """Endpoint receives request id and retrieve a background task"""

    wr = await retrieve_weather_request(request_id)
    if wr:
        return MongoResponse(wr, status_code=status.HTTP_200_OK)
    return ErrorResponse(
        "Request ID '{}' does not exist".format(request_id), status.HTTP_404_NOT_FOUND
    )


# redis: ArqRedis = await create_pool(redis_settings)
# await redis.enqueue_job("fetch_data_task", new_wr['request_id'])
# task = celery.send_task('fetch_data_task', args=[new_wr['request_id'],])
# task = celery.send_task('fetch_dat', args=[new_wr['request_id'],])
