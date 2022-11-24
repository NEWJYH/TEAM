from pydantic import BaseModel
# from typing import List, Optional
# from datetime import date, timedelta
from datetime import date, timedelta, datetime


class index_post(BaseModel):
    today : date
    defaultStart : date
    
    class Config():
        orm_mode = True

class TrackerLog(BaseModel):
    idx : int
    time : datetime
    origin_frame : int
    frame : int
    start_frame : int
    track_id : int
    xmin : int
    ymin : int
    xmax : int
    ymax : int
    distance : int
    meal : bool
    water : bool
    
