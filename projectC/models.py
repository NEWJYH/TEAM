# DB 테이블 정의 
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Float

from database import Base
from datetime import datetime
# relationships table connect to table
# 테이블끼리 연결하기
# from sqlalchemy.orm import relationship

# 트레킹 테이블 _완료
class TrackerLog(Base):
    __tablename__="tracker_log"
    # 순번
    idx = Column(Integer, primary_key=True, autoincrement=True)
    # 등록시간 : -> 실시간 시간 기준으로 영상 시간기준
    time = Column(DateTime(timezone=True), default=datetime.now)
    # cctv_ch
    cctv_num = Column(Integer)
    # 디텍션영상프레임
    frame = Column(Integer)
    # 트레커아이디
    track_id = Column(Integer)
    # 중심 x좌표    
    xc = Column(Integer)
    # 중심 y좌표
    xy = Column(Integer)
    # 소이동 거리 1초
    distance = Column(Integer)
    # 식사여부 1초
    meal = Column(Boolean)
    # 음수여부 1초
    water = Column(Boolean)

# 소정보
class Cow(Base):
    __tablename__="cow"
    idx = Column(Integer, primary_key=True, autoincrement=True)
    track_id = Column(Integer)
    # cctv 번호
    cctv_num = Column(Integer, default=3)
    # 마지막 기록시간
    time =  Column(DateTime(timezone=True), default=datetime.now)

# 소관리내역 테이블
class Manage(Base):
    __tablename__="manage1"
    # 순번
    idx = Column(Integer, primary_key=True, autoincrement=True)
    # 등록 시간 분단위
    time =  Column(DateTime(timezone=True), default=datetime.now)
    # cctv 번호 
    cctv_num = Column(Integer)
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
    __tablename__="log1"
    # 순번 
    idx = Column(Integer, primary_key=True, autoincrement=True)
    # trackerlog 마지막 idx
    track_idx = Column(Integer)
    manage_idx = Column(Integer)

# # 트레킹 테이블 _완료
# class DoneTrackerLog(Base):
#     __tablename__="done_tracker_log"
#     # 순번
#     idx = Column(Integer, primary_key=True, autoincrement=True)
#     # 등록시간 : -> 실시간 시간 기준으로 영상 시간기준
#     time = Column(DateTime(timezone=True), default=datetime.now)
#     # cctv_ch
#     cctv_num = Column(Integer)
#     # 디텍션영상프레임
#     frame = Column(Integer)
#     # 트레커아이디
#     track_id = Column(Integer)
#     # 중심 x좌표    
#     xc = Column(Integer)
#     # 중심 y좌표
#     xy = Column(Integer)
#     # 소이동 거리 1초
#     distance = Column(Integer)
#     # 식사여부 1초
#     meal = Column(Boolean)
#     # 음수여부 1초
#     water = Column(Boolean)
