from typing import AsyncGenerator

from database import Session
from sqlalchemy.ext.asyncio import AsyncSession


async def get_session() -> AsyncGenerator:
    session: AsyncSession = Session()

    try:
        yield session
    finally:
        await session.close()
