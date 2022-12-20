from fastapi import APIRouter

from .auth import router as auth_router
from .movies import router as movies_router


router = APIRouter()
router.include_router(auth_router, prefix='/auth')
router.include_router(movies_router, prefix='/movies')
