from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import StreamingResponse
from fastapi.responses import HTMLResponse
from fastapi import Request, Response
from fastapi import Header
from sqlalchemy.orm import Session
from sqlalchemy import and_
from pathlib import Path

import database, schemas, models

from stream.stream import get_stream_video, get_stream_video2

import json

router = APIRouter(
    prefix="/live"
)

templates = Jinja2Templates(directory="templates")

CHUNK_SIZE = 1024*1024
video_path = Path("./static/video/detect/h264_v01.mp4")

@router.get("/")
async def index(request:Request):
    # 보낼 request를 설정
    return templates.TemplateResponse("live.html", context={"request": request})

@router.get("/video")
async def video_endpoint(range: str = Header(None)):
    start, end = range.replace("bytes=", "").split("-")
    # print(start)
    # print(end)
    start = int(start)
    end = int(end) if end else start + CHUNK_SIZE
    with open(video_path, "rb") as video:
        video.seek(start)
        data = video.read(end - start)
        filesize = str(video_path.stat().st_size)
        headers = {
            'Content-Range': f'bytes {str(start)}-{str(end)}/{filesize}',
            'Accept-Ranges': 'bytes'
        }
        return Response(data, status_code=206, headers=headers, media_type="video/mp4")

# @router.get("/stream_video")
# async def stream_video(request:Request):
#     # StringResponse함수를 return하고,
#     # 인자로 OpenCV에서 가져온 "바이트"이미지와 type을 명시
#     return StreamingResponse(get_stream_video(), media_type="multipart/x-mixed-replace; boundary=frame")


# db접근될때
@router.post('/post2')
async def get_test(form:schemas.MiniMapForm, db:Session=Depends(database.get_db)):
    
    minimapobj = db.query(models.MiniMap).filter(
                                                and_(models.MiniMap.sec >= form.sec),
                                                and_(models.MiniMap.sec <= form.sec+59),
                                                ).all()
    testdata = {}
    for data in minimapobj:
        sec = str(data.sec)
        frame = str(data.frame)
        cow_id = str(data.cow_id)
        x = str(data.xc)
        y = str(data.yc)
        if sec not in testdata.keys():
            testdata[sec] = {}
        if frame not in testdata[sec].keys():
            testdata[sec][frame] = {}
        testdata[sec][frame][cow_id] = {"x":x, "y":y}
    
    return json.dumps(testdata)

# db접속 안될때
@router.post('/post')
async def get_test(form:schemas.MiniMapForm):
    import time
    startsec = form.sec
    limitsec = startsec + 59
    import pandas as pd
    path = 'static/mini.csv'
    target = pd.read_csv(path)
    start = target.index[target.sec == startsec].tolist()[0]
    end = target.index[target.sec == limitsec].tolist()[-1]
    # print("start _ end", start, end)
    target = target.loc[start:end, :]
    # print(len(target))
    # print('호출됨')
    testdata = {}
    starttime = time.time()
    for index in range(len(target)):
        values = target.loc[index:].to_dict()
        sec = str(values['sec'])
        frame = str(values['frame'])
        cow_id = str(values['cow_id'])
        xc = str(values['xc'])
        yc = str(values['yc'])
        if sec not in testdata.keys():
            testdata[sec] = {}
        if frame not in testdata[sec].keys():
            testdata[sec][frame] = {}
        testdata[sec][frame][cow_id] = {"x":xc, "y":yc}
    endtime = time.time()
    print('time', endtime - starttime)

    return json.dumps(testdata)


# print('호출')
#     startsec = form.sec
#     limitsec = startsec + 59
#     import pandas as pd
#     path = 'static/mini.csv'
#     target = pd.read_csv(path)
#     start = target.index[target.sec == startsec].tolist()[0]
#     end = target.index[target.sec == limitsec].tolist()[-1]
    
#     data = {}
#     for index in range(start, end +1):
#         print('여기')
#         values = target.loc[index:].to_dict()
#         sec = str(values['sec'])
#         frame = str(values['frame'])
#         cow_id = str(values['cow_id'])
#         xc = values['xc']
#         yc = values['yc']
#         if sec not in data.keys():
#             data[sec] = {}
#         if frame not in data[sec].keys():
#             data[sec][frame] = {}
#         data[sec][frame][cow_id] = {"x":xc, "y":yc}
    
#     print(data)
#     return json.dumps(data)