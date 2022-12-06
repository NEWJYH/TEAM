import cv2
import time

async def get_stream_video():
    # camera 정의
    video_input_path = 'static/video/detect/ch3_rtsp.mp4'
    # cam = cv2.VideoCapture('rtsp://192.168.70.209:9876/cow')
    cam = cv2.VideoCapture(video_input_path)
    while True:
        # 카메라 값 불러오기
        success, frame = cam.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            # frame을 byte로 변경 후 특정 식??으로 변환 후에
            # yield로 하나씩 넘겨준다.
            frame = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(frame) + b'\r\n')

async def get_stream_video2():
    # camera 정의
    video_input_path = 'static/video/map/test.mp4'
    # cam = cv2.VideoCapture('rtsp://192.168.70.209:9876/cow')
    cam = cv2.VideoCapture(video_input_path)
    while True:
        # 카메라 값 불러오기
        success, frame = cam.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            # frame을 byte로 변경 후 특정 식??으로 변환 후에
            # yield로 하나씩 넘겨준다.
            frame = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(frame) + b'\r\n')



# async def get_stream_video():
#     # camera 정의
#     video_input_path = 'video/detect/ch3_rtsp.mp4'
#     cam = cv2.VideoCapture(video_input_path)
#     while True:
#         # 카메라 값 불러오기
#         success, frame = cam.read()
#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame)
#             # frame을 byte로 변경 후 특정 식??으로 변환 후에
#             # yield로 하나씩 넘겨준다.
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(frame) + b'\r\n')