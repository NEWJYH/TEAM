from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from sqlalchemy.orm import Session
from sqlalchemy import and_

import models
import database, schemas

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
    return templates.TemplateResponse("graph.html", context)



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

    # 시간 검색 경우
    # 일 검색 경우
    # 공통_작업
    # if startday == endday:
    #     # 일 검색
    #     if not starttime :
    #         print("일검색")
    #         manage = db.query(models.Manage).filter(and_(models.Manage.distance_hour != None), 
    #                                                 and_(models.Manage.time.contains(startday))).all()
    #     # 시간 검색
    #     else:
    #         # ----------------------
    #         # ----------------------
    #         # ----------------------
    #         # ----------------------
    #         # ----------------------
    #         # 여기서부터 수정 하면됨
    #         # ----------------------!SECTION
    #         print('시간검색')
    #         manage = db.query(models.Manage).filter(and_(models.Manage.distance_hour != None), 
    #                                                 and_(models.Manage.time.contains(startday)), 
    #                                                 or_(models.Manage.time.contains(starttime)), 
    #                                                 and_(models.Manage.time.contains(endtime))).all()
    # else:
    #     # 일 검색
    #     if not starttime:
    #         startindex = db.query(models.Manage).filter(and_(models.Manage.distance_hour != None), and_(models.Manage.time.contains(startday))).first().idx
    #         endindex =db.query(models.Manage).filter(and_(models.Manage.distance_hour != None), and_(models.Manage.time.contains(endday))).order_by(models.Manage.idx.desc()).first().idx
    #         manage = db.query(models.Manage).filter(and_(models.Manage.idx >= startindex), and_(models.Manage.idx <= endindex), and_(models.Manage.distance_hour != None)).all()
        
    # print("쿼리 수: ",len(manage))
    
    # for i in manage:
    #     print(str(i.track_id))

#     # return manage
#     pass
#     testdata = { 
#     "2022-11-29 00" : {
#         "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
#         "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
#         "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
#         "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
#         "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
#         "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
#         "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
#         "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
#     },
#     "2022-11-29 01" : {
#         "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
#         "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
#         "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
#         "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
#         "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
#         "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
#         "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
#         "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
#     },
#     "2022-11-29 02" : {
#         "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
#         "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
#         "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
#         "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
#         "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
#         "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
#         "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
#         "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
#     },
#     "2022-11-29 03" : {
#         "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
#         "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
#         "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
#         "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
#         "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
#         "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
#         "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
#         "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
#     },
#     "2022-11-29 04" : {
#         "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
#         "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
#         "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
#         "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
#         "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
#         "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
#         "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
#         "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
#     },
#     "2022-11-29 05" : {
#         "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
#         "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
#         "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
#         "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
#         "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
#         "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
#         "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
#         "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
#     },
#     "2022-11-29 06" : {
#         "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
#         "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
#         "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
#         "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
#         "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
#         "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
#         "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
#         "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
#     },
#     "2022-11-29 07" : {
#         "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
#         "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
#         "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
#         "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
#         "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
#         "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
#         "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
#         "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
#     },
#     "2022-11-29 08" : {
#         "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
#         "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
#         "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
#         "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
#         "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
#         "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
#         "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
#         "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
#     },
#     "2022-11-29 09" : {
#         "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
#         "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
#         "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
#         "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
#         "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
#         "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
#         "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
#         "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
#     },
#     "2022-11-29 10" : {
#         "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
#         "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
#         "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
#         "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
#         "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
#         "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
#         "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
#         "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
#     },
#     "2022-11-29 11" : {
#         "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
#         "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
#         "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
#         "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
#         "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
#         "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
#         "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
#         "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
#     },
#     "2022-11-29 12" : {
#         "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
#         "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
#         "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
#         "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
#         "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
#         "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
#         "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
#         "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
#     },
#     "2022-11-29 13" : {
#         "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
#         "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
#         "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
#         "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
#         "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
#         "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
#         "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
#         "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
#     },
#     "2022-11-29 14" : {
#         "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
#         "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
#         "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
#         "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
#         "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
#         "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
#         "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
#         "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
#     },
#     "2022-11-29 15" : {
#         "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
#         "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
#         "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
#         "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
#         "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
#         "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
#         "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
#         "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
#     },
#     "2022-11-29 16" : {
#         "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
#         "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
#         "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
#         "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
#         "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
#         "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
#         "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
#         "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
#     },
#     "2022-11-29 17" : {
#         "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
#         "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
#         "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
#         "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
#         "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
#         "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
#         "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
#         "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
#     },
#     "2022-11-29 18" : {
#         "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
#         "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
#         "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
#         "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
#         "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
#         "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
#         "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
#         "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
#     },
#     "2022-11-29 19" : {
#         "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
#         "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
#         "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
#         "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
#         "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
#         "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
#         "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
#         "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
#     },
#     "2022-11-29 20" : {
#         "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
#         "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
#         "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
#         "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
#         "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
#         "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
#         "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
#         "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
#     },
#     "2022-11-29 21" : {
#         "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
#         "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
#         "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
#         "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
#         "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
#         "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
#         "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
#         "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
#     },
#     "2022-11-29 22" : {
#         "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
#         "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
#         "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
#         "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
#         "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
#         "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
#         "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
#         "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
#     },
#     "2022-11-29 23" : {
#         "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
#         "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
#         "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
#         "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
#         "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
#         "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
#         "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
#         "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
#     }
# }
#     if formtype == 1:
#         starttime = form.starttime
#         endtime = form.endtime
#         objlist = []
#         Dataset = {'data': {}}
#         for key, value in testdata.items():
#             objlist.append({key.split()[1]:value})
            
