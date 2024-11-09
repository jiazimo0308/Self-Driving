# -*- coding: utf-8 -*-
# @Author : Jiazimo
# @Time : 2024/1/19 16:06

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
#显示中文标签
plt.rcParams['font.sans-serif']=['Arial Unicode MS']
plt.rcParams['axes.unicode_minus']=False
#文件路径
data='/Users/jiazimo/PycharmProjects/Pycharm_graduation_design/自动驾驶避障/避障数据(雷达)/scan_data.txt'
#初始化坐标
x_coords=[]
y_coords=[]

# 读取文件并处理每一行
with open(data, 'r') as file:
    for line in file:
       #前为角度(度)，后为距离(米)
        theta_degree, r = line.strip().split(', ')
        x = float(r) * math.cos(float(theta_degree))  # 计算 x 坐标
        y = float(r) * math.sin(float(theta_degree))  # 计算 y 坐标
        x_coords.append(x)
        y_coords.append(y)
# 创建散点图
plt.scatter(x_coords, y_coords,color='r')
plt.scatter(0, 0,color='b',s=65)
plt.scatter(-2,0,color='g',s=65)
plt.legend(['扫描障碍','起始位置','目标位置'])
plt.grid(True)
plt.show()













