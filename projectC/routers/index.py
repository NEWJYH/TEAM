from fastapi import APIRouter, Depends, status, HTTPException, Response, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from sqlalchemy.orm import Session
from sqlalchemy import and_ 



import models
import database, schemas

from datetime import date, timedelta
import random
import json


import json

from pydantic import BaseModel 

class Form(BaseModel):
    startday : str
    endday : str
    cctvnum : int

router = APIRouter(
    prefix="/graph"
)

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def get_test(request: Request ):
    print('get 호출')
    context = {}
    testDataset = {
    "startDate": "2022-10-23",
    "endDate": "2022-11-22",
    "cctv_id": 1,
    "data": {
        "2022-10-24": {
            "1": {
                "food": 10,
                "active": 26
            },
            "2": {
                "food": 18,
                "active": 33
            },
            "3": {
                "food": 8,
                "active": 40
            },
            "4": {
                "food": 11,
                "active": 36
            },
            "5": {
                "food": 16,
                "active": 30
            }
        },
        "2022-10-25": {
            "1": {
                "food": 11,
                "active": 26
            },
            "2": {
                "food": 19,
                "active": 33
            },
            "3": {
                "food": 8,
                "active": 40
            },
            "4": {
                "food": 11,
                "active": 36
            },
            "5": {
                "food": 16,
                "active": 30
            }
        },
        "2022-10-26": {
            "1": {
                "food": 12,
                "active": 26
            },
            "2": {
                "food": 20,
                "active": 33
            },
            "3": {
                "food": 8,
                "active": 40
            },
            "4": {
                "food": 11,
                "active": 36
            },
            "5": {
                "food": 16,
                "active": 30
            }
        },
        "2022-10-27": {
            "1": {
                "food": 13,
                "active": 26
            },
            "2": {
                "food": 21,
                "active": 33
            },
            "3": {
                "food": 8,
                "active": 40
            },
            "4": {
                "food": 11,
                "active": 36
            },
            "5": {
                "food": 16,
                "active": 30
            }
        },
        "2022-10-28": {
            "1": {
                "food": 14,
                "active": 26
            },
            "2": {
                "food": 22,
                "active": 33
            },
            "3": {
                "food": 8,
                "active": 40
            },
            "4": {
                "food": 11,
                "active": 36
            },
            "5": {
                "food": 16,
                "active": 30
            }
        },
        "2022-10-29": {
            "1": {
                "food": 15,
                "active": 26
            },
            "2": {
                "food": 23,
                "active": 33
            },
            "3": {
                "food": 8,
                "active": 40
            },
            "4": {
                "food": 11,
                "active": 36
            },
            "5": {
                "food": 16,
                "active": 30
            }
        },
        "2022-10-30": {
            "1": {
                "food": 16,
                "active": 26
            },
            "2": {
                "food": 24,
                "active": 33
            },
            "3": {
                "food": 8,
                "active": 40
            },
            "4": {
                "food": 11,
                "active": 36
            },
            "5": {
                "food": 16,
                "active": 30
            }
        },
        "2022-10-31": {
            "1": {
                "food": 15,
                "active": 26
            },
            "2": {
                "food": 23,
                "active": 33
            },
            "3": {
                "food": 8,
                "active": 40
            },
            "4": {
                "food": 11,
                "active": 36
            },
            "5": {
                "food": 16,
                "active": 30
            }
        }
    }
}
    testDataset = json.dumps(testDataset)
    context['testDataset'] = testDataset
    context['request'] = request
    # print(f'{request['startDate']}')
    # print(f'{request['endDate']}')

    # log.infod(request)
    return templates.TemplateResponse("graph.j2", context)



@router.post("/post")
async def create_item(form: Form):
    print(form)
    return form