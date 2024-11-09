#!/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/3/8
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

def joy_callback(data):
    global start_collecting, stop_collecting
    if data.axes[6] == 1 and not start_collecting:
        start_collecting = True
        print('开始数据采集')
    elif data.axes[6] == -1:
        stop_collecting = True
        print('数据采集结束')

def callback_speed(twist_data):
    global start_collecting, stop_collecting,df
    if start_collecting and not stop_collecting:
        df.append('time: {}, linear_x: {}, angular_z: {}'.format(rospy.get_time(), twist_data.linear.x, twist_data.angular.z))
        print('采集到数据量为:'+str(len(df)))
    if start_collecting and stop_collecting and df:
        start_collecting = False
        stop_collecting = False
        with open(LABEL_FILE, 'w') as f:
            for line in df:
                f.write(line + '\n')
        df=[]
def callback_image():
    global start_collecting, stop_collecting
    if start_collecting and not stop_collecting:
        np_arr = np.frombuffer(image_data.data, np.uint8)
        cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        cv2.imwrite(IMAGE_FOLDER + '/{}.jpg'.format(rospy.get_time()), cv_image)

def start():
    print('开始运行')
    clear_folder(IMAGE_FOLDER)
    clear_label_file()
    rospy.init_node('data_collector')
    joy_sub = rospy.Subscriber('/joy', Joy,joy_callback)
    image_sub = rospy.Subscriber('/camera/rgb/image_raw/compressed', CompressedImage,callback_image)
    twist_sub = rospy.Subscriber('/cmd_vel', Twist,callback_speed)
    rospy.spin()

if __name__ == '__main__':
    start()