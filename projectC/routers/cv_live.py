from fastapi import APIRouter, Depends, status, HTTPException, Response , Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
# from repository import index

from fastapi import  Request

from stream.stream import get_stream_video
from fastapi.responses import StreamingResponse

router = APIRouter(
    prefix="/live"
)

templates = Jinja2Templates(directory="templates")

# openCV에서 이미지 불러오는 함수
def video_streaming():
    return get_stream_video()

@router.get("/")
def main():
    # StringResponse함수를 return하고,
    # 인자로 OpenCV에서 가져온 "바이트"이미지와 type을 명시
    return StreamingResponse(video_streaming(), media_type="multipart/x-mixed-replace; boundary=frame")




