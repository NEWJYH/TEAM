from database import SessionLocal, engine
import models
import datetime
from sqlalchemy import and_ 
# 집계함수 사용
from sqlalchemy.sql import func

db = SessionLocal()

import threading 
import time

class BackgroundTasks(threading.Thread):
    def __init__(self):
        super().__init__()
        self.curtime = None

    def set_time(self):
        self.curtime = time.localtime()

    # 자동 인젝션
    def Auto_Manage(self):
        # 로그에서 찾음 () 인덱스
        # 마지막 인덱스를 찾음
        log = db.query(models.Log).order_by(models.Log.track_idx.desc()).first()
        if not log :
            startindex = 1
            # 마지막 인덱스 쿼리 완료된 시간을 찾음
            starttime = db.query(models.TrackerLog).get(startindex).time
        # 다음 
        else:
            # 첫 인덱스가 아니라면 마지막 인덱스 +1 부터 찾음
            startindex = log + 1 
            starttime = db.query(models.TrackerLog).get(startindex).time
        endtime = starttime + datetime.timedelta(minutes=1)
        # 시작 시작과 끝시간을 찾음
        endindex =db.query(models.TrackerLog).filter(models.TrackerLog.time >= endtime).order_by(models.TrackerLog.idx.desc()).first().idx
        print(f"Injection start time : {starttime}")
        print(f"Injection start TrackerLog index : {startindex}")
        print(f"Injection  end  TrackerLog index : {endindex}")
        print(f"Injection  end  time : {endtime}")
        # 1초 동안 Tackerlog를 불러왔음 Query Obejct
        manage = db.query(models.TrackerLog).filter(and_(models.TrackerLog.idx >= startindex), and_(models.TrackerLog.idx <= endindex))

        manage.
     
        # manage.filter(func.sum())
        
        print("injection Size : ", len(manage.all()))
        # aggregate sum and Cal by sqlalchemy
        
        return 'Auto Manage Injection Success'


    def run(self,*args,**kwargs):
        flag = True 
        while True:
            self.set_time()
            print(self.Auto_Manage())

            if self.curtime.tm_sec == 0 and flag == True:
                flag = False
            elif self.curtime.tm_sec == 59:
                flag = True