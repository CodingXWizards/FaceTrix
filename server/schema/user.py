from enum import Enum
from uuid import UUID
from pydantic import BaseModel, EmailStr

class UserType(Enum):
    BASIC = 'BASIC'
    ADMIN = 'ADMIN'
    SUPER = 'SUPER'

class User(BaseModel):
    id: UUID
    type: UserType
    name: str
    email: EmailStr
    phone_number: str
    designation: str

class Login(BaseModel):
    email: EmailStr | None
    phone_number: str | None
    password: str