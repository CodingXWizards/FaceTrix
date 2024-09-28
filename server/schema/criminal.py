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
    thana: str

    class Config:
        from_attributes=True
class CriminalResponse(CriminalSchema):
    id: UUID
