# 디비 엔진 생성
from sqlalchemy import create_engine

# 선언
from sqlalchemy.ext.declarative import declarative_base

# session orm
from sqlalchemy.orm import sessionmaker

SQLALCHAMY_DATABASE_URL = 'sqlite:///../blog.db'

engine = create_engine(SQLALCHAMY_DATABASE_URL, echo=True, connect_args={"check_same_thread":False})


SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()