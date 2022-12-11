from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from database import engine
import models
import os

from routers import graph, live, performance, perfect


app = FastAPI(
    # openapi.json 숨기기
    docs_url=None,
    redoc_url=None        
)

# DB
models.Base.metadata.create_all(engine)

# Static 
script_dir = os.path.dirname(__file__)
st_abs_file_path = os.path.join(script_dir, "static/")
app.mount("/static", StaticFiles(directory=st_abs_file_path), name="static")

# Router
app.include_router(graph.router)
app.include_router(live.router)
app.include_router(performance.router)
app.include_router(perfect.router)
