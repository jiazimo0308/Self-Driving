#!/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/3/12
import os
import cv2
import numpy as np
from PIL import Image, ImageEnhance
from moviepy.editor import VideoFileClip


def process_frame(img):
    img = Image.fromarray(img)
    enhancer = ImageEnhance.Contrast(img)
    enhanced_img = enhancer.enhance(3)
    img = np.array(enhanced_img)
    img = cv2.GaussianBlur(img, (17, 17), 0)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    #height,width=img.shape
    #crop_height = int(height / 3)
    #img = img[crop_height:, :]
    #img = cv2.resize(img, (200, int(height * (200 / width))), interpolation=cv2.INTER_AREA)
    return img

if __name__ == "__main__":
    output = '全新二值化.mp4'     #输出视频文件
    clip = VideoFileClip("new.mp4")   #输入视频文件
    out_clip = clip.fl_image(process_frame)
    out_clip.write_videofile(output, audio=False)
