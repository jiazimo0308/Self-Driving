#!/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/2/25
import tensorflow as tf
from PIL import Image,ImageFile,ImageEnhance
import numpy as np
import cv2

img=Image.open('1709118982.4.jpg')
# 创建对比度增强对象
enhancer = ImageEnhance.Contrast(img)
factor = 3
enhanced_img = enhancer.enhance(factor)
img = np.array(enhanced_img)
img = cv2.GaussianBlur(img, (3, 3), 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h, w = img.shape
img = cv2.resize(img, (200, int(h * (200 / w))), interpolation=cv2.INTER_AREA)
img=img/255
img = np.reshape(img, (150, 200, 1))
img = np.expand_dims(img, axis=0)
#
def perdict(image):
    model = tf.keras.models.load_model('/Users/jiazimo/PycharmProjects/Pycharm_graduation_design/自动驾驶行驶/模型/LeNet_5/LeNet_分类.h5')
    predictions = model.predict(image)
    print(predictions)
    average = sum(predictions[0]) / len(predictions[0])
    print(average)
    label = (predictions > average).astype(int)
    #labels = (predictions > 0.2).astype(int)#分类
    print(label)


perdict(img)