from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from sqlalchemy.orm import Session
from sqlalchemy import and_

import models
import database, schemas

import json

from utils.calday import getMonthRage, getSplitYMD

router = APIRouter(
    prefix="/graph"
)

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def get_test(request: Request):
    print('get 호출')
    context = {}
    context['request'] = request
    return templates.TemplateResponse("graph.html", context)



@router.post('/post2')
async def get_test(form: schemas.Form, db:Session=Depends(database.get_db)):
    formtype = form.formtype
    startday = form.startday
    endday = form.endday
    starttime = None
    endtime = None
    if formtype == 1:
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

   
# db 접근 안될때
@router.post('/post')
async def NoDB(form:schemas.Form):
    formtype = form.formtype
    startday = form.startday
    endday = form.endday
    cctvnum = form.cctvnum
    starttime = None
    endtime = None
    # 시작년도 시작월 시작일
    syear, smonth, sday = getSplitYMD(startday)
    # 끝년도 끝월 끝날
    eyear, emonth, eday = getSplitYMD(endday)
    # 같은달
    if smonth  == emonth :
        # 같은 달일 경우  day리스트
        r_day_table = [x for x in range(sday, eday+1)] 
    
    # 시작달  첫day, 마지막day
    _, slast_day = getMonthRage(syear, smonth)


    smonth_daylist = [x for x in range(sday, slast_day + 1)]

    emonth_daylist = [x for x in range(1, eday+1)]

    if formtype == 1:
        starttime = form.starttime
        endtime = form.endtime

    import pandas as pd
    path = 'static/manage.csv'
    target = pd.read_csv(path)
    dataset = {'data':{}}
    
    # 시간일 경우 
    if formtype == 1:
        if startday == endday:
            time_table = [x for x in range(int(starttime[0:2]), int(endtime[0:2])+1)]
        # Dataframe 순회
        for index in range(len(target)):
            request = target.loc[index,:].to_dict()
            year_month_day, h_m_s = str(request['time']).split()
            year, month, day = list(map(int, year_month_day.split('-')))
            h, _, _ = list(map(int, h_m_s.split(":")))
            
            if startday == endday and  h not in time_table: 
                continue
            # 같은 달일때 날짜 테이블에 포함되지 않는다면
            elif smonth == emonth and  day not in r_day_table:
                continue
            # 시작 달이 아니라면?
            elif smonth == month and day not in smonth_daylist:
                continue
            elif emonth == month and day not in emonth_daylist:
                 continue
            elif eday == day and h >  int(endtime[0:2]):
                continue
            

            
            # 등록시간
            day = day if day > 9 else "0"+str(day)
            h = h if h > 9 else "0"+str(h)
            logtime = f"{year}-{month}-{day} {h}"
            track_id =  str(request['track_id'])
            meal = request['meal']
            water = request['water']
            distance = request['distance']
            if logtime not in dataset['data'].keys():
                dataset['data'][logtime] = {}
            if track_id not in dataset['data'][logtime].keys():
                dataset['data'][logtime][track_id] = {"meal":0, "water":0, "distance":0}
            dataset['data'][logtime][track_id]["meal"] += meal
            dataset['data'][logtime][track_id]["water"] += water
            dataset['data'][logtime][track_id]["distance"] += distance
    else:
        day_table = [1, 2, 3]
        # Dataframe 순회
        for index in range(len(target)):
            request = target.loc[index,:].to_dict()
            year_month_day, h_m_s = str(request['time']).split()
            year, month, day = list(map(int, year_month_day.split('-')))
            h, _, _ = list(map(int, h_m_s.split(":")))
            if day not in day_table:
                continue
            if smonth == emonth and  day not in r_day_table:
                continue
            else:
                pass
            # 등록시간
            day = day if day > 9 else "0"+str(day)
            logtime = f"{year}-{month}-{day}"
            track_id =  str(request['track_id'])
            meal = request['meal']
            water = request['water']
            distance = request['distance']
            if logtime not in dataset['data'].keys():
                dataset['data'][logtime] = {}
            if track_id not in dataset['data'][logtime].keys():
                dataset['data'][logtime][track_id] = {"meal":0, "water":0, "distance":0}
            dataset['data'][logtime][track_id]["meal"] += meal
            dataset['data'][logtime][track_id]["water"] += water
            dataset['data'][logtime][track_id]["distance"] += distance
    return json.dumps(dataset)
