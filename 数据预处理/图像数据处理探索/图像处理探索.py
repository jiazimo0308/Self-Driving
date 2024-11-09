# !/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/2/19 09:30
import numpy as np
from PIL import Image, ImageEnhance
import cv2
# 打开图像
enhanced_img = Image.open('171024113872_副本.jpg')
enhanced_img2 = cv2.imread('171024113872_副本.jpg')
enhancer = ImageEnhance.Contrast(enhanced_img)
enhanced_img = enhancer.enhance(3)
enhanced_img_np = np.array(enhanced_img)
enhanced_img = enhanced_img_np.astype(np.uint8)
enhanced_img = cv2.GaussianBlur(enhanced_img, (21, 21), 0)
enhanced_img = cv2.cvtColor(enhanced_img, cv2.COLOR_BGR2GRAY)
ret, image = cv2.threshold(enhanced_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(image, connectivity=8)
sizes = stats[1:, -1]
main_object_label = 1 + np.argmax(sizes)
main_object = np.zeros_like(labels)
main_object[labels == main_object_label] = 255
enhanced_img2[main_object==255]=[0,255,0]
cv2.imshow('Marked Image', enhanced_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()



#image = cv2.adaptiveThreshold(enhanced_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 13, 2)
#average_gray = cv2.mean(enhanced_img)
#_, enhanced_img = cv2.threshold(enhanced_img, average_gray[0], 255, cv2.THRESH_BINARY)
#enhanced_img = Image.fromarray(image)
#enhanced_img.save('全局.jpg')

#height, width = image.shape[:2]
#crop_height = int(height / 4)
#image = image[crop_height:, :]
#print(image.shape)
#enhanced_img = Image.fromarray(image)
#enhanced_img.save('裁剪.jpg')
#resized_img = cv2.resize(image, (200, int(height * (200 / width))), interpolation=cv2.INTER_AREA)
#print(resized_img.shape)

#enhanced_img_pil = Image.fromarray(resized_img)
#enhanced_img_pil.save('结果.jpg')

