from contextlib import asynccontextmanager

from fastapi import FastAPI

from model import db
from routers import b_owner, user_router, freelance_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.create_all()
    app.include_router(user_router)
    app.include_router(freelance_router)
    app.include_router(b_owner)
    yield


app = FastAPI(lifespan=lifespan)
