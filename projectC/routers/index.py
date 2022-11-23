from fastapi import APIRouter, Depends, status, HTTPException, Response , Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from repository import index
from typing import List

from fastapi import  Request
import schemas
from LOG import log

import random
from datetime import date, timedelta

router = APIRouter(
    prefix="/graph",
)

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def get_test(request: Request):
    context = index.get_test()
    context['request'] = request
    log.infod(context)
    today = date.today()
    defaultStart = today - timedelta(29)
    randomlist = [random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1), random.choices(range(100, 200), k=(today - defaultStart).days+1),]
    return templates.TemplateResponse("graph.j2", context={'request':request, 'today':today, 'defaultStart':defaultStart, 'randomlist':randomlist})

@router.post('/post', response_class=HTMLResponse, status_code=status.HTTP_202_ACCEPTED)
def post(request: schemas.index_post):
    # context = {}
    # request.defaultStart = request.today-timedelta(29)
    # randomlist = [random.choices(range(100, 200), k=(request.today - request.defaultStart).days+1), random.choices(range(100, 200), k=(request.today - request.defaultStart).days+1), random.choices(range(100, 200), k=(request.today - request.defaultStart).days+1), random.choices(range(100, 200), k=(request.today - request.defaultStart).days+1), random.choices(range(100, 200), k=(request.today - request.defaultStart).days+1)]
    # false = False
    # test = [{
    #     'data': randomlist[0],
    #     'label': "1번 방",
    #     'borderColor': "#3e95cd",
    #     'fill': false
    # }, {
    #     'data': randomlist[1],
    #     'label': "2번 방",
    #     'borderColor': "#8e5ea2",
    #     'fill': false
    # }, {
    #     'data': randomlist[2],
    #     'label': "3번 방",
    #     'borderColor': "#3cba9f",
    #     'fill': false
    # }, {
    #     'data': randomlist[3],
    #     'label': "4번 방",
    #     'borderColor': "#e8c3b9",
    #     'fill': false
    # }, {
    #     'data': randomlist[4],
    #     'label': "5번 방",
    #     'borderColor': "#c45850",
    #     'fill': false
    # }
    # ]
    # context['today'] = request.today
    # context['defaultStart'] = request.defaultStart
    # context['randomlist'] = randomlist
    # context['request'] = request
    return request.json()



