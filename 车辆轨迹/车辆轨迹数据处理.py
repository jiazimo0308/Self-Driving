# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Jiazimo
# @Time : 2024/2/15 11:23
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
plt.rcParams['font.sans-serif']=['Arial Unicode MS']
plt.rcParams['axes.unicode_minus']=False

def read_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            time, x, y, z, yaw = map(float, parts)
            data.append((x, y))
    return np.array(data)

'''
# 调用函数读取所有数据文件
data_files = ['英伟达回归模型轨迹.txt', '英伟达分类模型轨迹.txt']  # 假设这是您的文件列表
data_files2=['LeNet回归模型轨迹.txt','LeNet分类模型轨迹.txt']
# 使用PCA找到参考轨迹的主要方向
ref_data = read_data('英伟达回归模型轨迹.txt')
pca = PCA(n_components=2)
pca.fit(ref_data)
direction = pca.components_[0]

# 计算旋转矩阵
rotation_matrix = np.array([[direction[0], -direction[1]], [direction[1], direction[0]]])'''

# 旋转所有轨迹并绘制
'''
for file_name in data_files2:
    data = read_data(file_name)
    # 将所有点都减去起始点
    data -= data[0]
    rotated_data = np.dot(data, rotation_matrix)
    # 如果旋转后的轨迹与期望的方向不一致，反转旋转矩阵
    if np.dot(rotated_data[-1] - rotated_data[0], direction) < 0:
        rotation_matrix *= -1
        rotated_data = np.dot(data, rotation_matrix)
    # 绘制旋转后的轨迹
    plt.figure(figsize=(10, 5))
    plt.plot(rotated_data[:, 0], rotated_data[:, 1], 'o')
    plt.title(f'Vehicle Trajectory from {file_name}')
    plt.xlabel('Scaled X Coordinate')
    plt.ylabel('Scaled Y Coordinate')
    plt.grid(True)
    plt.show()'''
data_files = ['英伟达回归模型轨迹.txt', '英伟达分类模型轨迹.txt', 'LeNet回归模型轨迹.txt','LeNet分类模型轨迹.txt','最终.txt']
# 旋转所有轨迹并绘制
for file_name in data_files:
    data = read_data(file_name)
    # 将所有点都减去起始点
    data -= data[0]
    # 计算旋转矩阵
    start_point = data[0]
    end_point = data[-1]
    direction = end_point - start_point
    direction /= np.linalg.norm(direction)  # normalize
    rotation_matrix = np.array([[direction[0], -direction[1]], [direction[1], direction[0]]])
    rotated_data = np.dot(data, rotation_matrix)
    # 绘制旋转后的轨迹
    plt.figure(figsize=(6, 5))
    colors=np.arange(len(rotated_data),0,-1)
    plt.scatter(rotated_data[:, 0], rotated_data[:, 1],c=colors, cmap='viridis')
    plt.colorbar()
    print(f'{file_name}')
    #plt.title(f'Vehicle Trajectory from {file_name}')
    plt.axis('equal')
    #plt.xlabel('Scaled X Coordinate')
    #plt.ylabel('Scaled Y Coordinate')
    #plt.grid(True)
    plt.savefig(f'{file_name}'+'.jpg')
    plt.show()