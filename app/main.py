from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from builtins import Exception
from app.database import Database
from app.dependencies import get_settings
from app.routers import user_routes
from app.utils.api_description import getDescription
from app.utils.minio_client import ensure_bucket_exists  # ← new import

app = FastAPI(
    title="User Management",
    description=getDescription(),
    version="0.0.1",
    contact={
        "name": "API Support",
        "url": "http://www.example.com/support",
        "email": "support@example.com",
    },
    license_info={"name": "MIT", "url": "https://opensource.org/licenses/MIT"},
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # allow all origins
    allow_credentials=True,    # allow cookies, auth headers
    allow_methods=["*"],       # allow all HTTP methods
    allow_headers=["*"],       # allow all headers
)

@app.on_event("startup")
async def startup_event():
    # 1) Initialize DB
    settings = get_settings()
    Database.initialize(settings.database_url, settings.debug)

    # 2) Ensure MinIO bucket exists before serving any upload requests
    ensure_bucket_exists(settings.MINIO_BUCKET_NAME)

@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    # Generic 500 error handler
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred."},
    )

# Mount your user routes
app.include_router(user_routes.router)
