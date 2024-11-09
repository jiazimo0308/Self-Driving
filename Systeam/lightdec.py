#!/usr/bin/env python3
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/3/26
import cv2
import rospy
import numpy as np
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import String


class LightrNode:
    def __init__(self):
        self.camer_sub = rospy.Subscriber('/camera/rgb/image_raw/compressed', CompressedImage,self.light_decected)
        self.light_pub = rospy.Publisher('light_info', String, queue_size=10)
        self.height = 480
        self.width = 640
        self.camera_matrix = np.array(
            [[623.8586354204893, 0.0, 330.46207618626505], [0.0, 623.2426495788945, 246.8463868100791],
             [0.0, 0.0, 1.0]])
        self.light = None

    def light_decected(self, msg):
        np_arr = np.frombuffer(msg.data, np.uint8)
        cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        mid_width = self.width // 2
        image = cv_image[0:self.height, mid_width:self.width]
        image_copy = image.copy()
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_white, upper_white = (np.array([0, 0, 170]), np.array([172, 120, 255]))
        white_mask = cv2.inRange(hsv, lower_white, upper_white)
        contours, _ = cv2.findContours(white_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        traffic_light_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(traffic_light_contour)
        focal_length = self.camera_matrix[0, 0]
        distance = (80 * focal_length) / h
        if distance * 0.1 <= 260:
            which_color_image = image_copy[y:y + h, x:x + w]
            hsv2 = cv2.cvtColor(which_color_image, cv2.COLOR_BGR2HSV)
            red_lower_bound, red_upper_bound = (np.array([0, 100, 100]), np.array([10, 255, 255]))
            green_lower_bound, green_upper_bound = (np.array([40, 100, 100]), np.array([70, 255, 255]))
            red_mask = cv2.inRange(hsv2, red_lower_bound, red_upper_bound)
            green_mask = cv2.inRange(hsv2, green_lower_bound, green_upper_bound)
            red_pixels = np.count_nonzero(red_mask)
            green_pixels = np.count_nonzero(green_mask)
            light_color = ['红灯', '绿灯', '无信号']
            if red_pixels > green_pixels:
                self.light = light_color[0]
            elif green_pixels > red_pixels:
                self.light = light_color[1]
            else:
                self.light = light_color[2]
        msg = String()
        msg.data = self.light
        # 发布消息
        self.light_pub.publish(msg)

def main():
    rospy.init_node('light_info', anonymous=True)
    ln = LightrNode()
    rospy.spin()

if __name__ == '__main__':
    main()