from fastapi import FastAPI
from routers import index
from fastapi.staticfiles import StaticFiles
from database import engine
# from starlette.middleware.cors import CORSMiddleware
import models

# import uvicorn

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     alloworigin=["*"]
    
# )

# DB
models.Base.metadata.create_all(engine)

# Static 
app.mount("/static", StaticFiles(directory="static") ,name="static")

# Router
app.include_router(index.router)


