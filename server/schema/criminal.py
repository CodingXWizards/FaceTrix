from pydantic import BaseModel
from datetime import date, time
from uuid import UUID

class CriminalSchema(BaseModel):
    criminalname: str
    crimes: str
    date: date
    time: time
    location: str
    cameraid: int
    thana: str
    images: str

class CriminalResponse(CriminalSchema):
    id: UUID

    class Config:
        orm_mode = True