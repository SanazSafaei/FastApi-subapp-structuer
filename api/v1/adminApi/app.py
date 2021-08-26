from fastapi import FastAPI
from .router import api_router


adminApi = FastAPI()

adminApi.include_router(api_router)