#     Dataset['data'] = objlist
#     # print(Dataset)
#     return json.dumps(Dataset)
#     # print('post 호출')
#     # formtype = form.formtype
#     # startday = form.startday
#     # endday = form.endday
#     # cctvnum = form.cctvnum
#     # if formtype == 1:
#     #     starttime = form.starttime
#     #     endtime = form.endtime

#     # print('input')
#     # print('startday : ', startday)
#     # print('endday : ', endday)
#     # try:
#     #     check = db.query(models.Manage).filter(models.Manage.time.contains(startday)).first().idx
#     # except:
#     #     check = db.query(models.Manage).first()
#     #     startday, endday = check.time, check.time + timedelta(hours=1)
#     #     print('data null ')
#     #     print('startday : ', startday)
#     #     print('endday : ', endday)
#     # # 쿼리 날짜 확인
#     # if startday == endday:
#     #     manage = db.query(models.Manage).filter(models.Manage.time.contains(startday)).all()
#     # else:
#     #     startindex = db.query(models.Manage).filter(models.Manage.time.contains(startday)).first().idx
#     #     endindex =db.query(models.Manage).filter(models.Manage.time.contains(endday)).order_by(models.Manage.idx.desc()).first().idx
#     #     manage = db.query(models.Manage).filter(and_(models.Manage.idx >= startindex), and_(models.Manage.idx <= endindex), and_(models.Manage.meal_min == None)).all()
#     # cnt = 0
#     # print("data size : ", len(manage))
#     # Dataset = {
#     #         'startDate': str(date(startday.year, startday.month, startday.day)),
#     #         'endDate' : str(date(endday.year, endday.month, endday.day)),
#     #         'cctv_id': cctvnum,
#     #         'data': {}
#     #     }
    
#     # objlist = []
#     # for x in manage:
#     #     day =str(date(x.time.year, x.time.month, x.time.day))
#     #     cnt += 1
#     #     if  day not in Dataset['data'].keys(): 
#     #Dataset['data'][day] = {}         
#     #     obj= { str(x.track_id) : {
#     #             'food': x.meal_hour,
#     #             'active': x.distance_hour,
#     #             'water' : x.water_hour
#     #             }
#     #     }
#     #     objlist.append(obj)
#     # Dataset['data'] = objlist
#     # print("Dataset", Dataset)



