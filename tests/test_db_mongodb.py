import motor.motor_asyncio
import pytest
import pymongo.errors

from unittest.mock import patch, AsyncMock, MagicMock

from fastweather.db import crud


@pytest.fixture
def get_mongodb_db():
    async def _get_mongodb_db():
        client = motor.motor_asyncio.AsyncIOMotorClient(
            "mongodb://localhost:27017", serverSelectionTimeoutMS=100
        )

        try:
            await client.server_info()
        except pymongo.errors.ServerSelectionTimeoutError:
            pytest.skip("MongoDB is not available", allow_module_level=True)

        db = client["test_weather_requests"]
        collection = db["test_weather_requests_collection"]

        yield collection

        await collection.drop()
        client.close()

    return _get_mongodb_db


@pytest.fixture
async def mongodb_db_collection(get_mongodb_db):
    async for c in get_mongodb_db():
        yield c


@pytest.mark.asyncio
async def test_crud_operations(mongodb_db_collection):
    collection = mongodb_db_collection

    # Adding weather request
    wr_data = {
        "request_id": "1",
        "created_at": "2020-12-05T13:18:32.222557",
        "status": "PENDING",
        "percentage_completed": "0%",
        "data": [],
    }
    wr_data_2 = {**wr_data, "request_id": "2"}

    added_wr = await crud.add_weather_request(wr_data, collection=collection)
    added_wr_2 = await crud.add_weather_request(wr_data_2, collection=collection)

    assert added_wr["request_id"] == "1"
    assert added_wr_2["request_id"] == "2"

    # Retrieving single weather_requests data
    ret_wr = await crud.retrieve_weather_request("1", collection=collection)
    assert ret_wr["request_id"] == "1"

    # Updating weather request data
    wr_upd_data = {"status": "COMPLETE", "percentage_completed": "100%"}
    upd_wr = await crud.update_weather_request("1", wr_upd_data, collection=collection)
    upd_wr_2 = await crud.update_weather_request("1", {}, collection=collection)
    upd_wr_3 = await crud.update_weather_request(
        "3", wr_upd_data, collection=collection
    )

    assert upd_wr == True
    assert upd_wr_2 == False
    assert upd_wr_3 == False

    # Retrieving all weather_requests data
    all_wr = await crud.retrieve_all_weather_requests(collection=collection)
    assert len(all_wr) == 2

    # Deleting weather request data
    del_wr = await crud.delete_weather_request("1", collection=collection)
    del_wr_2 = await crud.delete_weather_request("3", collection=collection)
    assert del_wr == True
    assert del_wr_2 == False
