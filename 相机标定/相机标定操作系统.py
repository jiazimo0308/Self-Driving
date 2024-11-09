# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/1/19 20:57
import os
import rospy
import shutil
from sensor_msgs.msg import Joy,Image
from cv_bridge import CvBridge
import cv2

save_image=False
image_count=0
bridge = CvBridge()

# 检测遥控器是否要进行标定数据集拍照
def joy_callback():
    global save_image
    if data.buttons[3] == 1:
        save_image = True

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
#
def image_callback(msg):
    # 检测遥控器按键，开始进行拍照
    global image_count,save_image
    if save_image:# 如果为1则进行拍一张照片
        print('拍摄相机标定图片'+str(image_count))
        cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
        cv2.imwrite('/media/huanyu/DATASET1/calibration/calibration{}.jpg'.format(image_count), cv_image)
        image_count += 1
        save_image=False


def start():
    print('开始运行拍摄标定图片集')
    clear_folder('/media/huanyu/DATASET1/calibration/')
    rospy.init_node('image_capture', anonymous=True)
    rospy.Subscriber("/camera/rgb/image_raw", Image, image_callback)
    rospy.Subscriber("/joy", Joy, joy_callback)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        rate.sleep()
    rospy.spin()


if __name__ == '__main__':
    start()