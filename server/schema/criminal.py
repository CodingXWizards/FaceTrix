from pydantic import BaseModel
from datetime import date, time
from uuid import UUID

from .camera import Camera

class CriminalSchema(BaseModel):
    criminalname: str
    crimes: str
    date: date
    time: time
    location: str
    cameras: list[UUID] | list[Camera]
    thana: str
    images: str

class CriminalResponse(CriminalSchema):
    id: UUID

    class Config:
        orm_mode = True