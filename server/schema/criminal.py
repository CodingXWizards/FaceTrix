from pydantic import BaseModel
from datetime import date, time
from uuid import UUID

class Camera(BaseModel):
    id: UUID
    criminalname: str
    crimes: int
    date: date
    time: time
    location: str
    cameraid: int
    thana: str
    images: str

    class Config:
        orm_mode = True