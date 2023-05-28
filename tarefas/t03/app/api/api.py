from app.api.routes import status
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(status.router)