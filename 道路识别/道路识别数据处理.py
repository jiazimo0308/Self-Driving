#!/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/3/24
import cv2
import os

# 指定要处理的文件夹路径
folder_path = '/道路识别/数据集/转弯'

# 遍历文件夹下的所有文件
for filename in os.listdir(folder_path):
    # 检查文件是否为图片
    if filename.endswith('.jpg'):
        # 读取图片
        img = cv2.imread(os.path.join(folder_path, filename))
        # 进行截取操作，这里以截取图片的左上角为例
        height, width, _ = img.shape
        start_row, start_col = int(height * .3), int(width * .0)
        end_row, end_col = int(height * .7), int(width * 1.0)
        # 使用numpy的切片操作截取图像
        img = img[start_row:end_row, start_col:end_col]
        # 将截取后的图片保存回原路径，使用原文件的名字
        cv2.imwrite(os.path.join(folder_path, filename), img)
print('处理完成')
