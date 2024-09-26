from uuid import UUID
from pydantic import BaseModel

class Camera(BaseModel):
    id: UUID
    username: str
    ip_address: str
    password: str
    port: int
    channel: str
    subtype: str
    latitude: float
    longitute: float
    azimuth: int
    status: str
    thana: str