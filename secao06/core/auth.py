from datetime import datetime, timedelta
from typing import List, Optional

from core.configs import settings
from core.security import verificar_senha
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from models.usuario_model import UsuarioModel
from pydantic import EmailStr
from pytz import timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

oauth2_schema = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/usuarios/login")


async def autenticar(email: EmailStr, senha: str, db: AsyncSession) -> Optional[UsuarioModel]:
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.email == email)
        result = await session.execute(query)
        usuario: UsuarioModel = result.scalars().unique().one_or_none()

        if not usuario:
            return None

        if not verificar_senha(senha, usuario.senha):
            return None

        return usuario


def criar_token_acesso(sub: str) -> str:
    """
    https://jwt.io
    """

    tz_sp = timezone("America/Sao_Paulo")
    tempo_vida = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    payload = {
        "type": "access_token",
        "exp": datetime.now(tz=tz_sp) + tempo_vida,
        "iat": datetime.now(tz=tz_sp),
        "sub": str(sub),
    }

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)
