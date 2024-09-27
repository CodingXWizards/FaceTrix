import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from routes import criminal

from middleware.db_session_middleware import DBSessionMiddleware
from db import engine, Base
from routes import router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(fastapi: FastAPI):
    print("Connecting to PostgreSQL...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        logger.info("Connected to PostgreSQL")
    yield

app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(DBSessionMiddleware)

app.include_router(router, prefix='/api')

app.include_router(criminal.router, prefix='/api')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0")