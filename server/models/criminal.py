from uuid import uuid4
from sqlalchemy import Column, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.dialects.postgresql import UUID

from db import Base

class User(Base):
    __tablename__ = "criminal"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    criminalname = Column(String,index=True)
    crimes = Column(int,index=True)
    date = Column(date,index=True)
    time=Column(time,index=True)
    location = Column(String,index=True)
    cameraid=Column(int,index=True)
    thana = Column(String,index=True)
    images=Column(Text,index=True)

    @hybrid_property
    def public_data(self):
        return {
            "id": self.id,
            "criminalname": self.criminalname,
            "crimes": self.crimes,
            "date": self.date,
            "time": self.time,
            "location":self.location,
            "cameraid":self.cameraid,
            "thana":self.thana,
            "images":self.images
        }