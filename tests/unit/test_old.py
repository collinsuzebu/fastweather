import json
import contextlib
from dataclasses import dataclass
import aiohttp

# @pytest.mark.asyncio
# @pytest.mark.integration_test
# @patch('fastweather.async_weather.get.ClientSession.get')
# async def test_get_request(mock_get, response_data):
#     mock_get.return_value.__aenter__.return_value.json = CoroutineMock(
#         side_effect=response_data
#     )
#
#     cities = ("3443207","3442546")
#     queue = asyncio.Queue()
#     result = await async_weather.multiple_weather_requests(cities, queue, 1)
#
#     assert result == response_data['data']


# @dataclass
# class FakeAIOHttpResponse:
#     body: str
#     status: int = 200
#
#     async def json(self) -> t.Any:
#         return json.loads(self.body)
#
#
# @dataclass
# class FakeAIOHttpClient:
#     responses: t.Dict[str, str]
#
#     @contextlib.asynccontextmanager
#     async def get(
#         self, url: str, headers: t.Optional[t.Dict[str, str]] = None
#     ) -> t.AsyncIterator[FakeAIOHttpResponse]:
#         if url in self.responses:
#             yield FakeAIOHttpResponse(body=self.responses[url])
#         else:
#             yield FakeAIOHttpResponse(body="", status=404)
#
#
#
#
#
#
# @pytest.fixture
# def mockclient(data) -> FakeAIOHttpClient:
#     return FakeAIOHttpClient(
#         {
#             "http://localhost/tasks": json.dumps(data),
#             "http://localhost/tasks/task_id": json.dumps(
#                 {
#                   "request_id": "1",
#                   "created_at": "2020-12-05T07:59:01.986863",
#                   "status": "COMPLETE",
#                   "percentage_completed": "100.0%",
#                   "data": [
#                     {
#                       "city_id": 3439525,
#                       "temperature": 31.67,
#                       "humidity": 27
#                     }]
#                 }
#             )
#         }
#     )
#
#
# class TestCreateNewRequest:
#     @pytest.fixture()
#     def patch_aiohttp(self, mockclient):
#         with patch("aiohttp.ClientSession") as ClientSession:
#             ClientSession.return_value.__aenter__.return_value = mockclient
#             yield ClientSession
#
#     @pytest.mark.asyncio
#     async def test_get(self, patch_aiohttp, cities="3210,1234"):
#         result = await async_weather.get(patch_aiohttp, cities)
#
#         assert result == None


# @pytest.mark.integration_test
# @pytest.mark.asyncio
# async def test_get():
#     async with aiohttp.ClientSession() as session:
#         result = await async_weather.get(session=session, cities="3443207,3442546")
#     assert result['cnt'] == 2
#
#
# @pytest.mark.integration_test
# @pytest.mark.asyncio
# async def test_multiple_weather_requests():
#     cities = ("3443207","3442546")
#     queue = asyncio.Queue()
#     result = await async_weather.multiple_weather_requests(cities, queue, 1)
#
#     assert len(result) == 2


# async def test_multiple_weather_requests(aiohttp_client: Any) -> None:
#     async def handler(request):
#         data = await request.post()
#         return web.json_response(dict(data))
#
#
#     app = web.Application()
#     app.router.add_post("/", handler)
#     client = await aiohttp_client(app)
#
#     form = aiohttp.FormData()
#     form.add_field("request_id", "1", content_transfer_encoding="base64")
#
#     resp = await client.post("/", data=form)
#     assert 202 == resp.status
#     content = await resp.json()
#     assert content == {
#       "request_id": "2",
#       "created_at": "2020-12-06T18:55:39.588111",
#       "status": "PENDING",
#       "percentage_completed": "0%",
#       "data": "null"
#     }
#     resp.close()


# @pytest.mark.asyncio
# async def test_get():
#     app = aiohttp.web.Application()
#     async def handler(request):
#         return aiohttp.web.Response(text=SAMPLE_RESPONSE_FROM_OPENWEATHERAPI)
#     app.router.add_route('get', '/random/url')
#
#     server = aiohttp.test_utils.TestServer(app):
#     async with server:


# @pytest.mark.asyncio
# @pytest.mark.integration_test
# async def test_get_request():
#     """Test get"""
#     session = Mock()
#     mock_response = Mock()
#     mock_response.status = 200
#     session.get.return_value = asyncio.Future()
#     session.get.return_value.set_result(mock_response)
#
#     result = await async_weather.get(session, "3442546,3443207")
#
#     assert result == mock_response
