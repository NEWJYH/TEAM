from fastapi import APIRouter, Depends, status, HTTPException, Response
import schemas, database, models
from sqlalchemy.orm import Session
from sqlalchemy import and_
# from typing import List

# from fastapi import  Request
from datetime import datetime, date

router = APIRouter(
    prefix="/db",
    tags=['CRUD']
)

# ---------------------------------------------------------
# 트래커 로그 테이블에 입력하기
@router.post("/post_trackerlog")
def post_TrackerLog(request: schemas.trackerLog, db:Session = Depends(database.get_db)):
    new_log = models.TrackerLog(
        origin_frame = request.origin_frame,
        frame = request.frame,
        score = request.score,
        start_frame = request.start_frame,
        track_id = request.track_id,
        xmin = request.xmin,
        ymin = request.ymin,
        xmax = request.xmax,
        ymax = request.ymax,
        distance = request.distance,
        meal = request.meal,
        water = request.water)    
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return new_log

# test injection
# import pandas as pd
# import time
# @router.post("/testpost")
# def post_test_trackerLog(db:Session = Depends(database.get_db)):   
#     df = pd.read_csv('test_22112616.csv')
#     cnt = 0
#     for index in range(len(df)):
#         request = df.loc[index, :].to_dict()
#         test_log =  models.TrackerLog(
#             time = request['time'],
#             score = request['score'],
#             origin_frame = request['origin_frame'],
#             frame = request['frame'],
#             start_frame = request['start_frame'],
#             track_id = request['track_id'],
#             xmin = request['xmin'],
#             ymin = request['ymin'],
#             xmax = request['xmax'],
#             ymax = request['ymax'],
#             distance = request['distance'],
#             meal = request['meal'],
#             water = request['water']    
#         )
#         print(cnt)
#         cnt += 1
#         db.add(test_log)
#         db.commit()
#         db.refresh(test_log)
#         if index == 0:
#             time.sleep(1)
#     return "success"

# ---------------------------------------------------------
# 소정보 테이블 
@router.post("/post_cow")
def post_Cow(request:schemas.Cow, db:Session = Depends(database.get_db)):
    new_cow = models.Cow(
        track_id = request.track_id,
        cctv_num = request.cctv_num,
        farm_num = request.farm_num
    )
    db.add(new_cow)
    db.commit()
    # db.refresh(new_cow)
    return new_cow

# 소정보 테이블 전부 읽어오기
@router.get('/getall_cows')
def getall_Cow(db:Session = Depends(database.get_db)):
    cows = db.query(models.Cow).all()
    return cows

# ----------------------------------------------------------------
# 소관리내역 테이블
# @router.post('/post_manage')
# def post_Manage(request:schemas.Manage, db:Session = Depends(database.get_db)):
#     new_Manage = models.Manage(
#         track_id = request.track_id,
#         meal_hour = request.meal_hour,
#         meal_day = request.meal_day,
#         water_hour = request.water_hour,
#         water_day = request.water_day,
#         distance_hour = request.distance_hour,
#         distance_day = request.distance_day
#     )
#     db.add(new_Manage)
#     db.commit()
#     db.refresh(new_Manage)
#     return new_Manage


# @router.get('/getall_manage')
# def getall_Manage(db:Session = Depends(database.get_db)):
#     manage = db.query(models.Manage).all()
#     return manage

# 날짜 지정해서 쿼리해오기 
@router.post('/get_manage')
def get_Manage(request:schemas.Option, db:Session=Depends(database.get_db)):
    if request.starttime == request.endtime:
        manage = db.query(models.Manage).filter(models.Manage.time.contains(request.starttime)).all()
    else:
        startindex = db.query(models.Manage).filter(models.Manage.time.contains(request.starttime)).first().idx
        endindex =db.query(models.Manage).filter(models.Manage.time.contains(request.endtime)).order_by(models.Manage.idx.desc()).first().idx
        manage = db.query(models.Manage).filter(and_(models.Manage.idx >= startindex), and_(models.Manage.idx <= endindex)).all()
    return manage


@router.get("/getall_manage")
def get_Manage( db:Session=Depends(database.get_db)):
    manage = db.query(models.Manage).all()
    return manage
