from enum import Enum
from uuid import UUID
from pydantic import BaseModel, EmailStr

class UserType(Enum):
    BASIC = 'BASIC'
    ADMIN = 'ADMIN'
    SUPER = 'SUPER'

class User(BaseModel):
    user_type: UserType
    name: str
    password: str
    email: EmailStr
    phone_number: str
    designation: str

class Login(BaseModel):
    email: EmailStr
    password: str