from fastapi import APIRouter, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from models import User

router = APIRouter()

@router.get("/")
async def get_user(request: Request):
    db: AsyncSession = request.state.db
    user_id = request.state.user_id
    
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    user_data = {
        "id": user.id,
        "name": user.name,
        "userType": user.user_type,
        "email": user.email,
        "phoneNumber": user.phone_number,
        "designation": user.designation,
    }
    return {"user": user_data}

@router.get("/all")
async def get_user(request: Request):
    db: AsyncSession = request.state.db
    
    try:
        result = await db.execute(select(User).options(selectinload(User.workspaces)))
        users = result.scalars().all()
        return [user.public_data for user in users]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occured during fetching: {str(e)}")