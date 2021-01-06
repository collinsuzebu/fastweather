from fastapi import HTTPException
from fastapi.responses import Response
from bson.json_util import dumps


class MongoResponse(Response):
    def __init__(self, content, *args, **kwargs):
        super().__init__(
            content=dumps(content),
            media_type="application/json",
            *args,
            **kwargs,
        )


def ErrorResponse(message, code):
    raise HTTPException(detail=message, status_code=code)
