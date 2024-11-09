# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/1/19 16:06

#!/usr/bin/env python
# -*- coding: utf-8 -*
import os
import rospy
import cv2
import shutil
import message_filters
from cv_bridge import CvBridge
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy,Image
from nav_msgs.msg import Odometry
import tf

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
            print('删除失败 %s. 原因如下: %s' % (file_path, e))


speed_level = 0#初始速度
start_collecting = False#数据收集开始
stop_collecting = False#数据收集结束
df=[]#运行数据记录
df_1=[]

def callback(data,image_data,data_track):
    #print(data)#具体按键的操控信息
    #速度信息
    global speed_level,start_collecting,stop_collecting,df,df_1
    twist = Twist()
    # 检测按键输入，改变速度档次
    if data.axes[7] == 1:  # 7上用于加速
        speed_level += 1
    elif data.axes[7] == -1:  # 7下用于减速
        speed_level -= 1
    print('当前速度档位为:'+str(speed_level))
    # 限制速度档次在0-3之间
    speed_level = max(0, min(3, speed_level))

    #检测遥控器输入分别为开始数据收集与结束数据收集
    if data.axes[6] == 1:  # 假设按钮0用于开始收集数据
        start_collecting = True
        print('开始数据采集')
    elif data.axes[6] ==-1:  # 假设按钮1用于停止收集数据
        stop_collecting = True
        print('停止数据采集')
        with open('/media/huanyu/DATASET1/label.txt','w') as f:
            for line in df:
                f.write(line+'\n')

        with open('/media/huanyu/DATASET1/guiji/trajectory.txt','w') as trajectory_file:
            for line2 in df_1:
                trajectory_file.write(line2+'\n')

    #设置速度窗口
    twist = Twist()
    twist.linear.x = data.axes[1] * 0.4 * speed_level  # 前进和后退
    twist.angular.z = data.axes[2] * 0.7 * speed_level  # 左右转向
    pub.publish(twist)
    #保存两个速度到指定的csv文件里
    if start_collecting and not stop_collecting:
        df.append('time: {}, linear_x: {}, angular_z: {}'.format(rospy.get_time(), twist.linear.x, twist.angular.z))
        bridge = CvBridge()
        cv_image = bridge.imgmsg_to_cv2(image_data, "bgr8")
        cv2.imwrite('/media/huanyu/DATASET1/get_image/{}.jpg'.format(rospy.get_time()), cv_image)
        # 获取小车的位置
        x = data_track.pose.pose.position.x
        y = data_track.pose.pose.position.y
        z = data_track.pose.pose.position.z
        # 获取小车的方向
        quaternion = (
            data_track.pose.pose.orientation.x,
            data_track.pose.pose.orientation.y,
            data_track.pose.pose.orientation.z,
            data_track.pose.pose.orientation.w)
        euler = tf.transformations.euler_from_quaternion(quaternion)
        yaw = euler[2]
        df_1.append("{},{},{},{},{}".format(rospy.get_time(), x, y, z, yaw))

#主函数
def start():
    print('开始运行')
    global pub
    clear_folder('/media/huanyu/DATASET1/get_image/')
    rospy.init_node('joy_control')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=30)
    #rospy.Subscriber("joy", Joy, callback)
    #rospy.Subscriber("camera/rgb/image_raw", Image, image_callback)
    joy_sub=message_filters.Subscriber("joy",Joy)
    image_sub=message_filters.Subscriber("camera/rgb/image_raw",Image)
    #odom_sub=message_filters.Subscriber('odom',Odometry)
    #imu_sub = message_filters.Subscriber("/mobile_base/sensors/imu_data", Imu)
    ts = message_filters.ApproximateTimeSynchronizer([joy_sub, image_sub], 1,1)#message_filters.ApproximateTimeSynchronizer#message_filters.TimeSynchronizer
    ts.registerCallback(callback)
    rate=rospy.Rate(200)#10hz
    #rospy.spin()
    while not rospy.is_shutdown():
        rate.sleep()
    rospy.spin()


if __name__ == '__main__':
    start()
