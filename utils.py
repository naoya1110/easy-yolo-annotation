import cv2
import base64
from datetime import datetime

def get_base64_img(img):
    _, encoded = cv2.imencode(".jpg", img)
    img_base64 = base64.b64encode(encoded).decode("ascii")
    return img_base64


def scan_cap_devices():
    cap_devices = []
    for i in range(10):
        try:
            cap = cv2.VideoCapture(i)
            ret, frame = cap.read()
            if ret:
                cap_devices.append(i)
            cap.release()
        
        except:
            pass
    return cap_devices

def get_datetime_now_str():
    now = datetime.now()
    now_str = now.strftime("%Y%m%d_%H%M%S")
    return now_str