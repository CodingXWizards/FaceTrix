from uuid import uuid4
from sqlalchemy import Column, String, Date, Time, Integer
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from .detected import detected
from db import Base

class Criminal(Base):
    __tablename__ = "criminal"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    criminalname = Column(String,index=True)
    crimes = Column(String,index=True)
    date = Column(Date,index=True)
    time = Column(Time,index=True)
    location = Column(String,index=True)
    thana = Column(String,index=True)
    images = Column(String,index=True)

    cameras = relationship("Camera", secondary=detected, back_populates="criminals")

    @hybrid_property
    def public_data(self):
        return {
            "id": self.id,
            "criminalname": self.criminalname,
            "crimes": self.crimes,
            "date": self.date,
            "time": self.time,
            "location":self.location,
            "thana":self.thana,
            "images":self.images
        }