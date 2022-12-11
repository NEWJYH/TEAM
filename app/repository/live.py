from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi import Request
from sqlalchemy.orm import Session
from sqlalchemy import and_

import database, schemas, models

import json
import time

templates = Jinja2Templates(directory="templates")

def live_html(request:Request):
    # 보낼 request를 설정
    return templates.TemplateResponse("live.html", context={"request": request})

def live_minimap(form:schemas.MiniMapForm, db:Session=Depends(database.get_db)):
    if form.sec == 1:
        time.sleep(10)
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

