from app.api.routes import status
from app.api.routes import odbc
from app.api.routes import atividades
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(status.router)
api_router.include_router(odbc.router)
api_router.include_router(atividades.router)