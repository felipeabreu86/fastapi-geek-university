"""
arquivo principal da API da seção 02

opções de inicialização do servidor: 
    python main.py
    uvicorn main:app --reload
    gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def raiz():
    return {"msg": "FastAPI"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
