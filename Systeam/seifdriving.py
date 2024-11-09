#!/usr/bin/env python3
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/3/26
import cv2
import rospy
import numpy as np
import math
import tensorflow as tf
from PIL import ImageEnhance,Image
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import Float64MultiArray
import joblib
#
class AutonomousDriving:
    def __init__(self):
        self.model = tf.keras.models.load_model('/home/huanyu/robot_ws/src/ps2_teleop/src/NIVIDA_fenlei.h5', compile=False)
        self.camar_sub = rospy.Subscriber('/camera/rgb/image_raw/compressed', CompressedImage, self.image_callback)
        self.selfdrive_pub = rospy.Publisher('selfdrive_info', Float64MultiArray, queue_size=10)
        self.height = 480
        self.width = 640
        self.crop_height = int(self.height / 3)
        self.resize_height = int(self.height * (200 / self.width))
        self.last_processed_time = rospy.Time.now()
        self.throttle_period = rospy.Duration(0.3)
        self.speed_linear = 0
        self.speed_angular = 0

    def preprocess_image(self, cv_image):#数据处理
        image = Image.fromarray(cv_image)
        enhancer = ImageEnhance.Contrast(image)
        enhanced_img = enhancer.enhance(3)
        img = np.array(enhanced_img)
        img = cv2.GaussianBlur(img, (17, 17), 0)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        img = img[self.crop_height:, :]
        nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(img, connectivity=8)
        sizes = stats[1:, -1]
        main_object_label = 1 + np.argmax(sizes)
        main_object = np.zeros_like(labels)
        main_object[labels == main_object_label] = 255
        new_img = np.zeros_like(img)
        new_img[main_object == 255] = 255
        h, w = new_img.shape
        img = cv2.resize(new_img, (200, self.resize_height), interpolation=cv2.INTER_AREA)
        img = np.reshape(img, (150, 200, 1))
        img = np.expand_dims(img, axis=0)
        img = img / 255  # 图像归一化
        return img


    def rord_dec(self,img):
        height, width, _ = img.shape
        start_row, start_col = int(height * .3), int(width * .0)
        end_row, end_col = int(height * .7), int(width * 1.0)
        img = img[start_row:end_row, start_col:end_col]
        img=img/255
        model=joblib.load('道路识别.m')
        perdict=model.predict(img)
        return perdict

    def predict_movement(self, img):
        predictions = self.model.predict(img)
        return predictions[0]

    def image_callback(self, msg):
        current_time = rospy.Time.now()
        if (current_time - self.last_processed_time) > self.throttle_period:
            try:
                np_arr = np.frombuffer(msg.data, np.uint8)
                cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
                processed_img = self.preprocess_image(cv_image)
                labels = self.predict_movement(processed_img)
                action = np.argmax(labels)
                labe_road=rord_dec(img)
                if action == 7:
                    print('直行')
                    self.speed_linear = 0.2
                    self.speed_angular = 0
                if labe_road==0:
                    if action == 6:
                        print('向左转弯')
                        self.speed_linear = 0.2
                        self.speed_angular = 0.5
                    if action == 5:
                        print('向右转弯')
                        self.speed_linear = 0.2
                        self.speed_angular = -0.5
                else:
                    if action == 6:
                        print('向左转弯')
                        self.speed_linear = 0.2
                        self.speed_angular = 0.1
                    if action == 5:
                        print('向右转弯')
                        self.speed_linear = 0.2
                        self.speed_angular = -0.1
                self.last_processed_time = current_time
                msg = Float64MultiArray()
                msg.data = [self.speed_linear, self.speed_angular]
                self.selfdrive_pub.publish(msg)
            except Exception as e:
                rospy.logerr(f"Error processing image: {e}")

def main():
    rospy.init_node('selfdrive_node', anonymous=True)
    ad = AutonomousDriving()
    rospy.spin()

if __name__ == '__main__':
    main()