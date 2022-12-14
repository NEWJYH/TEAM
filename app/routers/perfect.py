from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi import Request

router = APIRouter(
    prefix="/perfect"
)

templates = Jinja2Templates(directory="templates")

@router.get("/")
async def performance(request:Request):
    return templates.TemplateResponse("perfect.html", context={"request": request})


