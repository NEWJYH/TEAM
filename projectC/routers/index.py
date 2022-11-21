from fastapi import APIRouter, Depends, status, HTTPException, Response , Request
import schemas, database, models
from sqlalchemy.orm import Session
from typing import List

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from datetime import date, timedelta
import random

router = APIRouter(
    prefix="/index",
)

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    today = date.today()
    defaultStart = today - timedelta(29)
    dayLabel = list(range(1, (today - defaultStart).days + 1))
    randomlist = [random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1),]
    return templates.TemplateResponse("main.j2", context={'request':request, 'today':today, 'defaultStart':defaultStart, 'dayLabel':dayLabel, 'randomlist':randomlist})



