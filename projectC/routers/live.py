from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import StreamingResponse
from fastapi.responses import HTMLResponse
from pathlib import Path
from fastapi import Request, Response
from fastapi import Header


from stream.stream import get_stream_video, get_stream_video2

router = APIRouter(
    prefix="/live"
)

templates = Jinja2Templates(directory="templates")

@router.get("/")
async def index(request:Request):
    # 보낼 request를 설정
    return templates.TemplateResponse("test.j2", context={"request": request})


@router.get("/stream_video")
async def stream_video(request:Request):
    # StringResponse함수를 return하고,
    # 인자로 OpenCV에서 가져온 "바이트"이미지와 type을 명시
    return StreamingResponse(get_stream_video(), media_type="multipart/x-mixed-replace; boundary=frame")

@router.get("/stream_video2")
async def stream_video2(request:Request):
    # StringResponse함수를 return하고,
    # 인자로 OpenCV에서 가져온 "바이트"이미지와 type을 명시
    return StreamingResponse(get_stream_video2(), media_type="multipart/x-mixed-replace; boundary=frame")


# CHUNK_SIZE = 1024*1024
# video_path = Path("ch3_rtsp.mp4")
# mapvideo_path = Path("test.mp4")

# @router.get("/mapvideo")
# async def video_endpoint(range: str = Header(None)):
#     start, end = range.replace("bytes=", "").split("-")
#     start = int(start)
#     end = int(end) if end else start + CHUNK_SIZE
#     with open(mapvideo_path, "rb") as video:
#         video.seek(start)
#         data = video.read(end - start)
#         filesize = str(mapvideo_path.stat().st_size)
#         headers = {
#             'Content-Range': f'bytes {str(start)}-{str(end)}/{filesize}',
#             'Accept-Ranges': 'bytes'
#         }
#         return Response(data, status_code=206, headers=headers, media_type="video/mp4")



# from fastapi import APIRouter, Response , Request
# from fastapi.templating import Jinja2Templates

# from fastapi import Header
# from fastapi.templating import Jinja2Templates
# from fastapi import  Request

# CHUNK_SIZE = 1024*1024

# @router.get("/")
# async def read_root(request: Request):
#     return templates.TemplateResponse("test.j2", context={"request": request})

# @router.get("/video")
# async def video_endpoint(range: str = Header(None)):
#     start, end = range.replace("bytes=", "").split("-")
#     start = int(start)
#     end = int(end) if end else start + CHUNK_SIZE
#     with open(video_path, "rb") as video:
#         video.seek(start)
#         data = video.read(end - start)
#         filesize = str(video_path.stat().st_size)
#         headers = {
#             'Content-Range': f'bytes {str(start)}-{str(end)}/{filesize}',
#             'Accept-Ranges': 'bytes'
#         }
#         return StreamingResponse(data, status_code=206, headers=headers, media_type="video/webm")