# # {'data': 
# # 	[
# # 		{'00': {'1': {'meal_hour': 5094, 'water_hour': 0, 'distance_hour': 7628}, '2': {'meal_hour': 5088, 'water_hour': 0, 'distance_hour': 7144}, '3': {'meal_hour': 3064, 'water_hour': 0, 'distance_hour': 9979}, '4': {'meal_hour': 3902, 'water_hour': 0, 'distance_hour': 9207}, '5': {'meal_hour': 1590, 'water_hour': 0, 'distance_hour': 8868}, '6': {'meal_hour': 4112, 'water_hour': 0, 'distance_hour': 5951}, '7': {'meal_hour': 2719, 'water_hour': 0, 'distance_hour': 5534}, '8': {'meal_hour': 0, 'water_hour': 0, 'distance_hour': 1523}}}, 
# # 		{'01': {'1': {'meal_hour': 5094, 'water_hour': 0, 'distance_hour': 7628}, '2': {'meal_hour': 5088, 'water_hour': 0, 'distance_hour': 7144}, '3': {'meal_hour': 3064, 'water_hour': 0, 'distance_hour': 9979}, '4': {'meal_hour': 3902, 'water_hour': 0, 'distance_hour': 9207}, '5': {'meal_hour': 1590, 'water_hour': 0, 'distance_hour': 8868}, '6': {'meal_hour': 4112, 'water_hour': 0, 'distance_hour': 5951}, '7': {'meal_hour': 2719, 'water_hour': 0, 'distance_hour': 5534}, '8': {'meal_hour': 0, 'water_hour': 0, 'distance_hour': 1523}}}, 
# # 		{'02': {'1': {'meal_hour': 5094, 'water_hour': 0, 'distance_hour': 7628}, '2': {'meal_hour': 5088, 'water_hour': 0, 'distance_hour': 7144}, '3': {'meal_hour': 3064, 'water_hour': 0, 'distance_hour': 9979}, '4': {'meal_hour': 3902, 'water_hour': 0, 'distance_hour': 9207}, '5': {'meal_hour': 1590, 'water_hour': 0, 'distance_hour': 8868}, '6': {'meal_hour': 4112, 'water_hour': 0, 'distance_hour': 5951}, '7': {'meal_hour': 2719, 'water_hour': 0, 'distance_hour': 5534}, '8': {'meal_hour': 0, 'water_hour': 0, 'distance_hour': 1523}}}, 
# # 		{'03': {'1': {'meal_hour': 5094, 'water_hour': 0, 'distance_hour': 7628}, '2': {'meal_hour': 5088, 'water_hour': 0, 'distance_hour': 7144}, '3': {'meal_hour': 3064, 'water_hour': 0, 'distance_hour': 9979}, '4': {'meal_hour': 3902, 'water_hour': 0, 'distance_hour': 9207}, '5': {'meal_hour': 1590, 'water_hour': 0, 'distance_hour': 8868}, '6': {'meal_hour': 4112, 'water_hour': 0, 'distance_hour': 5951}, '7': {'meal_hour': 2719, 'water_hour': 0, 'distance_hour': 5534}, '8': {'meal_hour': 0, 'water_hour': 0, 'distance_hour': 1523}}}, 
# # 		{'04': {'1': {'meal_hour': 5094, 'water_hour': 0, 'distance_hour': 7628}, '2': {'meal_hour': 5088, 'water_hour': 0, 'distance_hour': 7144}, '3': {'meal_hour': 3064, 'water_hour': 0, 'distance_hour': 9979}, '4': {'meal_hour': 3902, 'water_hour': 0, 'distance_hour': 9207}, '5': {'meal_hour': 1590, 'water_hour': 0, 'distance_hour': 8868}, '6': {'meal_hour': 4112, 'water_hour': 0, 'distance_hour': 5951}, '7': {'meal_hour': 2719, 'water_hour': 0, 'distance_hour': 5534}, '8': {'meal_hour': 0, 'water_hour': 0, 'distance_hour': 1523}}}, 
# # 		{'05': {'1': {'meal_hour': 5094, 'water_hour': 0, 'distance_hour': 7628}, '2': {'meal_hour': 5088, 'water_hour': 0, 'distance_hour': 7144}, '3': {'meal_hour': 3064, 'water_hour': 0, 'distance_hour': 9979}, '4': {'meal_hour': 3902, 'water_hour': 0, 'distance_hour': 9207}, '5': {'meal_hour': 1590, 'water_hour': 0, 'distance_hour': 8868}, '6': {'meal_hour': 4112, 'water_hour': 0, 'distance_hour': 5951}, '7': {'meal_hour': 2719, 'water_hour': 0, 'distance_hour': 5534}, '8': {'meal_hour': 0, 'water_hour': 0, 'distance_hour': 1523}}}, 
# # 		{'06': {'1': {'meal_hour': 5094, 'water_hour': 0, 'distance_hour': 7628}, '2': {'meal_hour': 5088, 'water_hour': 0, 'distance_hour': 7144}, '3': {'meal_hour': 3064, 'water_hour': 0, 'distance_hour': 9979}, '4': {'meal_hour': 3902, 'water_hour': 0, 'distance_hour': 9207}, '5': {'meal_hour': 1590, 'water_hour': 0, 'distance_hour': 8868}, '6': {'meal_hour': 4112, 'water_hour': 0, 'distance_hour': 5951}, '7': {'meal_hour': 2719, 'water_hour': 0, 'distance_hour': 5534}, '8': {'meal_hour': 0, 'water_hour': 0, 'distance_hour': 1523}}},
# # 		{'07': {'1': {'meal_hour': 5094, 'water_hour': 0, 'distance_hour': 7628}, '2': {'meal_hour': 5088, 'water_hour': 0, 'distance_hour': 7144}, '3': {'meal_hour': 3064, 'water_hour': 0, 'distance_hour': 9979}, '4': {'meal_hour': 3902, 'water_hour': 0, 'distance_hour': 9207}, '5': {'meal_hour': 1590, 'water_hour': 0, 'distance_hour': 8868}, '6': {'meal_hour': 4112, 'water_hour': 0, 'distance_hour': 5951}, '7': {'meal_hour': 2719, 'water_hour': 0, 'distance_hour': 5534}, '8': {'meal_hour': 0, 'water_hour': 0, 'distance_hour': 1523}}}, 
# # 		{'08': {'1': {'meal_hour': 5094, 'water_hour': 0, 'distance_hour': 7628}, '2': {'meal_hour': 5088, 'water_hour': 0, 'distance_hour': 7144}, '3': {'meal_hour': 3064, 'water_hour': 0, 'distance_hour': 9979}, '4': {'meal_hour': 3902, 'water_hour': 0, 'distance_hour': 9207}, '5': {'meal_hour': 1590, 'water_hour': 0, 'distance_hour': 8868}, '6': {'meal_hour': 4112, 'water_hour': 0, 'distance_hour': 5951}, '7': {'meal_hour': 2719, 'water_hour': 0, 'distance_hour': 5534}, '8': {'meal_hour': 0, 'water_hour': 0, 'distance_hour': 1523}}}, 
# # 		{'09': {'1': {'meal_hour': 5094, 'water_hour': 0, 'distance_hour': 7628}, '2': {'meal_hour': 5088, 'water_hour': 0, 'distance_hour': 7144}, '3': {'meal_hour': 3064, 'water_hour': 0, 'distance_hour': 9979}, '4': {'meal_hour': 3902, 'water_hour': 0, 'distance_hour': 9207}, '5': {'meal_hour': 1590, 'water_hour': 0, 'distance_hour': 8868}, '6': {'meal_hour': 4112, 'water_hour': 0, 'distance_hour': 5951}, '7': {'meal_hour': 2719, 'water_hour': 0, 'distance_hour': 5534}, '8': {'meal_hour': 0, 'water_hour': 0, 'distance_hour': 1523}}}, 
# # 		{'10': {'1': {'meal_hour': 5094, 'water_hour': 0, 'distance_hour': 7628}, '2': {'meal_hour': 5088, 'water_hour': 0, 'distance_hour': 7144}, '3': {'meal_hour': 3064, 'water_hour': 0, 'distance_hour': 9979}, '4': {'meal_hour': 3902, 'water_hour': 0, 'distance_hour': 9207}, '5': {'meal_hour': 1590, 'water_hour': 0, 'distance_hour': 8868}, '6': {'meal_hour': 4112, 'water_hour': 0, 'distance_hour': 5951}, '7': {'meal_hour': 2719, 'water_hour': 0, 'distance_hour': 5534}, '8': {'meal_hour': 0, 'water_hour': 0, 'distance_hour': 1523}}}, 
# # 		{'11': {'1': {'meal_hour': 5094, 'water_hour': 0, 'distance_hour': 7628}, '2': {'meal_hour': 5088, 'water_hour': 0, 'distance_hour': 7144}, '3': {'meal_hour': 3064, 'water_hour': 0, 'distance_hour': 9979}, '4': {'meal_hour': 3902, 'water_hour': 0, 'distance_hour': 9207}, '5': {'meal_hour': 1590, 'water_hour': 0, 'distance_hour': 8868}, '6': {'meal_hour': 4112, 'water_hour': 0, 'distance_hour': 5951}, '7': {'meal_hour': 2719, 'water_hour': 0, 'distance_hour': 5534}, '8': {'meal_hour': 0, 'water_hour': 0, 'distance_hour': 1523}}}, 
# # 		{'12': {'1': {'meal_hour': 5094, 'water_hour': 0, 'distance_hour': 7628}, '2': {'meal_hour': 5088, 'water_hour': 0, 'distance_hour': 7144}, '3': {'meal_hour': 3064, 'water_hour': 0, 'distance_hour': 9979}, '4': {'meal_hour': 3902, 'water_hour': 0, 'distance_hour': 9207}, '5': {'meal_hour': 1590, 'water_hour': 0, 'distance_hour': 8868}, '6': {'meal_hour': 4112, 'water_hour': 0, 'distance_hour': 5951}, '7': {'meal_hour': 2719, 'water_hour': 0, 'distance_hour': 5534}, '8': {'meal_hour': 0, 'water_hour': 0, 'distance_hour': 1523}}}, 
# # 		{'13': {'1': {'meal_hour': 5094, 'water_hour': 0, 'distance_hour': 7628}, '2': {'meal_hour': 5088, 'water_hour': 0, 'distance_hour': 7144}, '3': {'meal_hour': 3064, 'water_hour': 0, 'distance_hour': 9979}, '4': {'meal_hour': 3902, 'water_hour': 0, 'distance_hour': 9207}, '5': {'meal_hour': 1590, 'water_hour': 0, 'distance_hour': 8868}, '6': {'meal_hour': 4112, 'water_hour': 0, 'distance_hour': 5951}, '7': {'meal_hour': 2719, 'water_hour': 0, 'distance_hour': 5534}, '8': {'meal_hour': 0, 'water_hour': 0, 'distance_hour': 1523}}}, 
# # 		{'14': {'1': {'meal_hour': 5094, 'water_hour': 0, 'distance_hour': 7628}, '2': {'meal_hour': 5088, 'water_hour': 0, 'distance_hour': 7144}, '3': {'meal_hour': 3064, 'water_hour': 0, 'distance_hour': 9979}, '4': {'meal_hour': 3902, 'water_hour': 0, 'distance_hour': 9207}, '5': {'meal_hour': 1590, 'water_hour': 0, 'distance_hour': 8868}, '6': {'meal_hour': 4112, 'water_hour': 0, 'distance_hour': 5951}, '7': {'meal_hour': 2719, 'water_hour': 0, 'distance_hour': 5534}, '8': {'meal_hour': 0, 'water_hour': 0, 'distance_hour': 1523}}}, 
# # 		{'15': {'1': {'meal_hour': 5094, 'water_hour': 0, 'distance_hour': 7628}, '2': {'meal_hour': 5088, 'water_hour': 0, 'distance_hour': 7144}, '3': {'meal_hour': 3064, 'water_hour': 0, 'distance_hour': 9979}, '4': {'meal_hour': 3902, 'water_hour': 0, 'distance_hour': 9207}, '5': {'meal_hour': 1590, 'water_hour': 0, 'distance_hour': 8868}, '6': {'meal_hour': 4112, 'water_hour': 0, 'distance_hour': 5951}, '7': {'meal_hour': 2719, 'water_hour': 0, 'distance_hour': 5534}, '8': {'meal_hour': 0, 'water_hour': 0, 'distance_hour': 1523}}}, 
# # 		{'16': {'1': {'meal_hour': 5094, 'water_hour': 0, 'distance_hour': 7628}, '2': {'meal_hour': 5088, 'water_hour': 0, 'distance_hour': 7144}, '3': {'meal_hour': 3064, 'water_hour': 0, 'distance_hour': 9979}, '4': {'meal_hour': 3902, 'water_hour': 0, 'distance_hour': 9207}, '5': {'meal_hour': 1590, 'water_hour': 0, 'distance_hour': 8868}, '6': {'meal_hour': 4112, 'water_hour': 0, 'distance_hour': 5951}, '7': {'meal_hour': 2719, 'water_hour': 0, 'distance_hour': 5534}, '8': {'meal_hour': 0, 'water_hour': 0, 'distance_hour': 1523}}}, 
# # 		{'17': {'1': {'meal_hour': 5094, 'water_hour': 0, 'distance_hour': 7628}, '2': {'meal_hour': 5088, 'water_hour': 0, 'distance_hour': 7144}, '3': {'meal_hour': 3064, 'water_hour': 0, 'distance_hour': 9979}, '4': {'meal_hour': 3902, 'water_hour': 0, 'distance_hour': 9207}, '5': {'meal_hour': 1590, 'water_hour': 0, 'distance_hour': 8868}, '6': {'meal_hour': 4112, 'water_hour': 0, 'distance_hour': 5951}, '7': {'meal_hour': 2719, 'water_hour': 0, 'distance_hour': 5534}, '8': {'meal_hour': 0, 'water_hour': 0, 'distance_hour': 1523}}}, 
# # 		{'18': {'1': {'meal_hour': 5094, 'water_hour': 0, 'distance_hour': 7628}, '2': {'meal_hour': 5088, 'water_hour': 0, 'distance_hour': 7144}, '3': {'meal_hour': 3064, 'water_hour': 0, 'distance_hour': 9979}, '4': {'meal_hour': 3902, 'water_hour': 0, 'distance_hour': 9207}, '5': {'meal_hour': 1590, 'water_hour': 0, 'distance_hour': 8868}, '6': {'meal_hour': 4112, 'water_hour': 0, 'distance_hour': 5951}, '7': {'meal_hour': 2719, 'water_hour': 0, 'distance_hour': 5534}, '8': {'meal_hour': 0, 'water_hour': 0, 'distance_hour': 1523}}}, 
# # 		{'19': {'1': {'meal_hour': 5094, 'water_hour': 0, 'distance_hour': 7628}, '2': {'meal_hour': 5088, 'water_hour': 0, 'distance_hour': 7144}, '3': {'meal_hour': 3064, 'water_hour': 0, 'distance_hour': 9979}, '4': {'meal_hour': 3902, 'water_hour': 0, 'distance_hour': 9207}, '5': {'meal_hour': 1590, 'water_hour': 0, 'distance_hour': 8868}, '6': {'meal_hour': 4112, 'water_hour': 0, 'distance_hour': 5951}, '7': {'meal_hour': 2719, 'water_hour': 0, 'distance_hour': 5534}, '8': {'meal_hour': 0, 'water_hour': 0, 'distance_hour': 1523}}}, 
# # 		{'20': {'1': {'meal_hour': 5094, 'water_hour': 0, 'distance_hour': 7628}, '2': {'meal_hour': 5088, 'water_hour': 0, 'distance_hour': 7144}, '3': {'meal_hour': 3064, 'water_hour': 0, 'distance_hour': 9979}, '4': {'meal_hour': 3902, 'water_hour': 0, 'distance_hour': 9207}, '5': {'meal_hour': 1590, 'water_hour': 0, 'distance_hour': 8868}, '6': {'meal_hour': 4112, 'water_hour': 0, 'distance_hour': 5951}, '7': {'meal_hour': 2719, 'water_hour': 0, 'distance_hour': 5534}, '8': {'meal_hour': 0, 'water_hour': 0, 'distance_hour': 1523}}}, 
# # 		{'21': {'1': {'meal_hour': 5094, 'water_hour': 0, 'distance_hour': 7628}, '2': {'meal_hour': 5088, 'water_hour': 0, 'distance_hour': 7144}, '3': {'meal_hour': 3064, 'water_hour': 0, 'distance_hour': 9979}, '4': {'meal_hour': 3902, 'water_hour': 0, 'distance_hour': 9207}, '5': {'meal_hour': 1590, 'water_hour': 0, 'distance_hour': 8868}, '6': {'meal_hour': 4112, 'water_hour': 0, 'distance_hour': 5951}, '7': {'meal_hour': 2719, 'water_hour': 0, 'distance_hour': 5534}, '8': {'meal_hour': 0, 'water_hour': 0, 'distance_hour': 1523}}}, 
# # 		{'22': {'1': {'meal_hour': 5094, 'water_hour': 0, 'distance_hour': 7628}, '2': {'meal_hour': 5088, 'water_hour': 0, 'distance_hour': 7144}, '3': {'meal_hour': 3064, 'water_hour': 0, 'distance_hour': 9979}, '4': {'meal_hour': 3902, 'water_hour': 0, 'distance_hour': 9207}, '5': {'meal_hour': 1590, 'water_hour': 0, 'distance_hour': 8868}, '6': {'meal_hour': 4112, 'water_hour': 0, 'distance_hour': 5951}, '7': {'meal_hour': 2719, 'water_hour': 0, 'distance_hour': 5534}, '8': {'meal_hour': 0, 'water_hour': 0, 'distance_hour': 1523}}}, 
# # 		{'23': {'1': {'meal_hour': 5094, 'water_hour': 0, 'distance_hour': 7628}, '2': {'meal_hour': 5088, 'water_hour': 0, 'distance_hour': 7144}, '3': {'meal_hour': 3064, 'water_hour': 0, 'distance_hour': 9979}, '4': {'meal_hour': 3902, 'water_hour': 0, 'distance_hour': 9207}, '5': {'meal_hour': 1590, 'water_hour': 0, 'distance_hour': 8868}, '6': {'meal_hour': 4112, 'water_hour': 0, 'distance_hour': 5951}, '7': {'meal_hour': 2719, 'water_hour': 0, 'distance_hour': 5534}, '8': {'meal_hour': 0, 'water_hour': 0, 'distance_hour': 1523}}}
# # 	]
# # }

