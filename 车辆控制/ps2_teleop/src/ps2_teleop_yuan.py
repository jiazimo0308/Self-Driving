#!/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/3/10
import os
import cv2
import shutil
import rospy
import numpy as np
import message_filters
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy,CompressedImage

DATA_FOLDER='/media/huanyu/DATASET11'
IMAGE_FOLDER=DATA_FOLDER+"/get_image"
LABEL_FILE=DATA_FOLDER+"/label.txt"
start_collecting = False#数据收集开始
stop_collecting = False#数据收集结束
df=[]#运行数据记录
speed_level=0
#运行前清空一次文件夹
def clear_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('删除失败')

def clear_label_file():
    open(LABEL_FILE,'w').close()

def callback(data,image_data):
    global speed_level,start_collecting,stop_collecting,df
    if data.axes[7] == 1:
        speed_level += 1
    elif data.axes[7] == -1:
        speed_level -= 1
    speed_level = max(0, min(3, speed_level))
    print('当前速度档位为:' + str(speed_level))
    if data.axes[6] == 1:
        start_collecting = True
        print('开始数据采集')
    elif data.axes[6] ==-1:
        stop_collecting = True
        print('停止数据采集')

    twist = Twist()
    twist.linear.x = data.axes[1] * 0.2* speed_level  # 前进和后退
    twist.angular.z = data.axes[2] * 0.5 * speed_level  # 左右转向
    pub.publish(twist)

    if start_collecting and not stop_collecting:
        timestamp1 = int(rospy.get_time() * 100)
        df.append('time: {}, linear_x: {}, angular_z: {}'.format(timestamp1,  twist.linear.x, twist.angular.z))
        print('采集到数据量为:' + str(len(df)))
        np_arr = np.frombuffer(image_data.data, np.uint8)
        cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        timestamp2 = int(rospy.get_time() * 100)
        cv2.imwrite(IMAGE_FOLDER + '/{}.jpg'.format(timestamp2), cv_image)
    if start_collecting and stop_collecting and df:
        start_collecting = False
        stop_collecting = False
        with open(LABEL_FILE, 'w') as f:
            for line in df:
                f.write(line + '\n')
        df = []

def start():
    print('开始运行')
    global pub
    clear_folder(IMAGE_FOLDER)
    clear_label_file()
    rospy.init_node('joy_control')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=30)
    joy_sub = message_filters.Subscriber("joy", Joy)
    image_sub = message_filters.Subscriber('/camera/rgb/image_raw/compressed', CompressedImage)
    ts = message_filters.ApproximateTimeSynchronizer([joy_sub, image_sub], 1,1)
    ts.registerCallback(callback)
    rospy.spin()

if __name__ == '__main__':
    start()
