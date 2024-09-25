from uuid import uuid4
from sqlalchemy import Column, String, Numeric
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.dialects.postgresql import UUID


from db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    phone_number = Column(Numeric, unique=True, index=True)
    designation = Column(String)

    @hybrid_property
    def public_data(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone_number": self.phone_number,
            "designation": self.designation
        }