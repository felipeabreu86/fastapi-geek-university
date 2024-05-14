import json
from random import randint
from typing import Optional

from pydantic import BaseModel, field_validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

    @field_validator("titulo")
    def validar_titulo(cls, value: str):
        if len(value.split(" ")) < 3:
            raise ValueError("O título deve ter pelo menos 3 palavras.")

        if value.islower():
            raise ValueError("O título deve ser capitalizado.")

        return value

    @field_validator("aulas")
    def validar_aulas(cls, value: int):
        if value <= 12:
            raise ValueError("São necessárias mais de 12 aulas.")

        return value

    @field_validator("horas")
    def validar_horas(cls, value: int):
        if value <= 10:
            raise ValueError("São necessárias mais de 10 horas de aula.")

        return value


# Dados
cursos = []

for x in range(1, 11):
    cursos.append(Curso(id=x, titulo=f"Programação para Leigos {x}", aulas=randint(13, 25), horas=randint(11, 110)))


def fake_db() -> list[Curso]:
    try:
        print("Abrindo conexão com banco de dados...")
    finally:
        print("Fechando conexão com banco de dados...")
        return cursos
