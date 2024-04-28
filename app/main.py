from fastapi import FastAPI
from .routers import results, sensors, changes
from contextlib import asynccontextmanager
from .database.database import create_db

@asynccontextmanager
async def lifespan(app: FastAPI):
  create_db()
  yield

app = FastAPI(lifespan=lifespan)

app.include_router(results.router)
app.include_router(sensors.router)
app.include_router(changes.router)