from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Camera
from schema import CamType
from db import get_db
import cv2
import numpy as np
import face_recognition
import asyncio
import time

router = APIRouter()

async def get_camera_url(db: AsyncSession, camera_id: str):
    result = await db.execute(select(Camera).where(Camera.id == camera_id))
    camera = result.scalars().first()
    if not camera:
        raise HTTPException(status_code=404, detail=f"Camera with id {camera_id} not found")
    
    if camera.cam_type == CamType.IP:
        return f"https://{camera.ip_address}:{camera.port}"
    elif camera.cam_type == CamType.RTSP:
        return f"rtsp://{camera.username}:{camera.password}@{camera.ip_address}:{camera.port}/cam/realmonitor?channel={camera.channel}&subtype={camera.subtype}"
    else:
        raise HTTPException(status_code=400, detail=f"Unsupported camera type: {camera.cam_type}")

async def process_camera(camera_url: str, input_encoding, camera_id: str):
    cap = cv2.VideoCapture(camera_url)
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        # Resize frame to speed up face recognition
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces([input_encoding], face_encoding)
            if matches[0]:
                # Scale back up face locations
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Encode frame as JPEG
                _, buffer = cv2.imencode('.jpg', frame)
                jpg_as_text = buffer.tobytes()

                yield {
                    "camera_id": camera_id,
                    "time": time.time(),
                    "frame": jpg_as_text,
                    "bounding_box": {
                        "top": top,
                        "right": right,
                        "bottom": bottom,
                        "left": left
                    }
                }

        await asyncio.sleep(0.1)  # To prevent the loop from running too fast

    cap.release()

@router.post("/cctv")
async def cctv_tracking(image: UploadFile = File(...), camera_ids: list[str] = [], db: AsyncSession = Depends(get_db)):
    # Read and encode the input image
    contents = await image.read()
    nparr = np.fromstring(contents, np.uint8)
    input_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    input_encoding = face_recognition.face_encodings(input_image)[0]

    # Get camera URLs
    camera_urls = []
    for camera_id in camera_ids:
        url = await get_camera_url(db, camera_id)
        camera_urls.append((camera_id, url))

    # Process cameras
    async def process_all_cameras():
        tasks = [process_camera(url, input_encoding, camera_id) for camera_id, url in camera_urls]
        async for result in asyncio.as_completed(tasks):
            yield result

    return process_all_cameras()