# 일 검색 결과 
# {'data': 
#     {'2022-12-01': 
#         {'1': {'meal_hour': 574, 'water_hour': 0, 'distance_hour': 53733}, 
#          '2': {'meal_hour': 1452, 'water_hour': 0, 'distance_hour': 110926}, 
#          '3': {'meal_hour': 205, 'water_hour': 0, 'distance_hour': 71431}, 
#          '4': {'meal_hour': 1292, 'water_hour': 0, 'distance_hour': 113494}, 
#          '5': {'meal_hour': 2529, 'water_hour': 0, 'distance_hour': 136947}, 
#          '6': {'meal_hour': 2250, 'water_hour': 0, 'distance_hour': 145484}, 
#          '7': {'meal_hour': 2829, 'water_hour': 0, 'distance_hour': 113744}, 
#          '8': {'meal_hour': 804, 'water_hour': 0, 'distance_hour': 99488}
#         }
#     }
# }

# # 시간검색
# {   
#     '2022-12-01 14': 
#         {
#             '1': {'meal_hour': 574, 'water_hour': 0, 'distance_hour': 53733}, 
#             '2': {'meal_hour': 1452, 'water_hour': 0, 'distance_hour': 110926}, 
#             '3': {'meal_hour': 205, 'water_hour': 0, 'distance_hour': 71431}, 
#             '4': {'meal_hour': 1292, 'water_hour': 0, 'distance_hour': 113494}, 
#             '5': {'meal_hour': 2529, 'water_hour': 0, 'distance_hour': 136947}, 
#             '6': {'meal_hour': 2250, 'water_hour': 0, 'distance_hour': 145484}, 
#             '7': {'meal_hour': 2829, 'water_hour': 0, 'distance_hour': 113744}, 
#             '8': {'meal_hour': 804, 'water_hour': 0, 'distance_hour': 99488}
#             }, 
#     '2022-12-01 15': 
#         {
#             '5': {'meal_hour': 2359, 'water_hour': 0, 'distance_hour': 152273}, 
#             '6': {'meal_hour': 979, 'water_hour': 0, 'distance_hour': 108438}, 
#             '3': {'meal_hour': 1646, 'water_hour': 0, 'distance_hour': 180881}, 
#             '7': {'meal_hour': 2818, 'water_hour': 0, 'distance_hour': 228523}, 
#             '8': {'meal_hour': 757, 'water_hour': 0, 'distance_hour': 177440}, 
#             '1': {'meal_hour': 3007, 'water_hour': 0, 'distance_hour': 183995}, 
#             '2': {'meal_hour': 2466, 'water_hour': 0, 'distance_hour': 158283}, 
#             '4': {'meal_hour': 2208, 'water_hour': 0, 'distance_hour': 118695}
#         }
# }
