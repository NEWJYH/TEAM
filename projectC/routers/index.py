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
def get_test(form: schemas.Form):
    print('post')
    formtype = form.formtype
    startday = form.startday
    endday = form.endday
    cctvnum = form.cctvnum
    
    testdata = { 
    "2022-11-29 00" : {
        "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
        "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
        "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
        "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
        "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
        "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
        "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
        "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
    },
    "2022-11-29 01" : {
        "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
        "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
        "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
        "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
        "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
        "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
        "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
        "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
    },
    "2022-11-29 02" : {
        "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
        "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
        "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
        "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
        "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
        "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
        "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
        "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
    },
    "2022-11-29 03" : {
        "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
        "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
        "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
        "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
        "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
        "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
        "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
        "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
    },
    "2022-11-29 04" : {
        "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
        "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
        "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
        "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
        "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
        "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
        "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
        "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
    },
    "2022-11-29 05" : {
        "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
        "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
        "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
        "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
        "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
        "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
        "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
        "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
    },
    "2022-11-29 06" : {
        "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
        "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
        "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
        "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
        "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
        "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
        "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
        "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
    },
    "2022-11-29 07" : {
        "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
        "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
        "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
        "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
        "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
        "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
        "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
        "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
    },
    "2022-11-29 08" : {
        "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
        "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
        "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
        "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
        "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
        "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
        "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
        "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
    },
    "2022-11-29 09" : {
        "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
        "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
        "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
        "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
        "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
        "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
        "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
        "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
    },
    "2022-11-29 10" : {
        "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
        "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
        "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
        "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
        "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
        "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
        "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
        "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
    },
    "2022-11-29 11" : {
        "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
        "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
        "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
        "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
        "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
        "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
        "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
        "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
    },
    "2022-11-29 12" : {
        "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
        "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
        "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
        "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
        "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
        "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
        "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
        "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
    },
    "2022-11-29 13" : {
        "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
        "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
        "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
        "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
        "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
        "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
        "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
        "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
    },
    "2022-11-29 14" : {
        "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
        "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
        "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
        "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
        "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
        "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
        "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
        "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
    },
    "2022-11-29 15" : {
        "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
        "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
        "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
        "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
        "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
        "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
        "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
        "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
    },
    "2022-11-29 16" : {
        "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
        "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
        "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
        "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
        "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
        "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
        "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
        "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
    },
    "2022-11-29 17" : {
        "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
        "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
        "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
        "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
        "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
        "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
        "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
        "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
    },
    "2022-11-29 18" : {
        "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
        "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
        "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
        "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
        "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
        "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
        "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
        "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
    },
    "2022-11-29 19" : {
        "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
        "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
        "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
        "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
        "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
        "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
        "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
        "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
    },
    "2022-11-29 20" : {
        "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
        "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
        "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
        "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
        "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
        "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
        "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
        "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
    },
    "2022-11-29 21" : {
        "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
        "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
        "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
        "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
        "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
        "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
        "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
        "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
    },
    "2022-11-29 22" : {
        "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
        "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
        "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
        "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
        "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
        "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
        "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
        "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
    },
    "2022-11-29 23" : {
        "1": {"meal_hour": 5094, "water_hour": 0, "distance_hour": 7628},
        "2": {"meal_hour": 5088, "water_hour": 0, "distance_hour": 7144},
        "3": {"meal_hour": 3064, "water_hour": 0, "distance_hour": 9979},
        "4": {"meal_hour": 3902, "water_hour": 0, "distance_hour": 9207},
        "5": {"meal_hour": 1590, "water_hour": 0, "distance_hour": 8868},
        "6": {"meal_hour": 4112, "water_hour": 0, "distance_hour": 5951},
        "7": {"meal_hour": 2719, "water_hour": 0, "distance_hour": 5534},
        "8": {"meal_hour": 0, "water_hour": 0, "distance_hour": 1523}
    }
}
    
    if formtype == 1:
        starttime = form.starttime
        endtime = form.endtime
    
    for key, value in testdata.items():
        print(key, value)

    return json.dumps(Dataset)
    # print('post 호출')
    # formtype = form.formtype
    # startday = form.startday
    # endday = form.endday
    # cctvnum = form.cctvnum
    # if formtype == 1:
    #     starttime = form.starttime
    #     endtime = form.endtime

    # print('input')
    # print('startday : ', startday)
    # print('endday : ', endday)
    # try:
    #     check = db.query(models.Manage).filter(models.Manage.time.contains(startday)).first().idx
    # except:
    #     check = db.query(models.Manage).first()
    #     startday, endday = check.time, check.time + timedelta(hours=1)
    #     print('data null ')
    #     print('startday : ', startday)
    #     print('endday : ', endday)
    # # 쿼리 날짜 확인
    # if startday == endday:
    #     manage = db.query(models.Manage).filter(models.Manage.time.contains(startday)).all()
    # else:
    #     startindex = db.query(models.Manage).filter(models.Manage.time.contains(startday)).first().idx
    #     endindex =db.query(models.Manage).filter(models.Manage.time.contains(endday)).order_by(models.Manage.idx.desc()).first().idx
    #     manage = db.query(models.Manage).filter(and_(models.Manage.idx >= startindex), and_(models.Manage.idx <= endindex), and_(models.Manage.meal_min == None)).all()
    # cnt = 0
    # print("data size : ", len(manage))
    # Dataset = {
    #         'startDate': str(date(startday.year, startday.month, startday.day)),
    #         'endDate' : str(date(endday.year, endday.month, endday.day)),
    #         'cctv_id': cctvnum,
    #         'data': {}
    #     }
    
    # objlist = []
    # for x in manage:
    #     day =str(date(x.time.year, x.time.month, x.time.day))
    #     cnt += 1
    #     if  day not in Dataset['data'].keys(): 
    #         Dataset['data'][day] = {}
    #     obj= { str(x.track_id) : {
    #             'food': x.meal_hour,
    #             'active': x.distance_hour,
    #             'water' : x.water_hour
    #             }
    #     }
    #     objlist.append(obj)
    # Dataset['data'] = objlist
    # print("Dataset", Dataset)
