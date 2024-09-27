from fastapi import APIRouter, Depends

from .auth import router as auth_router
from .user import router as user_router
from .camera import router as camera_router
from .criminal import router as criminals_router  # Import the new criminals router

from utils.security import authenticate_user

router = APIRouter()

router.include_router(auth_router, prefix="/auth")
router.include_router(user_router, prefix='/user', dependencies=[Depends(authenticate_user)])
router.include_router(camera_router, prefix='/camera', dependencies=[Depends(authenticate_user)])
router.include_router(criminals_router, prefix='/criminals', dependencies=[Depends(authenticate_user)])  # Include the new criminals router