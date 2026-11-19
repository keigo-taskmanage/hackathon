import os
from sqlalchemy import URL


from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase


DATABASE_URL = URL.create(
    "mysql+asyncmy",
    username=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PWD"],
    database=os.environ["MYSQL_DATABASE"],
    query={"unix_socket": os.environ["MYSQL_SOCKET"], "charset": "utf8mb4"},
)

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
)


AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as db:
        yield db
