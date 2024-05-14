from endpoints import curso
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(curso.router, prefix="/cursos", tags=["cursos"])


# /api/v1/cursos
