# !/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/2/22 21:25
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Arial Unicode MS']
plt.rcParams['axes.unicode_minus']=False
pd.set_option('display.float_format', '{:.2f}'.format)
# 读取文件内容
with open('/数据预处理/数据集1/第一次/label.txt', 'r') as f:#/Users/jiazimo/PycharmProjects/Pycharm_graduation_design/数据预处理/数据集1/第二次采集/label2.txt
    lines = f.readlines()
    parsed_data = []
    for line in lines:
        parts = line.strip().split(", ")
        row = {}
        for part in parts:
            key, value = part.split(": ")
            row[key] = float(value)
        parsed_data.append(row)
    # 转换为pandas DataFrame
    df = pd.DataFrame(parsed_data)
    # 替换所有的 -0 为 0
    df = df.replace(-0, 0)
    plt.plot(df['linear_x'],label='线速度')
    plt.plot(df['angular_z'],label='角速度')
    plt.legend(loc='upper right', fontsize=14)
    plt.show()
