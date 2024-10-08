from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from core.config import settings
from fastapi import HTTPException, Request

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(user_id, expires_delta: timedelta = None):
    to_encode = {"sub": str(user_id)}
    
    if expires_delta:
        expire = datetime.now() + expires_delta
    else: 
        expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload['sub']
    except JWTError:
        raise HTTPException(403, detail="Unauthorized")

# Helper function for authenticating users
async def authenticate_user(request: Request):
    token = request.cookies.get('access_token')
    if(token is None):
        raise HTTPException(status_code=403, detail="Unauthorized")
    
    user_id = verify_token(token)
    request.state.user_id = user_id