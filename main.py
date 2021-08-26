from fastapi import FastAPI
from core import settings
from api.v1.userApi.app import userApi
from api.v1.adminApi.app import adminApi
from starlette.middleware.cors import CORSMiddleware
from starlette.datastructures import CommaSeparatedStrings
import uvicorn
from fastapi.responses import ORJSONResponse


if settings.DEBUG:
    app = FastAPI(default_response_class=ORJSONResponse)
else:
    app = FastAPI(default_response_class=ORJSONResponse, redoc_url=None, docs_url=None)


# middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=CommaSeparatedStrings(settings.ALLOWED_HOSTS),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# mount subapis
app.mount("/user", userApi)
app.mount("/admin", adminApi)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
