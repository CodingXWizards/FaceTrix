from uuid import UUID
from pydantic import BaseModel
from enum import Enum

class CamType(Enum):
    RTSP = 'RTSP'
    IP = 'IP'
class Status(Enum):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
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
    status: Status
    thana: str

class Search(BaseModel):
    lat: float
    lon: float
    radius: float