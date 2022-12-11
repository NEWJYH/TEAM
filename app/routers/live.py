from fastapi import APIRouter, Request, Depends
from fastapi import Request
from sqlalchemy.orm import Session
import database, schemas

from repository import live

router = APIRouter(
    prefix="/live",
    tags=['lives']
)

@router.get("/")
async def live_html(request:Request):
    return live.live_html(request)

@router.post('/post2')
async def live_minimap(form:schemas.MiniMapForm, db:Session=Depends(database.get_db)):
    return live.live_minimap(form, db)