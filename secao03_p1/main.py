"""
arquivo principal da API da seção 03

opções de inicialização do servidor: 
    python main.py
    uvicorn main:app --reload
    gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
"""

from typing import List, Optional

from fastapi import (
    Depends,
    FastAPI,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    status,
)
from helper import binarySearch
from models import Curso, fake_db

app = FastAPI(
    title="API de Cursos",
    version="0.0.1",
    description="Uma API para estudo do FastAPI",
)


# Métodos HTTP GET
@app.get(
    "/cursos",
    description="Retorna todos os cursos ou uma lista vazia",
    summary="Retorna todos os cursos",
    response_model=List[Curso],
    response_description="Cursos encontrados com sucesso",
    status_code=status.HTTP_200_OK,
)
async def get_cursos(cursos: list[Curso] = Depends(fake_db)) -> list[Curso]:
    return cursos


@app.get(
    "/cursos/{curso_id}",
    description="Retorna um curso pelo ID ou HTTP 404 Not Found",
    summary="Retorna um curso pelo ID",
    response_model=Curso,
    response_description="Curso encontrado com sucesso",
    status_code=status.HTTP_200_OK,
)
async def get_curso(
    curso_id: int = Path(title="ID do curso", description="Identificador do curso", gt=0),
    cursos: list[Curso] = Depends(fake_db),
) -> Curso:
    index: int = binarySearch(cursos, curso_id, match_by_obj_id=True)

    if index > -1:
        curso: Curso = cursos[index]
        return curso

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Curso não encontado.",
    )


# Métodos HTTP POST
@app.post(
    "/cursos",
    description="Cria um novo curso e retorna os dados criados",
    summary="Cria um novo curso",
    response_model=Curso,
    response_description="Curso criado com sucesso",
    status_code=status.HTTP_201_CREATED,
)
async def criar_curso(curso: Curso, cursos: list[Curso] = Depends(fake_db)) -> Curso:
    curso.id = len(cursos) + 1
    cursos.append(curso)
    return curso


# Métodos HTTP PUT
@app.put(
    "/cursos/{curso_id}",
    description="Atualiza um curso pelo ID",
    summary="Atualiza um curso",
    response_model=Curso,
    response_description="Curso atualizado com sucesso",
    status_code=status.HTTP_200_OK,
)
async def atualizar_curso(curso_id: int, curso: Curso, cursos: list[Curso] = Depends(fake_db)) -> Curso:
    index: int = binarySearch(cursos, curso_id, match_by_obj_id=True)

    if index > -1:
        curso.id = curso_id
        cursos[index] = curso
        return curso

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Curso não encontado.",
    )


# Métodos HTTP DELETE
@app.delete(
    "/cursos/{curso_id}",
    description="Deleta um curso pelo ID",
    summary="Deleta um curso",
    response_model=None,
    response_description="Curso deletado com sucesso",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def deletar_curso(curso_id: int, cursos: list[Curso] = Depends(fake_db)) -> Response:
    index: int = binarySearch(cursos, curso_id, match_by_obj_id=True)

    if index > -1:
        del cursos[index]
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Curso não encontado.",
    )


# Método para exemplificar o uso de Query Parameters
@app.get("/calculadora")
async def calcular(
    a: int = Query(default=None, gt=5),
    b: int = Query(default=None, gt=10),
    x_geek: str = Header(default=None),
    c: Optional[int] = Query(default=0),
) -> dict:
    soma = a + b + c
    print(f"X-GEEK: {x_geek}")
    return {"resultado": soma}


# Main
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
