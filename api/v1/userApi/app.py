from fastapi import FastAPI
from .router import api_router


userApi = FastAPI()

userApi.include_router(api_router)