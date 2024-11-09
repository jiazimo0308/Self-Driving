# -*- coding: utf-8 -*-
# @Author : Jiazimo
# @Time : 2024/1/19 16:06

#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

received = False

def callback(data):
    global received
    # 如果已经收到过数据，就不再处理新的数据
    if received:
        return
    received = True
    # 打开文件
    with open('/media/huanyu/DATASET1/Laserdata/scan_data.txt', 'w') as f:
        for i, range in enumerate(data.ranges):
            # 检查数据是否有效，这里假设非有效距离（无回波或太近）被设为 inf
            if not rospy.is_shutdown() and not range == float('Inf'):
                # 计算角度
                angle = data.angle_min + i * data.angle_increment
                # 将距离和角度写入文件
                f.write('{}, {}\n'.format(angle, range))

def listener():
    print('开始数据采集')
    rospy.init_node('listener', anonymous=True)
    # 订阅激光雷达的话题，这里需要替换为你的激光雷达话题
    rospy.Subscriber("/scan", LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()


#/media/huanyu/DATASET1/Laserdata/scan_data.txt