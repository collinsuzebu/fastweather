import typing as t
import asyncio
from unittest.mock import patch, AsyncMock, MagicMock

import pytest

from tests.data import city_id_1, city_id_2
from fastweather import async_weather


@pytest.mark.asyncio
@pytest.mark.async_funcs
@patch("aiohttp.ClientSession.request")
async def test_multiple_request(mock_get, open_wm_response_data, get_response_data):
    mock_get.return_value.__aenter__.return_value.json = AsyncMock(
        side_effect=open_wm_response_data
    )
    mock_get.return_value.__aenter__.return_value.raise_for_status = MagicMock()

    cities = (city_id_1, city_id_2)
    queue = asyncio.Queue()
    result = await async_weather.multiple_weather_requests(cities, queue, 1)

    assert result == get_response_data["data"]


# @pytest.mark.asyncio
# @pytest.mark.async_funcs
# @patch('aiohttp.ClientSession.request')
# async def test_get_request(mock_get,):
#     result = await async_weather.get()
