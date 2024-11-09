#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Jiazimo
# @Time : 2024/2/15 10:48

#车辆轨迹记录
import rospy
from nav_msgs.msg import Odometry
import tf

trajectory_file=None
def odometry_callback(data):
    global trajectory_file
    # 获取小车的位置
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    z = data.pose.pose.position.z
    # 获取小车的方向
    quaternion = (
        data.pose.pose.orientation.x,
        data.pose.pose.orientation.y,
        data.pose.pose.orientation.z,
        data.pose.pose.orientation.w)
    euler = tf.transformations.euler_from_quaternion(quaternion)
    yaw = euler[2]
    # 使用with语句写入文件
    trajectory_file.write("{},{},{},{},{}\n".format(rospy.get_time(), x, y, z, yaw))


def listener():
    global sub,trajectory_file
    file_path = '/media/huanyu/DATASET11/guiji/trajectory.txt'
    trajectory_file=open(file_path,'w')
    rospy.init_node('trajectory_recorder', anonymous=True)
    sub=rospy.Subscriber('odom', Odometry, odometry_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
