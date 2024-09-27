from uuid import UUID
from pydantic import BaseModel
from enum import Enum

class CamType(Enum):
    RTSP = 'RTSP'
    IP = 'IP'

class Camera(BaseModel):
    ip_address: str
    cam_type: CamType
    username: str | None
    password: str | None
    port: int
    channel: int | None
    subtype: int | None
    latitude: float
    longitude: float
    azimuth: int
    status: str
    thana: str