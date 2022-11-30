from fastapi import APIRouter, Depends, status, HTTPException, Response, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from sqlalchemy.orm import Session
from sqlalchemy import and_ 



import models
import database, schemas

from datetime import date, timedelta
import random
import json


import json

from pydantic import BaseModel

router = APIRouter(
    prefix="/live"
)

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def get_test(request: Request):
    context = {}
    context['request'] = request
    return templates.TemplateResponse("live.j2", context)