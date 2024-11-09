#!/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/3/10
import rospy
from sensor_msgs.msg import CompressedImage
import cv2
import numpy as np
DATA_FOLDER='/media/huanyu/DATASET11'
def callback(data):
    # 将压缩的图像数据解码为OpenCV图像
    np_arr = np.frombuffer(data.data, np.uint8)
    image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    # 检查图像是否正确解码
    if image_np is not None:
        # 假设我们有一个全局的视频写入对象
        global out
        out.write(image_np)
    else:
        rospy.logerr("Failed to decode image!")

def main():
    rospy.init_node('simple_compressed_image_recorder', anonymous=True)
    global out
    out = cv2.VideoWriter(DATA_FOLDER+'/视频.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30.0, (640, 480))
    rospy.Subscriber("camera/rgb/image_raw/compressed", CompressedImage, callback)
    rospy.spin()

if __name__ == '__main__':
    main()