from fastapi import APIRouter, Depends, status, HTTPException, Response, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from sqlalchemy.orm import Session
from sqlalchemy import and_ 



import models
import database, schemas

from datetime import date, timedelta
import random
import json


router = APIRouter(
    prefix="/graph"
)

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def get_test(request:Request, db:Session=Depends(database.get_db)):
    today = date.today()
    defaultStart = today - timedelta(29)
    randomlist = [random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1)]
    testDataset = [{
        'label': "1",
        'borderColor': "#3e95cd",
    }, {
        'label': "2",
        'borderColor': "#8e5ea2",
    }, {
        'label': "3",
        'borderColor': "#3cba9f",
    }, {
        'label': "4",
        'borderColor': "#e8c3b9",
    }
    ]
    
    testDataset = json.dumps(testDataset)
    context = {'today':today, 'defaultStart':defaultStart,'randomlist':randomlist, 'testDataset':testDataset} 
    context['request'] = request
    

    return templates.TemplateResponse("graph.j2", context)


@router.post("/", response_class=HTMLResponse)
def get_test(request:Request, data:schemas.Form, db:Session=Depends(database.get_db)):
    print(data.startday)
    print(data.endday)
    print(data.cctvnum)
    today = date.today()
    defaultStart = today - timedelta(29)
    randomlist = [random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1)]
    testDataset = [{
        'label': "1",
        'borderColor': "#3e95cd",
    }, {
        'label': "2",
        'borderColor': "#8e5ea2",
    }, {
        'label': "3",
        'borderColor': "#3cba9f",
    }, {
        'label': "4",
        'borderColor': "#e8c3b9",
    }
    ]
    
    testDataset = json.dumps(testDataset)
    context = {'today':today, 'defaultStart':defaultStart,'randomlist':randomlist, 'testDataset':testDataset} 
    context['request'] = request
    

    return templates.TemplateResponse("graph.j2", context)


