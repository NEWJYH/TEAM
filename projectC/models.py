
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Float

from database import Base
from datetime import datetime
# relationships table connect to table
# 테이블끼리 연결하기
# from sqlalchemy.orm import relationship

# 트레킹 테이블
class TrackerLog(Base):
    __tablename__="trackerlog"
    # 순번
    idx = Column(Integer, primary_key=True, autoincrement=True)
    # 등록시간
    time = Column(DateTime(timezone=True), default=datetime.now)
    # 영상원본프레임
    origin_frame = Column(Integer)
    # 디텍션영상프레임
    frame = Column(Integer)
    # 디텍션시작 프레임 기록
    start_frame = Column(Integer)
    # 트레커아이디
    track_id = Column(Integer)
    # score
    score = Column(Float)
    # tl
    xmin = Column(Integer)
    ymin = Column(Integer)
    # br
    xmax = Column(Integer)
    ymax = Column(Integer)
    # 소이동 거리
    distance = Column(Integer)
    # 식사여부
    meal = Column(Boolean)
    # 음수여부
    water = Column(Boolean)

# 소정보
class Cow(Base):
    __tablename__="cow"
    idx = Column(Integer, primary_key=True, autoincrement=True)
    # 소 개체가 프라이머리키로 되어있음
    track_id = Column(Integer)
    # cctv 번호
    cctv_num = Column(Integer, default=3)
    # 사육장 
    farm_num = Column(Integer, default=3)
    # 마지막 기록시간
    time =  Column(DateTime(timezone=True), default=datetime.now)



# 소관리내역 테이블
class Manage(Base):
    __tablename__="manage"
    # 순번
    idx = Column(Integer, primary_key=True, autoincrement=True)
    # 등록 시간
    time =  Column(DateTime(timezone=True), default=datetime.now)
    # 소개체 번호
    track_id = Column(Integer)
    # 시간별 식사량
    meal_min = Column(Integer)
    # 시간별 음수량
    water_min= Column(Integer)
    # 시간별 이동시간
    distance_min = Column(Integer)
    # 시간별 식사량
    meal_hour = Column(Integer)
    # 시간별 음수량
    water_hour= Column(Integer)
    # 시간별 이동시간
    distance_hour = Column(Integer)
    

# trackerlog 순회를 위함 
class Log(Base):
    __tablename__="log"
    # 순번 
    idx = Column(Integer, primary_key=True, autoincrement=True)
    # trackerlog 마지막 idx
    track_idx = Column(Integer)
    # manage 마지막 idx
    manage_idx = Column(Integer)


# class Testhour(Base):
#     __tablename__='test'
#     # 순번
#     idx = Column(Integer, primary_key=True, autoincrement=True)
#     time =  Column(DateTime(timezone=True), default=datetime.now)
#     track_id = Column(Integer)
#     meal_hour = Column(Integer)
#     water_hour = Column(Integer)
#     distance_hour = Column(Integer)


# class TestDay(Base):
    # 순번
