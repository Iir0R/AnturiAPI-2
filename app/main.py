from fastapi import FastAPI
from .routers import results, sensors, changes
from contextlib import asynccontextmanager
from .database.database import create_db
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
  create_db()
  yield

app = FastAPI(lifespan=lifespan)

origins = ['*']

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*']
)

app.include_router(results.router)
app.include_router(sensors.router)
app.include_router(changes.router)