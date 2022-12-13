# DB 테이블 정의 
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Float

from database import Base
from datetime import datetime
# relationships table connect to table
# 테이블끼리 연결하기
# from sqlalchemy.orm import relationship

# 트레킹 테이블 _완료
# class TrackerLog(Base):
#     __tablename__="trackerlog_1"
#     # 순번
#     idx = Column(Integer, primary_key=True, autoincrement=True)
#     # 등록시간 : -> 실시간 시간 기준으로 영상 시간기준
#     time = Column(DateTime(timezone=True), default=datetime.now)
#     xc = Column(Integer)
#     yc = Column(Integer)
#     # cctv_ch
#     cctv_num = Column(Integer)
#     # 트레커아이디
#     cow_id = Column(Integer)
#     # 거리
#     distance = Column(Integer)
#     # 식사여부 1초
#     meal = Column(Boolean)
#     # 음수여부 1초
#     water = Column(Boolean)

# # 소정보
# class Cow(Base):
#     __tablename__="cow_1"
#     cow_id = Column(Integer, primary_key=True)
#     # cctv 번호
#     cctv_num = Column(Integer)
#     # 마지막 기록시간
#     time =  Column(DateTime(timezone=True), default=datetime.now)
#     # 정보
#     info = Column(String(100))


# minimap
class MiniMap(Base):
    __tablename__="minimap"
    idx = Column(Integer, primary_key=True, autoincrement=True)
    sec = Column(Integer)
    frame = Column(Integer)
    cow_id = Column(Integer)
    xc = Column(Integer)
    yc = Column(Integer)


# class MiniMap1(Base):
#     __tablename__="minimap1"
#     cow_id = Column(Integer, primary_key=True)
#     time = Column(Integer)
#     xc = Column(Integer)
#     yc = Column(Integer)

