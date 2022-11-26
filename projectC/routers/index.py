from fastapi import APIRouter, Depends, status, HTTPException, Response , Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from repository import index

from fastapi import  Request
from LOG import log

router = APIRouter(
    prefix="/graph"
)

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def get_test(request: Request ):
    context = index.get_test()
    context['request'] = request
    # log.infod(request)
    return templates.TemplateResponse("graph.j2", context)




