from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi import Request

router = APIRouter(
    prefix="/performance"
)

templates = Jinja2Templates(directory="templates")

@router.get("/")
async def performance(request:Request):
    # 보낼 request를 설정
    # 여기 변경하면됨 html
    # 영상 2개 들어갈 html임
    return templates.TemplateResponse("live.html", context={"request": request})


