from fastapi import FastAPI, Depends
from routers import index, CRUD
from fastapi.staticfiles import StaticFiles
from database import engine
import models

from schedule import schedule
from routers.CRUD import post_Auto_Manage
import database 
from sqlalchemy.orm import Session

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
app.include_router(CRUD.router)

# schedule 
t = schedule.BackgroundTasks()
t.start()