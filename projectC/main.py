from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from database import engine
from routers import index, live
import models

app = FastAPI()

# DB
# models.Base.metadata.create_all(engine)

# Static 
app.mount("/static", StaticFiles(directory="static") , name="static")

# Router
app.include_router(index.router)
app.include_router(live.router)