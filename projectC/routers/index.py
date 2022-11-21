from fastapi import APIRouter, Depends, status, HTTPException, Response , Request
import schemas, database, models
from sqlalchemy.orm import Session
from typing import List

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse



router = APIRouter(
    prefix="/index",
)

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", context={'request':request})



