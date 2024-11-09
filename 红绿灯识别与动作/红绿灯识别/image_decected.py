# !/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/2/22 14:06

import cv2
import numpy as np
import distance_mm

def light_decected(image):
    image_copy=image.copy()#复制副本
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)#HSV色彩转变
    lower_white,upper_white=(np.array([0, 0, 170]),np.array([172, 120, 255]))#白色范围
    white_mask = cv2.inRange(hsv, lower_white, upper_white)#创建白色遮罩
    contours, _ = cv2.findContours(white_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#确定白色范围轮廓
    traffic_light_contour = max(contours, key=cv2.contourArea)#选择最大面积的轮廓
    x, y, w, h = cv2.boundingRect(traffic_light_contour)#计算轮廓的边界框
    #计算车与现在前方的距离
    distance=distance_mm.distance_far(image, h)
    which_color_image = image_copy[y:y + h, x:x + w]#截取出颜色路灯
    #设置红色，绿色HSV颜色范围
    hsv2 = cv2.cvtColor(which_color_image, cv2.COLOR_BGR2HSV)  # HSV色彩转变
    red_lower_bound, red_upper_bound = (np.array([0, 100, 100]), np.array([10, 255, 255]))#红色范围
    green_lower_bound, green_upper_bound = (np.array([40, 100, 100]), np.array([70, 255, 255]))#绿色范围
    red_mask = cv2.inRange(hsv2, red_lower_bound, red_upper_bound)#红色遮罩
    green_mask = cv2.inRange(hsv2, green_lower_bound, green_upper_bound)#绿色遮罩
    red_pixels = np.count_nonzero(red_mask)#红灯区域
    green_pixels = np.count_nonzero(green_mask)#绿灯区域
    light=None
    light_color=['R','Y','L']
    if red_pixels>green_pixels:
        print('前方为红灯')
        light=light_color[0]
    elif green_pixels > red_pixels:
        print("前方为绿灯")
        light = light_color[2]
    elif red_pixels == green_pixels:
        print("前方为黄灯")
        light = light_color[1]
    else:
        print("无法判断")
    return light,distance

#image = cv2.imread("/Users/jiazimo/PycharmProjects/Pycharm_graduation_design/红绿灯识别与动作/红绿灯识别/红绿灯数据集/test.jpg")
#light_decected(image)
