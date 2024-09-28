import math
from fastapi import APIRouter, HTTPException, Response, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from shapely.geometry import Point, Polygon

from models import Camera
from schema import CameraSchema, SearchSchema

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
            cam_type=data.cam_type,
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

def calculate_arc_points(lat, lon, azimuth, radius=100, num_points=100):
    points = []
    start_angle = azimuth - 60
    end_angle = azimuth + 60
    angle_step = (end_angle - start_angle) / num_points
    for i in range(num_points + 1):
        angle = start_angle + i * angle_step
        angle_rad = math.radians(angle)
        point_lat = lat + (radius * math.cos(angle_rad))
        point_lon = lon + (radius * math.sin(angle_rad))
        points.append((point_lon, point_lat))
    points.append((lon, lat))
    points.append((points[0][0], points[0][1]))
    return points

@router.post("/search-azimuth")
async def search_azimuth(data:SearchSchema, request: Request):
    db: AsyncSession = request.state.db
    lat = data.lat
    lon = data.lon
    radius = data.radius

    try:
        # Fetch all cameras from the database
        result = await db.execute(select(Camera))
        cameras = result.scalars().all()

        # Point to search
        search_point = Point(lon, lat)

        # List to store matching camera IDs
        matching_cameras = []

        for camera in cameras:
            arc_points = calculate_arc_points(camera.latitude, camera.longitude, camera.azimuth, radius=radius)
            polygon = Polygon(arc_points)

            if polygon.contains(search_point):
                matching_cameras.append(camera.public_data)  # Convert UUID to string

        return {"matching_camera_ids": matching_cameras}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")