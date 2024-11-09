#!/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/3/24
import os
import cv2
import numpy as np
import joblib
from moviepy.editor import VideoFileClip

def process_frame(img):
    height,width,_=img.shape
    start_row, start_col = int(height * .3), int(width * .0)
    end_row, end_col = int(height * .7), int(width * 1.0)
    img = img[start_row:end_row, start_col:end_col]
    copy_img=img.copy()
    white_pixels = np.where(copy_img > 200)
    x = img.reshape(1, -1)

    model = joblib.load('auto_play.m')
    pred = model.predict(x/255)

    if pred==1:
        copy_img[white_pixels[0], white_pixels[1], :] = [0, 255, 0]
    else:
        copy_img[white_pixels[0], white_pixels[1], :] = [255, 0, 0]
    return copy_img

if __name__ == "__main__":
    output = '直线测试.mp4'     #输出视频文件
    clip = VideoFileClip("最终识别.mp4")   #输入视频文件
    out_clip = clip.fl_image(process_frame)
    out_clip.write_videofile(output, audio=False)
