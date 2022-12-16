from loguru import logger
from pydantic import PostgresDsn
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from app.services import settings


pg_dsn: PostgresDsn = settings["DB_URI"]
engine = create_async_engine(pg_dsn, echo=True, future=True)


async def get_db():
    async_session = AsyncSession(engine, expire_on_commit=False)
    try:
        yield async_session
    except SQLAlchemyError as err:
        await async_session.rollback()
        logger.error(err)
        raise err

    await async_session.commit()
    await async_session.close()
