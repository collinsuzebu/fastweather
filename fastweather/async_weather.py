import typing as t
import time
import sys
import asyncio
import aiohttp

# from throttled import ThrottledClientSession
from .utils import extract_info
from .config import CHUNKS, API_KEY


async def get(session: aiohttp.ClientSession, cities: str, **kwargs) -> t.Dict:
    url = (
        f"https://api.openweathermap.org/data/2.5/group?&units=metric&"
        f"id={cities}&appid={API_KEY}"
    )

    async with session.request("GET", url=url, **kwargs) as resp:
        # resp.raise_for_status()
        return await resp.json()


async def multiple_weather_requests(
    cities: t.Generator,
    queue: asyncio.Queue,
    cities_per_request: int = CHUNKS,
    **kwargs,
) -> t.List:

    async with aiohttp.ClientSession() as session:
        state = 1
        tasks = [
            asyncio.create_task(get(session=session, cities=ctys, **kwargs))
            for ctys in cities
        ]
        for ti in asyncio.as_completed(tasks):
            await queue.put(state)
            await ti
            # await asyncio.sleep(5)

            state += 1

        results = [ti.result() for ti in tasks]

    await queue.put(None)
    return extract_info(results)
