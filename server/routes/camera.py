from fastapi import APIRouter, HTTPException, Response, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models import Camera
from schema import CameraSchema

router = APIRouter()

@router.get('/')
async def get_cameras(request: Request):
    db: AsyncSession = request.state.db
    all_camera = await db.execute(select(Camera))
    all_camera = all_camera.scalars().all()

    if all_camera is None:
        raise HTTPException(status_code=404, detail="No Camera found")

    return [camera.public_data for camera in all_camera]

@router.get('/{id}')
async def get_camera(id:str, request: Request):
    db: AsyncSession = request.state.db
    camera = await db.execute(select(Camera).where(Camera.id == id))
    camera = camera.scalars().first()

    if camera is None:
        raise HTTPException(status_code=404, detail="No Camera found")

    return camera

@router.post('/')
async def get_camera(data: CameraSchema, request: Request):
    try: 
        db: AsyncSession = request.state.db

        new_camera = Camera(username=data.username,
            password=data.password,
            ip_address=data.ip_address,
            port=data.port,
            channel=data.channel,
            subtype=data.subtype,
            latitude=data.latitude,
            longitude=data.longitude,
            azimuth=data.azimuth,
            status=data.status,
            thana=data.thana)

        db.add(new_camera)
        
        await db.commit()
        await db.refresh(new_camera)
        return new_camera
    except Exception as e: 
        raise HTTPException(500, detail=f"Interal Server Error: {str(e)}")