# 통신데이터 형식으로 Django schemas와 같음
# json converter

from pydantic import BaseModel
from datetime import date, datetime

class index_post(BaseModel):
    today : date
    defaultStart : date
    class Config():
        orm_mode = True

# trackerLog테이블처리 할 시리얼라이저
class trackerLog(BaseModel):
    time : datetime
    cctv_num : int
    frame : int
    track_id : int
    xc : int
    xy : int
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
    formtype : int
    startday : str
    starttime : str
    endday : str
    endtime : str
    cctvnum : int

class MiniMapForm(BaseModel):
    sec : int

