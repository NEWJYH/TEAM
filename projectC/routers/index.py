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
    # print('postdata', postData)
    context = {}
#     testDataset = {
#     "startDate": "2022-10-23",
#     "endDate": "2022-11-22",
#     "cctv_id": 1,
#     "data": [{
#         "2022-10-24": {
#             "1": {
#                 "food": 10,
#                 "active": 26
#             },
#             "2": {
#                 "food": 18,
#                 "active": 33
#             },
#             "3": {
#                 "food": 8,
#                 "active": 40
#             },
#             "4": {
#                 "food": 11,
#                 "active": 36
#             },
#             "5": {
#                 "food": 16,
#                 "active": 30
#             }
#         },
#         "2022-10-25": {
#             "1": {
#                 "food": 11,
#                 "active": 26
#             },
#             "2": {
#                 "food": 19,
#                 "active": 33
#             },
#             "3": {
#                 "food": 8,
#                 "active": 40
#             },
#             "4": {
#                 "food": 11,
#                 "active": 36
#             },
#             "5": {
#                 "food": 16,
#                 "active": 30
#             }
#         },
#         "2022-10-26": {
#             "1": {
#                 "food": 12,
#                 "active": 26
#             },
#             "2": {
#                 "food": 20,
#                 "active": 33
#             },
#             "3": {
#                 "food": 8,
#                 "active": 40
#             },
#             "4": {
#                 "food": 11,
#                 "active": 36
#             },
#             "5": {
#                 "food": 16,
#                 "active": 30
#             }
#         },
#         "2022-10-27": {
#             "1": {
#                 "food": 13,
#                 "active": 26
#             },
#             "2": {
#                 "food": 21,
#                 "active": 33
#             },
#             "3": {
#                 "food": 8,
#                 "active": 40
#             },
#             "4": {
#                 "food": 11,
#                 "active": 36
#             },
#             "5": {
#                 "food": 16,
#                 "active": 30
#             }
#         },
#         "2022-10-28": {
#             "1": {
#                 "food": 14,
#                 "active": 26
#             },
#             "2": {
#                 "food": 22,
#                 "active": 33
#             },
#             "3": {
#                 "food": 8,
#                 "active": 40
#             },
#             "4": {
#                 "food": 11,
#                 "active": 36
#             },
#             "5": {
#                 "food": 16,
#                 "active": 30
#             }
#         },
#         "2022-10-29": {
#             "1": {
#                 "food": 15,
#                 "active": 26
#             },
#             "2": {
#                 "food": 23,
#                 "active": 33
#             },
#             "3": {
#                 "food": 8,
#                 "active": 40
#             },
#             "4": {
#                 "food": 11,
#                 "active": 36
#             },
#             "5": {
#                 "food": 16,
#                 "active": 30
#             }
#         },
#         "2022-10-30": {
#             "1": {
#                 "food": 16,
#                 "active": 26
#             },
#             "2": {
#                 "food": 24,
#                 "active": 33
#             },
#             "3": {
#                 "food": 8,
#                 "active": 40
#             },
#             "4": {
#                 "food": 11,
#                 "active": 36
#             },
#             "5": {
#                 "food": 16,
#                 "active": 30
#             }
#         },
#         "2022-10-31": {
#             "1": {
#                 "food": 15,
#                 "active": 26
#             },
#             "2": {
#                 "food": 23,
#                 "active": 33
#             },
#             "3": {
#                 "food": 8,
#                 "active": 40
#             },
#             "4": {
#                 "food": 11,
#                 "active": 36
#             },
#             "5": {
#                 "food": 16,
#                 "active": 30
#               }
#          }
#      }
#   ]
# }
#     testDataset = json.dumps(testDataset)
#     context['testDataset'] = testDataset
    context['request'] = request

    return templates.TemplateResponse("graph.j2", context)



@router.post('/post')
def get_test(form: schemas.Form,  db:Session=Depends(database.get_db)):
    print('post 호출')
    formtype = form.formtype
    startday = form.startday
    endday = form.endday
    cctvnum = form.cctvnum
    if formtype == 1:
        starttime = form.starttime
        endtime = form.endtime

    print('input')
    print('startday : ', startday)
    print('endday : ', endday)
    # print('cctvnum :', cctvnum)
    try:
        check = db.query(models.Manage).filter(models.Manage.time.contains(startday)).first().idx
    except:
        check = db.query(models.Manage).first()
        startday, endday = check.time, check.time + timedelta(hours=1)
        print('data null ')
        print('startday : ', startday)
        print('endday : ', endday)

    if startday == endday:
        manage = db.query(models.Manage).filter(models.Manage.time.contains(startday)).all()
    else:
        startindex = db.query(models.Manage).filter(models.Manage.time.contains(startday)).first().idx
        endindex =db.query(models.Manage).filter(models.Manage.time.contains(endday)).order_by(models.Manage.idx.desc()).first().idx
        manage = db.query(models.Manage).filter(and_(models.Manage.idx >= startindex), and_(models.Manage.idx <= endindex), and_(models.Manage.meal_min == None)).all()
    cnt = 0
    print("data size : ", len(manage))
    Dataset = {
            'startDate': str(date(startday.year, startday.month, startday.day)),
            'endDate' : str(date(endday.year, endday.month, endday.day)),
            'cctv_id': cctvnum,
            'data': {}
        }
    
    objlist = []
    for x in manage:
        day =str(date(x.time.year, x.time.month, x.time.day))
        cnt += 1
        if  day not in Dataset['data'].keys(): 
            Dataset['data'][day] = {}
        print('day', day)
        obj= { str(x.track_id) : {
                'food': x.meal_hour,
                'active': x.distance_hour,
                'water' : x.water_hour
                }
        }
        objlist.append(obj)
    print(objlist)
    Dataset['data'] = objlist
    print("Dataset", Dataset)
    return json.dumps(Dataset)