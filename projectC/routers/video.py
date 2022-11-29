from fastapi import APIRouter, Depends, status, HTTPException, Response , Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
# from repository import index


from pathlib import Path
from fastapi import FastAPI
from fastapi import Request, Response
from fastapi import Header
from fastapi.templating import Jinja2Templates


from fastapi import  Request

from stream.stream import get_stream_video
from fastapi.responses import StreamingResponse

router = APIRouter(
    prefix="/video"
)

templates = Jinja2Templates(directory="templates")

CHUNK_SIZE = 1024*1024
video_path = Path("./video/detect/cowfarmB_ch1_2022072519_003.mp4")


@router.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("test.html", context={"request": request})


@router.get("/video")
async def video_endpoint(range: str = Header(None)):
    print('응답이 왔어요')
    print(range)
    start, end = range.replace("bytes=", "").split("-")
    # print(start, end)
    start = int(start)
    end = int(end) if end else start + CHUNK_SIZE
    with open(video_path, "rb") as video:
        video.seek(start)
        data = video.read(end - start)
        filesize = str(video_path.stat().st_size)
        headers = {
            'Content-Range': f'bytes {str(start)}-{str(end)}/{filesize}',
            'Accept-Ranges': 'bytes'
        }
        return Response(data, status_code=206, headers=headers, media_type="video/mp4")





