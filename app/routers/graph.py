from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

import schemas 

from repository import graph

router = APIRouter(
    prefix="/graph",
    tags=['graphs']
)

router.mount('/static', StaticFiles(directory='static'), name='static')

@router.get("/", response_class=HTMLResponse)
async def graph_html(request: Request):
    return graph.graph_html(request)

@router.post('/post')
async def graph_query(form:schemas.Form):
   return graph.graph_query(form)
   