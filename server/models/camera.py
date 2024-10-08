from uuid import uuid4
from sqlalchemy import Column, String, Integer, Float, Enum
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from schema import CamType, Status
from .detected import detected
from db import Base

class Camera(Base):
    __tablename__ = "camera"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    cam_type = Column(Enum(CamType))
    ip_address = Column(String, index=True)
    username = Column(String, index=True)
    password = Column(String)
    port = Column(Integer, index=True)
    channel = Column(Integer,index=True)
    subtype = Column(Integer,index=True)
    latitude = Column(Float,index=True)
    longitude = Column(Float,index=True)
    azimuth = Column(Integer,index=True)
    status = Column(Enum(Status),index=True)
    thana = Column(String,index=True)

    criminals = relationship("Criminal", secondary=detected, back_populates="cameras")
    
    @hybrid_property
    def public_data(self):
        return {
            "id": self.id,
            "ipAddress": self.ip_address,
            "username": self.username,
            "password": self.password,
            "port": self.port,
            "channel":self.channel,
            "subtype":self.subtype,
            "latitude":self.latitude,
            "longitude":self.longitude,
            "azimuth":self.azimuth,
            "status":self.status,
            "thana":self.thana
        }