# !/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/2/22 14:20
import cv2
import numpy as np

def distance_far(image,h):
    camera_matrix = np.array([[623.8586354204893, 0.0, 330.46207618626505], [0.0, 623.2426495788945, 246.8463868100791], [0.0, 0.0, 1.0]])
    dist_coeffs = np.array([[-0.02090816022393141, 1.7020867956355417, 0.0034673454908852124, 0.00018072299007780134, -5.6789834764659215]])
    undistorted_image = cv2.undistort(image, camera_matrix, dist_coeffs)
    real_height_of_traffic_light=80# 假设红绿灯的真实高度
    # 估计距离
    focal_length = camera_matrix[0, 0]
    distance = (real_height_of_traffic_light * focal_length) / h
    print(f"距离红绿灯距离为: {distance*0.1} mm")
    return distance
