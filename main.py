from contextlib import asynccontextmanager

from fastapi import FastAPI

from model import db
from routers import b_owner, user_router, freelance_router, education


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.create_all()
    app.include_router(user_router)
    app.include_router(freelance_router)
    app.include_router(b_owner)
    app.include_router(education)
    yield


app = FastAPI(
    title="Freelance app",
    description="Description",
    version="1.0.0",
    docs_url="/",
    openapi_url="/freelance-openapi.json",
    lifespan=lifespan
)
