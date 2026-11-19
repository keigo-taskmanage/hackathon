from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.database import Base, engine
from api.routers import chats, hello


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    yield

    await engine.dispose()


app = FastAPI(lifespan=lifespan)

app.include_router(chats.router)
app.include_router(hello.router)







