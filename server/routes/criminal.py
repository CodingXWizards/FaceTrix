from fastapi import APIRouter, HTTPException, Request, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Criminal
from schema import CriminalSchema, CriminalResponse
from datetime import date, time
import uuid
import os

router = APIRouter()

@router.post('/', response_model=CriminalResponse)
async def add_criminal(request: Request, 
                       criminal: CriminalSchema,
                       image: UploadFile = File(...)):
    try: 
        db: AsyncSession = request.state.db

        # Save the image
        file_location = f"static/images/{uuid.uuid4()}.jpg"
        with open(file_location, "wb+") as file_object:
            file_object.write(image.file.read())

        new_criminal = Criminal(**criminal.dict(), images=file_location)

        db.add(new_criminal)
        await db.commit()
        await db.refresh(new_criminal)
        return CriminalResponse.from_orm(new_criminal)
    except Exception as e: 
        raise HTTPException(500, detail=f"Internal Server Error: {str(e)}")

@router.get('/', response_model=list[CriminalResponse])
async def get_criminals(request: Request):
    db: AsyncSession = request.state.db
    result = await db.execute(select(Criminal))
    criminals = result.scalars().all()
    return [CriminalResponse.from_orm(criminal) for criminal in criminals]

@router.get('/{id}', response_model=CriminalResponse)
async def get_criminal(id: uuid.UUID, request: Request):
    db: AsyncSession = request.state.db
    result = await db.execute(select(Criminal).where(Criminal.id == id))
    criminal = result.scalars().first()
    if criminal is None:
        raise HTTPException(status_code=404, detail="Criminal not found")
    return CriminalResponse.from_orm(criminal)