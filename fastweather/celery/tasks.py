import asyncio

from fastweather.async_weather import multiple_weather_requests, CHUNKS
from fastweather.utils import load_cities_in_chunks, get_current_percentage
from fastweather.db.crud import retrieve_weather_request, update_weather_request
from .celery_app import celery


@celery.task(name="fetch_dat")
def fetch_dat(request_id):
    print("FETCH--FETCH", request_id)


@celery.task(name="fetch_data_task")
async def fetch_data_task(request_id):
    queue = asyncio.Queue()
    await update_weather_request(request_id, {"status": "PROGRESS"})

    cities = load_cities_in_chunks("cities_id.txt")
    n_cities = len(list(load_cities_in_chunks("cities_id.txt")))
    task = asyncio.ensure_future(multiple_weather_requests(cities, queue, CHUNKS))

    while pct_completed := await queue.get():
        pct = f"{get_current_percentage(pct_completed, n_cities)}%"
        await update_weather_request(request_id, {"percentage_completed": pct})

    await update_weather_request(request_id, {"data": task.result()})
    await update_weather_request(request_id, {"status": "COMPLETE"})
