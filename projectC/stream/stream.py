import cv2
import time 
def get_stream_video():
    # camera 정의
    video_input_path = 'video/detect/ch3_rtsp.mp4'

    cam = cv2.VideoCapture(video_input_path)
    cnt = 0
    a = time.time()
    while True:
        cnt += 1
        # 카메라 값 불러오기
        success, frame = cam.read()

        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            # frame을 byte로 변경 후 특정 식??으로 변환 후에
            # yield로 하나씩 넘겨준다.
            frame = buffer.tobytes()
            print(cnt)
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(frame) + b'\r\n')
    b = time.time()
    print("time : ",b-a)