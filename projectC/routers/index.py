from fastapi import APIRouter, Depends, status, HTTPException, Response , Request
import schemas, database, models
from sqlalchemy.orm import Session
from typing import List

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from datetime import date, timedelta
import random

router = APIRouter(
    prefix="/graph",
)

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    today = date.today()
    defaultStart = today - timedelta(29)
    randomlist = [random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1),]
    return templates.TemplateResponse("graph.j2", context={'request':request, 'today':today, 'defaultStart':defaultStart, 'randomlist':randomlist})


