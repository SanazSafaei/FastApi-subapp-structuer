from fastapi import APIRouter

from .sample.views import router


api_router = APIRouter()

api_router.include_router(router, prefix="/sample")
