from pydantic import BaseModel
# from typing import List, Optional
# from datetime import date, timedelta
from datetime import date, timedelta

class index_post(BaseModel):
    today : date
    defaultStart : date
    
    class Config():
        orm_mode = True