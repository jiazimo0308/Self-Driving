# !/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/2/21 20:44
import cv2
import numpy as np
# 加载图像
image = cv2.imread("/Users/jiazimo/PycharmProjects/Pycharm_graduation_design/红绿灯识别与动作/红绿灯识别/红绿灯数据集/红绿灯4.jpg")
height, width = image.shape[:2]
mid_width = width // 2
# 裁剪图像的右半部分
# OpenCV中的图像格式为[rows, cols]
image = image[0:height, mid_width:width]
image_copy=image.copy()
# 转换到HSV色彩空间
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# 定义白色的HSV范围
lower_white = np.array([0, 0, 170])
upper_white = np.array([172, 120, 255])
# 创建掩模以只保留白色
mask = cv2.inRange(hsv, lower_white, upper_white)
cv2.imwrite("mask.png", mask)
# 寻找白色区域的轮廓
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
traffic_light_contour = max(contours, key=cv2.contourArea)
# 计算轮廓的边界框
x, y, w, h = cv2.boundingRect(traffic_light_contour)
# 在原图上绘制边界框
which_color_image = image_copy[y:y+h, x:x+w]#差分出的灯色
#cv2.imwrite("绿灯.png", which_color_image)
cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
# 红色和绿色和黄色的RGB空间
hsv2= cv2.cvtColor(which_color_image, cv2.COLOR_BGR2HSV)
red_lower_bound, red_upper_bound = (np.array([0, 100, 100]), np.array([0, 255, 255]))
green_lower_bound, green_upper_bound = (np.array([40, 100, 100]), np.array([70, 255, 255]))#(np.array([35, 50, 50]), np.array([85, 255, 255]))

red_mask = cv2.inRange(hsv2, red_lower_bound, red_upper_bound)
green_mask = cv2.inRange(hsv2, green_lower_bound, green_upper_bound)

#cv2.imwrite("绿灯遮罩.png", green_mask)
# 检测红灯、黄灯和绿灯区域
red_pixels = np.count_nonzero(red_mask)
green_pixels = np.count_nonzero(green_mask)

# 判断红灯、黄灯和绿灯
if  red_pixels > green_pixels:
    print("这张图片是红灯")
elif green_pixels > red_pixels:
    print("这张图片是绿灯")
elif  red_pixels==green_pixels:
    print("这张图片是黄灯")
else:
    print("无法判断")

# 将距离显示在图像上
#cv2.putText(image, f"Distance: {distance} mm", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
# 显示图像
cv2.imwrite("hld.png", image)
#黄，绿，红
#1，0，40
#10，142，7