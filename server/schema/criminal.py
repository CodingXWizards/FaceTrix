from uuid import UUID
from pydantic import BaseModel
from datetime import date, time
class Camera(BaseModel):
    id: UUID
    criminalname: str
    crimes: str
    date: date
    time: time
    location: str
    cameraid: int
    thana: str
    images: str
