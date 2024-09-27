from uuid import UUID
from pydantic import BaseModel

class Camera(BaseModel):
    ip_address: str
    username: str
    password: str
    port: int
    channel: int
    subtype: int
    latitude: float
    longitude: float
    azimuth: int
    status: str
    thana: str