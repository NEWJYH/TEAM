from pydantic import BaseModel
# from typing import List, Optional
# from datetime import date, timedelta

class request_item(BaseModel):
    today : str
    defaultStart : str
    dayLabel : list
    randomlist : list
    