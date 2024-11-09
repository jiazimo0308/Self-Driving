# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/2/12 18:32

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
#显示中文标签
plt.rcParams['font.sans-serif']=['Arial Unicode MS']
plt.rcParams['axes.unicode_minus']=False
#文件路径
data='/Users/jiazimo/PycharmProjects/Pycharm_graduation_design/自动驾驶避障/实现避障/scan_data4.txt'
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


#划定预警范围
alert_zone=0.45#数据范围
#定义小车
class Car():
    def __init__(self,po_x,po_y,alert,fun_x,fun_y):
        '''其中x,y代表小车在直角坐标系下投影的位置'''
        self.po_x=po_x#小车当前位置po_x
        self.po_y=po_y#小车当前位置po_y
        self.fun_x=fun_x#小车目标位置fun_x
        self.fun_y=fun_y#小车目标位置fun_y
        self.x=0.23#小车初始宽度
        self.y=0.26#小车初始长度
        self.alert=alert#预警范围
        self.centul_dis=math.sqrt(0.23**2+0.26**2)/2#小车中心点到定点距离

        #设置安全距离是否合格判断
        if self.alert<=self.centul_dis:
            print('预警范围小于最小范围,请重新设定')
        else:
            print('预警范围符合标准')

    #绘制出小车周围的预警范围
    def draw_alert_zone(self):
        # 绘制预警范围
        circle = plt.Circle((self.po_x, self.po_y), self.alert, color='lawngreen', fill=True,label='预警范围')#alpha=0.7
        # 将圆添加到图中
        plt.gca().add_patch(circle)
        # 绘制小车位置
        #plt.plot(self.po_x, self.po_y, 'ro')
        rectangle = patches.Rectangle((self.po_x - self.y / 2, self.po_y - self.x / 2), self.y, self.x, color='indigo',label='智能车')
        # 获取当前的轴
        ax = plt.gca()
        # 将矩形添加到轴中
        ax.add_patch(rectangle)
        # 检查障碍物是否在预警范围内，并设置颜色
    def draw_in_zone(self, obstacle_x, obstacle_y):
        for x1,y1 in zip(obstacle_x,obstacle_y):
            distance = math.sqrt((x1 - self.po_x) ** 2 + (y1 - self.po_y) ** 2)
            if distance <= alert_zone:
                plt.scatter(x1,y1,color='r')

# 创建小车实例
car = Car(0, 0, alert_zone, 0, 0)
# 调用方法绘制预警范围
plt.grid(True)
car.draw_alert_zone()
# 绘制散点
#plt.figure(figsize=(5,5))
plt.scatter(x_coords, y_coords, s=10, color='b',label='环境障碍')
car.draw_in_zone(x_coords,y_coords)
#plt.legend(fontsize=14)
plt.axis('equal')
plt.xlim(-1.5,0.5)
plt.ylim(-1.5,0.5)
 # 设置 x 轴和 y 轴的比例相等
#plt.show()
plt.savefig('fourth.png', dpi=300)  # 保存图像时设置高DPI




