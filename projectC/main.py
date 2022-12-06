<<<<<<< HEAD
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends
from routers import index, CRUD, cv_live, live, video
=======
from fastapi import FastAPI
>>>>>>> 47e6a24627fed00bffa2a48d21ae6a456c7c033e
from fastapi.staticfiles import StaticFiles

from database import engine
from schedule import schedule
from routers import index, CRUD, live
import models

app = FastAPI()

# DB
models.Base.metadata.create_all(engine)

# Static 
app.mount("/static", StaticFiles(directory="static") , name="static")

# Router
app.include_router(index.router)
app.include_router(CRUD.router)
<<<<<<< HEAD
app.include_router(cv_live.router)
app.include_router(live.router)
app.include_router(video.router)
=======
app.include_router(live.router)
>>>>>>> 47e6a24627fed00bffa2a48d21ae6a456c7c033e

t = schedule.BackgroundTasks()
t.start()



# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=['http://127.0.0.1:8000'],
#     allow_methods=["*"],
#     allow_headers=["*"],
# ) 