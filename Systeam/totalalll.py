#!/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/3/26

import cv2
import rospy
import numpy as np
from geometry_msgs.msg import Twist
from std_msgs.msg import String,Float64MultiArray
#
class AutonomousDriving:
    def __init__(self):
        self.speed_linear = 0
        self.speed_angular = 0
        self.light=''
        self.forword, self.back, self.right, self.left = 0, 0, 0, 0
        self.avoidance = False
        self.action_f = ''
        self.action_l = ''
        self.resl = ''
        self.light_sub = rospy.Subscriber('/light_info',String , self.Light)
        self.bizhang_sub = rospy.Subscriber('/avoidance_info',Float64MultiArray , self.Bizhang)
        self.selfdriving_sub = rospy.Subscriber('/selfdrive_info', Float64MultiArray, self.Selfdriving)
        self.full_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

    def Light(self, msg):
        self.light=msg.data
    def Bizhang(self,msg):
        forword,back,right,left= msg.data
        self.avoidance = self.right<=20 or self.left<=20
    def Selfdriving(self,msg):
        self.speed_linear=msg.data[0]
        self. speed_angular= msg.data[1]
    def publish_velocity(self):
        vel_msg = Twist()
        if self.light!='red':
            if self.avoidance:
                self.resl = '避障算法'
                if self.forword<=25:
                    self.speed_angular=0.5 if self.left>=self.right else -0.5
                    self.speed_linear = 0
                else:
                    self.speed_linear=0.2
                    self.speed_angular = 0
            else:
                self.resl='自动驾驶算法'
        else:
            vel_msg.linear.x = 0
            vel_msg.angular.z = 0
        vel_msg.linear.x = self.speed_linear
        vel_msg.angular.z = self.speed_angular
        self.full_pub.publish(vel_msg)
        self.print_info()

    def print_info(self):
        if self.speed_linear > 0:
            self.action_f = '前进'
        if self.speed_angular > 0:
            self.action_l = '左转'
        if self.speed_angular < 0:
            self.action_l = '右转'
        rospy.loginfo(f"FULL-SELF-DRIVE.V1----------------JYW"
                      f"    Light: {self.light},Obstacle:{self.avoidance}\n"
                      f"    Basis:{self.resl}\n"
                      f"    Action_L:{self.action_f},Action_L:{self.action_l}\n"
                      f"    Action_RLinearSpeed:{self.speed_linear},AngularSpeed:{self.speed_angular},")

def main():
    print('自动驾驶启动！！！！！！！！')
    rospy.init_node('autonomous_driving_node', anonymous=True)
    ad = AutonomousDriving()
    rate = rospy.Rate(10)  # 10Hz
    while not rospy.is_shutdown():
        ad.publish_velocity()
        rate.sleep()
    rospy.spin()

if __name__ == '__main__':
    main()
