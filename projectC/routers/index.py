from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from sqlalchemy.orm import Session
from sqlalchemy import and_

import models
import database, schemas

import json

import json

router = APIRouter(
    prefix="/graph"
)

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def get_test(request: Request):
    print('get 호출')
    context = {}
    context['request'] = request
    return templates.TemplateResponse("graph.j2", context)



@router.post('/post')
def get_test(form: schemas.Form, db:Session=Depends(database.get_db)):
    print('post')

    formtype = form.formtype
    startday = form.startday
    endday = form.endday
    cctvnum = form.cctvnum
    starttime = None
    endtime = None
    if formtype == 0:
        print('일 검색')
    else:
        print('시간 검색')
        starttime = form.starttime
        endtime = form.endtime

    # 시간 검색일 경우
    if starttime:
        startidx = db.query(models.Manage).filter(
                                                    and_(models.Manage.time.contains(startday)),
                                                    and_(models.Manage.distance_hour != None) 
                                                    ).first().idx
        endidx = db.query(models.Manage).filter(
                                                and_(models.Manage.time.contains(endday)),
                                                and_(models.Manage.distance_hour != None) 
                                                ).order_by(models.Manage.idx.desc()).first().idx
        manage = db.query(models.Manage).filter(
                                                and_(models.Manage.idx >= startidx),
                                                and_(models.Manage.idx <= endidx), 
                                                and_(models.Manage.distance_hour != None),
                                                ).all()
        dataset = {'data':{}}
        time_table = [x for x in range(int(starttime[0:2]), int(endtime[0:2])+1)]
        for data in manage:
            logday = str(data.time).split()[0] + ' ' + str(data.time).split()[1][0:2]
            logtime = str(data.time).split()[1]
            if int(logtime[:2]) not in time_table:
                continue
            logtrack_id = str(data.track_id)
            if logday not in dataset['data'].keys():
                dataset['data'][logday] = {}
            if logtrack_id not in dataset['data'][logday].keys():
                dataset['data'][logday][logtrack_id] = {"meal":0, "water":0, "distance":0}
            
            dataset['data'][logday][logtrack_id]["meal"] += data.meal_hour
            dataset['data'][logday][logtrack_id]["water"] += data.water_hour
            dataset['data'][logday][logtrack_id]["distance"] += data.distance_hour
        return json.dumps(dataset)
    # 일 검색일 경우
    else:
        startidx = db.query(models.Manage).filter(
                                                    and_(models.Manage.time.contains(startday)),
                                                    and_(models.Manage.distance_hour != None) 
                                                    ).first().idx
        endidx = db.query(models.Manage).filter(
                                                and_(models.Manage.time.contains(endday)),
                                                and_(models.Manage.distance_hour != None) 
                                                ).order_by(models.Manage.idx.desc()).first().idx
        manage = db.query(models.Manage).filter(
                                                and_(models.Manage.idx >= startidx),
                                                and_(models.Manage.idx <= endidx), 
                                                and_(models.Manage.distance_hour != None),
                                                ).all()
        dataset = {'data':{}}
        for data in manage:
            logday = str(data.time).split()[0]
            logtrack_id = str(data.track_id)
            if logday not in dataset['data'].keys():
                dataset['data'][logday] = {}
            if logtrack_id not in dataset['data'][logday].keys():
                dataset['data'][logday][logtrack_id] = {"meal":0, "water":0, "distance":0}
            dataset['data'][logday][logtrack_id]["meal"] += data.meal_hour
            dataset['data'][logday][logtrack_id]["water"] += data.water_hour
            dataset['data'][logday][logtrack_id]["distance"] += data.distance_hour
    return json.dumps(dataset)
