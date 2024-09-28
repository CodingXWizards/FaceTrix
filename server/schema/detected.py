from pydantic import BaseModel
from uuid import UUID

class Detected(BaseModel):
    criminal_id: UUID
    camera_id: UUID

    class Config:
        orm_mode = True