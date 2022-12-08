from fastapi import FastAPI
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
app.include_router(live.router)

# t = schedule.BackgroundTasks()
# t.start()



# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=['http://127.0.0.1:8000'],
#     allow_methods=["*"],
#     allow_headers=["*"],
# ) 