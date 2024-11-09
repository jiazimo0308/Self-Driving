# !/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/2/18 17:22
import os
import numpy
import pandas
import cv2
from PIL import Image,ImageFile,ImageEnhance
import numpy as np
# 设置PIL允许处理被截断的图像文件
ImageFile.LOAD_TRUNCATED_IMAGES = True

def preprocess_images(picturedatapath):
    '''对图像进行相关处理'''
    image_names=os.listdir(picturedatapath)
    size=False
    for image_name in image_names:#便利所有图片
        if image_name.startswith('.'):  # 跳过隐藏文件和文件夹
            continue
        image_path=os.path.join(picturedatapath,image_name)
        img=Image.open(image_path)
        # 创建对比度增强对象
        enhancer = ImageEnhance.Contrast(img)
        enhanced_img = enhancer.enhance(3)
        #
        img = np.array(enhanced_img)
        height, width = img.shape[:2]#获取图像大小
        if height != 480 and width != 640:
            print('图像尺寸不符，不符图像为', image_name)
            size=True
            break
        #高斯模糊
        img = cv2.GaussianBlur(img, (17, 17), 0)
        #灰度化
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #二值化
        ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        #图像裁剪
        crop_height = int(height / 3)
        img = img[crop_height:, :]
        #图像主体提取
        nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(img, connectivity=8)
        sizes = stats[1:, -1]
        main_object_label = 1 + np.argmax(sizes)
        main_object = np.zeros_like(labels)
        main_object[labels == main_object_label] = 255
        # 创建新的图像，主体部分为白色，其余为黑色
        new_img = np.zeros_like(img)
        new_img[main_object == 255] = 255
        # 对图像进行缩放减少内存
        img = cv2.resize(new_img, (200, int(height * (200 / width))), interpolation=cv2.INTER_AREA)
        #处理完数据后存回原路径下
        cv2.imwrite(image_path,img)
    if not size:
        print('所有图像尺寸相同')
        print('图像处理完成')


