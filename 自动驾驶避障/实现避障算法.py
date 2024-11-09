#!/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/2/15 16:08
import rospy
import math
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

#前后左右距离计算
def four_distence(what_list):
    po = []  # 正数
    neg = []  # 负数
    for j in what_list:
        if j > 0:
            po.append(j)
        if j < 0:
            neg.append(j)
    full_po = min(po)
    full_neg = abs(max(neg))
    return full_po, full_neg

# 判断小距离障碍物的位置
def distance(x_coords, y_coords):
    right_left = []
    forword_back = []
    for x1, y1 in zip(x_coords, y_coords):
        if -0.13 <= x1 <= 0.13:
            right_left.append(y1)
        if -0.115 <= y1 <= 0.115:
            forword_back.append(x1)
    # 获取前后左右距离障碍物的距离
    right, left = four_distence(right_left)
    back, forword = four_distence(forword_back)
    return forword, back, right, left

def xingshi(msg):
    global speed_linear,speed_angular
    speed_linear = msg.data[0]
    speed_angular = msg.data[1]

#避障函数
def bizhang_contrlle():
    #根据距离进行避障
    global forword,back,right,left,cmd_vel_publisher,speed_linear,speed_angular
    command = Twist()
    # 确定阈值报警动作范围
    if right<=0.25 or left<=0.25:
        if forword <= 0.25:  # 进入预警区
            if left >= right:  # 并进行避障(向左转向)
                command.angular.z = 0.5  # 设置一个正值来向左转
                print('向左转弯')
            else:
                command.angular.z = -0.5
                print('向右转弯')
        else:
            command.linear.x = 0.2
            print('直行')
    else:
        command.linear.x=speed_linear
        command.angular.z= speed_angular

    cmd_vel_publisher.publish(command)

#使用激光雷达
def Lasercallback(data_Laser):#激光雷达召回参数
    points_x = []
    points_y = []
    for i ,range in enumerate(data_Laser.ranges):
        # 检查数据是否有效，这里假设非有效距离（无回波或太近）被设为 inf
        if range!=float('Inf'):
            angle = data_Laser.angle_min + i * data_Laser.angle_increment#计算角度
            #极坐标与直角坐标进行转换
            x = float(range) * math.cos(float(angle))  # 计算 x 坐标
            y = float(range) * math.sin(float(angle))  # 计算 y 坐标
            points_x.append(x)
            points_y.append(y)
    #四方距离进行计算(并定义为全局变量)
    global forword,back,right,left
    forword,back,right,left=distance(points_x,points_y)
    #print(forword,back,right,left)
    #进行避障
    bizhang_contrlle()

def stop_robot():
    global cmd_vel_publisher
    command = Twist()  # 初始化速度命令变量
    cmd_vel_publisher.publish(command)  # 发送停止命令
    rospy.loginfo("Stop command has been sent.")

def listener():
    global cmd_vel_publisher
    rospy.init_node('listener', anonymous=True)
    #订阅激光雷达和驱动的话题
    cmd_vel_publisher = rospy.Publisher('/cmd_vel', Twist,queue_size=10)
    rospy.Subscriber("/scan", LaserScan, Lasercallback)
    rospy.Subscriber("/selfdrive_info", Float64MultiArray,)
    rospy.on_shutdown(stop_robot)  # 注册停止机器人的函数为关闭回调
    rospy.spin()

if __name__ == '__main__':
    listener()


