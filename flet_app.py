# https://flet.dev/docs/controls/image

import flet as ft
import cv2
import base64
import numpy as np
import os
from utils import get_base64_img, get_datetime_now_str

root_dir = "data_by_flet_app"
target_dir = ""

def main(page: ft.Page):
    
    # page(アプリ画面)の設定
    page.title = "WEBCAM"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.INDIGO_50
    page.padding = 50
    page.window_height = 500
    page.window_width = 800


    def start_taking_photos(e):
        global target_dir
        print("start taking photos")
        now_str = get_datetime_now_str()
        target_dir = os.path.join(root_dir, now_str)
        os.makedirs(target_dir)
        start_button.visible=False
        camera_button.visible=True
        finish_button.visible=True

    def finish_taking_photos(e):
        print("finish taking photos")
        start_button.visible=True
        camera_button.visible=False
        finish_button.visible=False

    # 写真を撮る
    def take_a_photo(e):
        now_str = get_datetime_now_str()
        print(f"{now_str} take a photo")
        filepath = os.path.join(target_dir, f"{now_str}.jpg")
        print(filepath)
        cv2.imwrite(filepath, img)

    
    cap = cv2.VideoCapture(1)

    
    
    # 初期画像（ダミー）
    img_blank = 255*np.ones((300, 533, 3), dtype="uint8")
    img_h, img_w, _ = img_blank.shape
    image_display = ft.Image(src_base64=get_base64_img(img_blank),
                             width=img_w, height=img_h, fit=ft.ImageFit.CONTAIN)
    
    start_button = ft.ElevatedButton("Start",
                                    icon=ft.icons.START,
                                    visible=True,
                                    on_click=start_taking_photos)
    
    finish_button = ft.ElevatedButton("Finish",
                                    icon=ft.icons.STOP_CIRCLE_ROUNDED,
                                    visible=False,
                                    on_click=finish_taking_photos)  
    
    camera_button = ft.ElevatedButton("Photo",
                                    icon=ft.icons.CAMERA_ALT_ROUNDED,
                                    visible=False, 
                                    on_click=take_a_photo)
    
    
    buttons = ft.Column([
                        start_button,
                        camera_button,
                        finish_button
                        ])

    page.add(ft.Row([image_display, buttons]))


    page.update()
    
    while True:
        ret, img = cap.read()
        # print(ret)
        # img = cv2.resize(img, (img_w, img_h))
        image_display.src_base64 = get_base64_img(img)
        page.update()




# デスクトップアプリとして開く
ft.app(target=main)

# webアプリとして開く場合は任意のポート番号を指定し
# ブラウザでlocalhost:7777を開く
# ft.app(target=main, port=7777)
    