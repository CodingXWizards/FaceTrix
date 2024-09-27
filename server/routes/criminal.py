from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from typing import List
from datetime import date, time
from uuid import UUID

from db import get_db
from models.criminal import Criminal
from schema import CameraSchema  # Update this import

router = APIRouter()

class CriminalCreate(BaseModel):
    criminalname: str
    crimes: int
    date: date
    time: time
    location: str
    cameraid: int
    thana: str
    images: str

@router.post("/")
async def create_criminal(criminal: CriminalCreate, db: AsyncSession = Depends(get_db)):
    db_criminal = Criminal(**criminal.dict())
    db.add(db_criminal)
    await db.commit()
    await db.refresh(db_criminal)
    return db_criminal

@router.get("/", response_model=List[CameraSchema])
async def read_criminals(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    result = await db.execute(Criminal.select().offset(skip).limit(limit))
    criminals = result.scalars().all()
    return [criminal.public_data for criminal in criminals]

@router.get("/{criminal_id}", response_model=CameraSchema)
async def read_criminal(criminal_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(Criminal.select().filter(Criminal.id == criminal_id))
    criminal = result.scalars().first()
    if criminal is None:
        raise HTTPException(status_code=404, detail="Criminal not found")
    return criminal.public_data

@router.put("/{criminal_id}", response_model=CameraSchema)
async def update_criminal(criminal_id: UUID, criminal: CriminalCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(Criminal.select().filter(Criminal.id == criminal_id))
    db_criminal = result.scalars().first()
    if db_criminal is None:
        raise HTTPException(status_code=404, detail="Criminal not found")
    
    for key, value in criminal.dict().items():
        setattr(db_criminal, key, value)
    
    await db.commit()
    await db.refresh(db_criminal)
    return db_criminal.public_data

@router.delete("/{criminal_id}", response_model=CameraSchema)
async def delete_criminal(criminal_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(Criminal.select().filter(Criminal.id == criminal_id))
    criminal = result.scalars().first()
    if criminal is None:
        raise HTTPException(status_code=404, detail="Criminal not found")
    
    await db.delete(criminal)
    await db.commit()
    return criminal.public_data