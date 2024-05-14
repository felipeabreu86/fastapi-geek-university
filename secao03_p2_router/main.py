"""
arquivo principal da API da seção 03 - Router

opções de inicialização do servidor: 
    python main.py
    uvicorn main:app --reload
    gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
"""

from fastapi import FastAPI
from routes import curso_router, usuario_router

app = FastAPI()
app.include_router(curso_router.router, tags=["cursos"])
app.include_router(usuario_router.router, tags=["usuários"])

# Main
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
