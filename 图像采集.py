# -*- coding: utf-8 -*-
# @Time    : 9/4/22 11:49 AM
# @Author  : ZhangP.H
# @File    : 图像采集.py
# @Software: PyCharm
import os

import cv2
import numpy as np
import time


def save_image(left_image, right_image, image, path="/home/zph/Pictures/stereo_usb_cam", tag=None):
    left_dir = os.path.join(path, "left")
    right_dir = os.path.join(path, "right")
    cam_dir = os.path.join(path, "cam")
    os.makedirs(left_dir, exist_ok=True)
    os.makedirs(right_dir, exist_ok=True)
    os.makedirs(cam_dir, exist_ok=True)
    t = time.time()
    print(t)
    cv2.imwrite("{}/{}_{}.jpg".format(left_dir, tag, t), left_image)
    cv2.imwrite("{}/{}_{}.jpg".format(right_dir, tag, t), right_image)
    cv2.imwrite("{}/{}_{}.jpg".format(cam_dir, tag, t), image)


def main():
    # 打开视频流或相机
    cap = cv2.VideoCapture(1)
    # 两个相机的视频流是合并在一起的， 需要手动设置size，不然只能显示一个相机
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        ret_val, img = cap.read()
        if ret_val:
            # print(img.shape)
            left_image = img[:, 640:1280, :]
            right_image = img[:, 0:640, :]
            img = np.hstack([left_image, right_image])
            cv2.imshow('usb cam', img)

            # 根据输入键确定功能
            key = cv2.waitKey(1) & 0xFF
            if key == ord('s'):
                save_image(left_image, right_image, img)
            elif key == 27:  # esc
                break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
