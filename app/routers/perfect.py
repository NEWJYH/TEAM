from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi import Request

router = APIRouter(
    prefix="/perfect"
)

templates = Jinja2Templates(directory="templates")

@router.get("/")
async def performance(request:Request):
    # 영상 한개 넣을것 cctv3개 합쳐진 좌표
    return templates.TemplateResponse("live.html", context={"request": request})


