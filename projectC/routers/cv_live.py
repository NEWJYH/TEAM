from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import StreamingResponse

from stream.stream import get_stream_video

router = APIRouter(
    prefix="/cv_live"
)

templates = Jinja2Templates(directory="templates")

@router.get("/")
async def index(request:Request):
    # 보낼 request를 설정
    return templates.TemplateResponse("test.j2", context={"request": request})

@router.get("/stream_video")
async def stream_video():
    # StringResponse함수를 return하고,
    # 인자로 OpenCV에서 가져온 "바이트"이미지와 type을 명시
    return StreamingResponse(get_stream_video(), media_type="multipart/x-mixed-replace; boundary=frame")


