from database import SessionLocal, engine
import models
import datetime
from sqlalchemy import and_ 

db = SessionLocal()

import threading 
import time

class BackgroundTasks(threading.Thread):
    def __init__(self):
        super().__init__()
        self.curtime = None
        self.queryflag = False

    def set_time(self):
        self.curtime = time.localtime()

    # 자동 인젝션
    def Auto_Manage(self):
        # 로그에서 찾음 () 인덱스
        # 마지막 인덱스를 찾음
        message = "Error"
        log = None
        try:
            log = db.query(models.Log).order_by(models.Log.track_idx.desc()).first().track_idx
        except:
            pass
        
        # print(type(log))
        if not log :
            startindex = 1
            # 마지막 인덱스 쿼리 완료된 시간을 찾음
            starttime = db.query(models.TrackerLog).get(startindex).time
        # 다음 
        else:
            # 첫 인덱스가 아니라면 마지막 인덱스 +1 부터 찾음
            startindex = log + 1 
            try:
                starttime = db.query(models.TrackerLog).get(startindex).time
            except:
                #여기 걸리면 쿼리할것이 없다는 것이다.
                self.queryflag = True
                message ='TrackerLog is empty'
                return f" Auto Manage Injection fail {message}"
        if self.queryflag == False:
            endtime = starttime + datetime.timedelta(minutes=1)
            # 시작 시작과 끝시간을 찾음
            endindex =db.query(models.TrackerLog).filter(models.TrackerLog.time >= endtime).order_by(models.TrackerLog.idx.desc()).first().idx
            print(f"Injection start time : {starttime}")
            print(f"Injection start TrackerLog index : {startindex}")
            print(f"Injection  end  TrackerLog index : {endindex}")
            print(f"Injection  end  time : {endtime}")
            # 1분 동안 Tackerlog를 불러왔음 Query Obejct
            manage = db.query(models.TrackerLog).filter(and_(models.TrackerLog.idx >= startindex), and_(models.TrackerLog.idx <= endindex)).all()
            
            # 빈 객체에 저장하기 위함
            qodict = {}
            for qo in manage:
                meal = 1 if qo.meal == True else 0
                water = 1 if qo.water == True else 0
                distance = qo.distance
                time = qo.time
                if qo.track_id not in qodict:
                    qodict[qo.track_id] = {
                        "meal_hour" : meal,
                        "water_hour" : water,
                        "distance_hour" : distance
                        }
                else:
                    qodict[qo.track_id]['meal_hour'] += meal
                    qodict[qo.track_id]['water_hour'] += water
                    qodict[qo.track_id]['distance_hour'] += distance

            for key, value in qodict.items():
                # 여기서 Manage Table에 인젝션
                newmanage = models.Manage(
                    time = endtime,
                    track_id = key,
                    meal_hour = value['meal_hour'],
                    water_hour = value['water_hour'],
                    distance_hour = value['water_hour']
                )    
                db.add(newmanage)
                db.commit()
                db.refresh(newmanage)
            
            print("injection Size : ", len(manage))
            newlog = models.Log(
                track_idx = endindex
            )
            db.add(newlog)
            db.commit()
            db.refresh(newlog)

            return 'Auto Manage Injection Success'


    def run(self,*args,**kwargs):
        flag = True 
        while True:
            self.set_time()
<<<<<<< HEAD
            if self.curtime.tm_sec == 0 and flag and not self.queryflag:
                flag = False
                print(self.Auto_Manage())
            elif self.curtime.tm_sec == 59:
                flag = True
=======
            if a == True:
                if self.curtime.tm_sec == 0:
                    a = False
                    # print(self.curtime)
                    # print('this')
            if a == False:
                if self.curtime.tm_sec == 5:
                    a = True
>>>>>>> develop
