from uuid import uuid4
from sqlalchemy import Column, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.dialects.postgresql import UUID

from db import Base

class User(Base):
    __tablename__ = "camera"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    username = Column(String)
    ip_address = Column(String, index=True)
    password = Column(String)
    port = Column(int, index=True)
    channel = Column(int,index=True)
    subtype = Column(int,index=True)
    latitude = Column(float,index=True)
    longitute = Column(float,index=True)
    azimuth = Column(int,index=True)
    status = Column(String,index=True)
    thana = Column(String,index=True)

    @hybrid_property
    def public_data(self):
        return {
            "id": self.id,
            "username": self.username,
            "ipaddress": self.ipaddress,
            "password": self.password,
            "port": self.port,
            "channel":self.channel,
            "subtype":self.subtype,
            "latitude":self.latitude,
            "longitude":self.longitute,
            "azimuth":self.azimuth,
            "status":self.status,
            "thana":self.thana
        }