# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/1/19 16:06

#!/usr/bin/env python
# -*- coding: utf-8 -*
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
MIN_SPEED_LEVEL=0
MAX_SPEED_LEVEL=3
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
            print(f'删除失败 %s. 原因如下: %s' % (file_path, e))

def clear_label_file():
    open(LABEL_FILE,'w').close()

speed_level = 0#初始速度
start_collecting = False#数据收集开始
stop_collecting = False#数据收集结束
df=[]#运行数据记录
class JoyControl:
    def __init__(self):
        self.speed_level = 0
        self.start_collecting = False
        self.stop_collecting = False
        self.df=[]
        rospy.init_node('joy_control',anonymous=True)
        self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        joy_sub = message_filters.Subscriber("joy", Joy)
        image_sub = message_filters.Subscriber("/camera/rgb/image_raw/compressed", CompressedImage)
        ts = message_filters.ApproximateTimeSynchronizer([joy_sub, image_sub], 10, 0.001)
        ts.registerCallback(self.callback)

    def callback(self,data,image_data):
        global speed_level, start_collecting, stop_collecting
        twist=Twist()
        if data.axes[7] == 1:
            self.speed_level += 1
        elif data.axes[7] == -1:
            self.speed_level -= 1
        self.speed_level=max(MIN_SPEED_LEVEL,min(MAX_SPEED_LEVEL,self.speed_level))
        print('当前速度档位为:', self.speed_level)
        if data.axes[6] == 1 and not self.start_collecting:
            self.start_collecting=True
            print('开始数据采集')
        elif data.axes[6]==-1:
            self.stop_collecting=True
            print('数据采集结束')
        twist.linear.x = data.axes[1] * 0.2 * self.speed_level
        twist.angular.z = data.axes[2] * 0.5 * self.speed_level
        self.pub.publish(twist)
        if self.start_collecting and not self.stop_collecting:
            time_stamp = rospy.get_time()
            self.df.append('time: {}, linear_x: {}, angular_z: {}'.format(time_stamp, twist.linear.x, twist.angular.z))
            np_arr = np.frombuffer(image_data.data, np.uint8)
            cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            cv2.imwrite(f'{IMAGE_FOLDER}/{time_stamp}.jpg', cv_image)

        if self.start_collecting and self.stop_collecting and self.df:
            self.start_collecting=False
            self.stop_collecting=False
            with open (LABEL_FILE,'w') as f:
                for line in self.df:
                    f.write(line+'\n')
            self.df=[]
    def start(self):
        clear_folder(IMAGE_FOLDER)
        clear_label_file()
        print('开始运行')
        rate=rospy.Rate(200)
        while not rospy.is_shutdown():
            rate.sleep()

if __name__ == '__main__':
    controller = JoyControl()
    controller.start()






