from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from database import engine
from routers import index, live
import models
import os

app = FastAPI()

# # DB
models.Base.metadata.create_all(engine)

# Static 
script_dir = os.path.dirname(__file__)
st_abs_file_path = os.path.join(script_dir, "static/")
app.mount("/static", StaticFiles(directory=st_abs_file_path), name="static")

# Router
app.include_router(index.router)
app.include_router(live.router)