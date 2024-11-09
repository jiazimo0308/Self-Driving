#!/usr/bin/env python3
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/2/29
import cv2
import rospy
import joblib
import numpy as np
import tensorflow as tf
from PIL import ImageEnhance,Image
from sensor_msgs.msg import CompressedImage
from geometry_msgs.msg import Twist

model = tf.keras.models.load_model('/home/huanyu/robot_ws/src/ps2_teleop/src/.h5',compile = False)
model_lu=joblib.load('')
height = 480
width = 640

def preprocess_image(cv_image):
    image = Image.fromarray(cv_image)
    enhancer = ImageEnhance.Contrast(image)
    enhanced_img = enhancer.enhance(3)
    img = np.array(enhanced_img)
    img = cv2.GaussianBlur(img, (17, 17), 0)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    crop_height = int(height / 3)
    img = img[crop_height:, :]
    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(img, connectivity=8)
    sizes = stats[1:, -1]
    main_object_label = 1 + np.argmax(sizes)
    main_object = np.zeros_like(labels)
    main_object[labels == main_object_label] = 255
    new_img = np.zeros_like(img)
    new_img[main_object == 255] = 255
    h, w = new_img.shape
    img = cv2.resize(new_img, (200, int(height * (200 / width))), interpolation=cv2.INTER_AREA)
    pred = model_lu.predict(img.reshape(-1))
    print(pred)
    img = np.reshape(img, (150, 200, 1))
    img = np.expand_dims(img, axis=0)
    img = img / 255  # 图像归一化
    return img

def predict_movement(img):
    predictions = model.predict(img)
    return predictions[0]

speed_huigui=[]
def image_callback(msg):
    global last_processed_time,throttle_period
    current_time = rospy.Time.now()
    if (current_time - last_processed_time) > throttle_period:
        try:
            np_arr = np.frombuffer(msg.data, np.uint8)
            cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            processed_img = preprocess_image(cv_image)
            labels = predict_movement(processed_img)
            linear_speed= labels[0]
            angular_speed = labels[1]
            if linear_speed>=0.2:
                linear_speed=0.2
            if abs(angular_speed)>0.5:
                if angular_speed<0:
                    angular_speed=-0.5
                if angular_speed>0:
                    angular_speed=0.5
            print(linear_speed,angular_speed)
            if linear_speed>0:
                print('直行')
            if angular_speed>0:
                print('左转')
            if angular_speed==0:
                print('无动作')
            if angular_speed<0:
                print('右转')
            twist_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
            twist_msg = Twist()
            twist_msg.linear.x = linear_speed
            twist_msg.angular.z = angular_speed
            twist_pub.publish(twist_msg)
            speed_huigui.append((linear_speed, angular_speed))
            #更新时间
            last_processed_time = current_time
        except Exception as e:
            rospy.logerr(f"Error processing image: {e}")

def save_speed_log_to_csv():
    # 将速度记录保存到CSV文件
    with open('/media/huanyu/DATASET11/speed_huigui.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Linear Speed', 'Angular Speed'])  # 写入标题
        for linear_speed, angular_speed in speed_huigui:
            writer.writerow([linear_speed, angular_speed])

def main():
    rospy.init_node('test_prediction_node2', anonymous=True)
    global last_processed_time, throttle_period
    last_processed_time = rospy.Time.now()  # 初始化last_processed_time
    throttle_period = rospy.Duration(0.3)
    rospy.Subscriber('/camera/rgb/image_raw/compressed',CompressedImage, image_callback)
    rospy.spin()
    save_speed_log_to_csv()

if __name__ == '__main__':
    main()












