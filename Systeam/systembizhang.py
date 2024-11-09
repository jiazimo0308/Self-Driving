#!/usr/bin/env python3
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/3/26
import rospy
import math
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float64MultiArray

def four_distence(right_left):
    pos = [i for i in right_left if i > 0]
    neg = [i for i in right_left if i < 0]
    full_pos = max(pos) if pos else 0
    full_neg = abs(max(neg)) if neg else 0
    return full_pos, full_neg

def distance(x_coords, y_coords):
    right_left = []
    forword_back = []
    for x1, y1 in zip(x_coords, y_coords):
        if -0.13 <= x1 <= 0.13:
            right_left.append(y1)
        if -0.115 <= y1 <= 0.115:#0.115
            forword_back.append(x1)
    right, left = four_distence(right_left)
    back, forword = four_distence(forword_back)
    return forword, back, right, left

class LaserNode:
    def __init__(self):
        self.laser_sub = rospy.Subscriber('/scan', LaserScan, self.laser_callback)
        self.avoidance_pub = rospy.Publisher('avoidance_info', Float64MultiArray, queue_size=10)

    def laser_callback(self, msg):
        points_x = []
        points_y = []
        for i, range in enumerate(msg.ranges):
            if range != float('Inf'):
                angle = msg.angle_min + i * msg.angle_increment  # 计算角度
                # 极坐标与直角坐标进行转换
                x = float(range) * math.cos(float(angle))  # 计算 x 坐标
                y = float(range) * math.sin(float(angle))  # 计算 y 坐标
                points_x.append(x)
                points_y.append(y)
        self.forword, self.back, self.right, self.left = distance(points_x, points_y)
        # 创建一个新的Float64MultiArray消息
        msg = Float64MultiArray()
        msg.data = [self.forword, self.back, self.right, self.left]
        self.avoidance_pub.publish(msg)
def main():
    print('红绿灯识别系统启动...')
    rospy.init_node('laser_node', anonymous=True)
    ln = LaserNode()
    rospy.spin()

if __name__ == '__main__':
    main()


