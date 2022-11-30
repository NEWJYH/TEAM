from fastapi import APIRouter, Response , Request
from fastapi.templating import Jinja2Templates

from pathlib import Path
from fastapi import Request, Response
from fastapi import Header
from fastapi.templating import Jinja2Templates
from fastapi import  Request

router = APIRouter(
    prefix="/video"
)

templates = Jinja2Templates(directory="templates")

CHUNK_SIZE = 1024*1024
# video_path = Path("test_sample.webm")
mapvideo_path = Path("test.webm")


@router.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("test.j2", context={"request": request})

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
#         return Response(data, status_code=206, headers=headers, media_type="video/webm")

@router.get("/mapvideo")
async def video_endpoint(range: str = Header(None)):
    start, end = range.replace("bytes=", "").split("-")
    start = int(start)
    end = int(end) if end else start + CHUNK_SIZE
    with open(mapvideo_path, "rb") as video:
        video.seek(start)
        data = video.read(end - start)
        filesize = str(mapvideo_path.stat().st_size)
        headers = {
            'Content-Range': f'bytes {str(start)}-{str(end)}/{filesize}',
            'Accept-Ranges': 'bytes'
        }
        return Response(data, status_code=206, headers=headers, media_type="video/webm")


# if "chrome" in request.headers.get("sec-ch-ua", "NO_MATCH").lower():
        #     data = video.read()
        # else:
        #     data = video.read(end - start)

# headers = {
        #     'Content-Range': f'bytes {str(start)}-{str(end)}/{filesize}',
        #     'Accept-Ranges': 'bytes'
        # }


# @router.get("/video")
# async def video_endpoint(range: str = Header(None)):
#     start, end = range.replace("bytes=", "").split("-")
#     start = int(start)
#     end = int(end) if end else start + CHUNK_SIZE
#     with open(video_path, "rb") as video:
#         video.seek(start)
#         data = video.read(end - start)
#         filesize = video_path.stat().st_size
        
#         if end >= filesize:
#             end = filesize - 1
        
#         headers = {
#             'Content-Range': f'bytes {str(start)}-{str(end)}/{str(filesize)}',
#             'Accept-Ranges': 'bytes'
#         }
#         return Response(data, status_code=206, headers=headers, media_type="video/mp4")