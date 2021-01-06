from typing import Optional, Dict, List
from datetime import datetime
from pydantic import BaseModel, Field


class WeatherRequestSchema(BaseModel):
    request_id: str = Field(...)
    created_at: datetime = datetime.now()
    status: str = "PENDING"
    percentage_completed: str = "0%"
    data: List[Dict[str, float]] = list()

    class Config:
        schema_extra = {
            "example": {
                "request_id": "1",
            }
        }


class UpdateWeatherRequestModel(BaseModel):
    request_id: str
    created_at: datetime
    status: Optional[str]
    percentage_completed: Optional[str]
    data: Optional[List[Dict[str, float]]]

    class Config:
        schema_extra = {
            "example": {
                "request_id": "1",
                "created_at": "2020-12-05T13:18:32.222557",
                "status": "COMPLETE",
                "percentage_completed": "100%",
                "data": [
                    {"city_id": 3439525, "temperature": 22.78, "humidity": 58},
                    {"city_id": 3439781, "temperature": 19.53, "humidity": 56},
                ],
            }
        }
