from fastapi import FastAPI
from routers import index
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Router
app.include_router(index.router)
app.mount("/static", StaticFiles(directory="static"), name="static")