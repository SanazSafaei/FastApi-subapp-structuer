from fastapi import APIRouter

from .sample.views import router as sample_router


api_router = APIRouter()

api_router.include_router(sample_router, prefix="/sample")
