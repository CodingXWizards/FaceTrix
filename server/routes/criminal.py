from fastapi import APIRouter, HTTPException, Request, UploadFile, File, Form
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Criminal
from schema import CriminalSchema, CriminalResponse
from datetime import date, time, datetime
import uuid
import json

router = APIRouter()

@router.post('/')
async def add_criminal(request: Request, metadata: str = Form(...), image: UploadFile = File(...)):
    try: 
        db: AsyncSession = request.state.db

        # Save the image
        image_name = f'{uuid.uuid4()}.jpg'
        file_location = f"static/images/{image_name}"
        with open(file_location, "wb+") as file_object:
            file_object.write(image.file.read())

        metadatadict = json.loads(metadata)
        data = CriminalSchema(**metadatadict)

        print(data.criminalname)
        new_criminal = Criminal(criminalname=data.criminalname, crimes=data.crimes, date=data.date, time=data.time, location=data.location, thana=data.thana, images=file_location)

        db.add(new_criminal)
        await db.commit()
        await db.refresh(new_criminal)
        return {"message": "success"}
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