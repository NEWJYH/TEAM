from pydantic import BaseModel
# from typing import List, Optional
# from datetime import date, timedelta
from datetime import date, timedelta, datetime


class index_post(BaseModel):
    today : date
    defaultStart : date
    class Config():
        orm_mode = True

class trackerLog(BaseModel):
    origin_frame : int
    frame : int
    start_frame : int
    track_id : int
    score : float
    xmin : int
    ymin : int
    xmax : int
    ymax : int
    distance : int
    meal : bool
    water : bool
    

class Cow(BaseModel):
    track_id : int
    cctv_num : int
    farm_num : int

class Manage(BaseModel):
    track_id : int
    meal_hour : int
    meal_day : int
    water_hour : int
    water_day : int
    distance_hour : int
    distance_day : int

class AutoSaveManage(Manage):
    class Config():
        orm_mode = True


class showTrackLog(trackerLog):
    class Config():
        orm_mode = True

class showCow(Cow):
    class Config():
        orm_mode = True

class showManage(Manage):
    class config():
        orm_mode = True

# 매니저 옵션
class Option(BaseModel):
    starttime: str
    endtime : str


# form data , web
class Form(BaseModel):
    startday : str
    endday : str
    cctvnum : int
