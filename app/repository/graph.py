from fastapi import Request
from fastapi.templating import Jinja2Templates
import schemas 
import json

from utils.calday import getMonthRage, getSplitYMD

templates = Jinja2Templates(directory="templates")

def graph_html(request:Request):
    return templates.TemplateResponse("graph.html", context={"request": request})

# db 접근 안될때
def graph_query(form:schemas.Form):
    formtype = form.formtype
    startday = form.startday
    endday = form.endday
    cctvnum = form.cctvnum
    starttime = None
    endtime = None
    # 시작년도 시작월 시작일
    syear, smonth, sday = getSplitYMD(startday)
    # 끝년도 끝월 끝날
    eyear, emonth, eday = getSplitYMD(endday)
    # 같은달
    if smonth  == emonth :
        # 같은 달일 경우  day리스트
        r_day_table = [x for x in range(sday, eday+1)] 
    
    # 시작달  첫day, 마지막day
    _, slast_day = getMonthRage(syear, smonth)


    smonth_daylist = [x for x in range(sday, slast_day + 1)]

    emonth_daylist = [x for x in range(1, eday+1)]

    if formtype == 1:
        starttime = form.starttime
        endtime = form.endtime

    import pandas as pd
    path = 'static/manage.csv'
    target = pd.read_csv(path)
    dataset = {'data':{}}
    
    # 시간일 경우 
    if formtype == 1:
        if startday == endday:
            time_table = [x for x in range(int(starttime[0:2]), int(endtime[0:2])+1)]
        # Dataframe 순회
        for index in range(len(target)):
            request = target.loc[index,:].to_dict()
            year_month_day, h_m_s = str(request['time']).split()
            year, month, day = list(map(int, year_month_day.split('-')))
            h, _, _ = list(map(int, h_m_s.split(":")))
            
            if startday == endday and  h not in time_table: 
                continue
            # 같은 달일때 날짜 테이블에 포함되지 않는다면
            elif smonth == emonth and  day not in r_day_table:
                continue
            # 시작 달이 아니라면?
            elif smonth == month and day not in smonth_daylist:
                continue
            elif emonth == month and day not in emonth_daylist:
                 continue
            elif eday == day and h >  int(endtime[0:2]):
                continue

            # 등록시간
            day = day if day > 9 else "0"+str(day)
            h = h if h > 9 else "0"+str(h)
            logtime = f"{year}-{month}-{day} {h}"
            track_id =  str(request['track_id'])
            meal = request['meal']
            water = request['water']
            distance = request['distance']
            if logtime not in dataset['data'].keys():
                dataset['data'][logtime] = {}
            if track_id not in dataset['data'][logtime].keys():
                dataset['data'][logtime][track_id] = {"meal":0, "water":0, "distance":0}
            dataset['data'][logtime][track_id]["meal"] += meal
            dataset['data'][logtime][track_id]["water"] += water
            dataset['data'][logtime][track_id]["distance"] += distance
    else:
        day_table = [1, 2, 3]
        # Dataframe 순회
        for index in range(len(target)):
            request = target.loc[index,:].to_dict()
            year_month_day, h_m_s = str(request['time']).split()
            year, month, day = list(map(int, year_month_day.split('-')))
            h, _, _ = list(map(int, h_m_s.split(":")))
            if day not in day_table:
                continue
            if smonth == emonth and  day not in r_day_table:
                continue
            else:
                pass
            # 등록시간
            day = day if day > 9 else "0"+str(day)
            logtime = f"{year}-{month}-{day}"
            track_id =  str(request['track_id'])
            meal = request['meal']
            water = request['water']
            distance = request['distance']
            if logtime not in dataset['data'].keys():
                dataset['data'][logtime] = {}
            if track_id not in dataset['data'][logtime].keys():
                dataset['data'][logtime][track_id] = {"meal":0, "water":0, "distance":0}
            dataset['data'][logtime][track_id]["meal"] += meal
            dataset['data'][logtime][track_id]["water"] += water
            dataset['data'][logtime][track_id]["distance"] += distance
    return json.dumps(dataset)