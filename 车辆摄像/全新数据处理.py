#!/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/3/15
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
    img2=img.copy()

    img = cv2.GaussianBlur(img, (17, 17), 0)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    height,width=img.shape
    crop_height = int(height / 3)
    img = img[crop_height:, :]
    img2 = img2[crop_height:, :]

    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(img, connectivity=8)
    sizes = stats[1:, -1]
    main_object_label = 1 + np.argmax(sizes)

    main_object = np.zeros_like(labels)
    main_object[labels == main_object_label] = 255
    img2[main_object == 255] = [0, 255, 0]

    new_img = np.zeros_like(img2)
    new_img[main_object == 255] = 255
    print(new_img.shape)
    img = cv2.resize(new_img, (200, int(height * (200 / width))), interpolation=cv2.INTER_AREA)
    print(img.shape)
    return img

if __name__ == "__main__":
    output = '最终识别.mp4'     #输出视频文件
    clip = VideoFileClip("new.mp4")   #输入视频文件
    out_clip = clip.fl_image(process_frame)
    out_clip.write_videofile(output, audio=False)