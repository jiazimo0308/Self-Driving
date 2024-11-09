# !/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/2/18 16:50
import pandas as pd

def txtlabelcsv(path):
    '''标签路径'''
    pd.set_option('display.float_format', '{:.2f}'.format)
    # 读取文件内容
    with open(str(path), 'r') as f:
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
    #
    t1=[]
    t2=[]
    t3=[]
    t4=[]
    t5 = []
    t6 = []
    t7 = []
    t8 = []
    t9 = []
    for i in range(len(df)):#将两个速度进行分解，分解为前进后退左转与右转
        if df.iloc[i, 1]==0 and df.iloc[i,2]==0:#停车
            t1.append(0)
            t2.append(0)
            t3.append(0)
            t4.append(0)
            t5.append(0)
            t6.append(0)
            t7.append(0)
            t8.append(0)
            t9.append(1)
        if df.iloc[i, 1] > 0 and df.iloc[i, 2]==0:#直行
            t1.append(0)
            t2.append(0)
            t3.append(0)
            t4.append(0)
            t5.append(0)
            t6.append(0)
            t7.append(0)
            t8.append(1)
            t9.append(0)
        if df.iloc[i, 1] > 0 and df.iloc[i, 2] > 0:  # 左转
            t1.append(0)
            t2.append(0)
            t3.append(0)
            t4.append(0)
            t5.append(0)
            t6.append(0)
            t7.append(1)
            t8.append(0)
            t9.append(0)
        if df.iloc[i, 1] > 0 and df.iloc[i, 2] <0:  # 右转
            t1.append(0)
            t2.append(0)
            t3.append(0)
            t4.append(0)
            t5.append(0)
            t6.append(1)
            t7.append(0)
            t8.append(0)
            t9.append(0)
        if df.iloc[i, 1] == 0 and df.iloc[i, 2] >0:  # 纯左转
            t1.append(0)
            t2.append(0)
            t3.append(0)
            t4.append(0)
            t5.append(1)
            t6.append(0)
            t7.append(0)
            t8.append(0)
            t9.append(0)
        if df.iloc[i, 1] == 0 and df.iloc[i, 2] <0:  # 纯右
            t1.append(0)
            t2.append(0)
            t3.append(0)
            t4.append(1)
            t5.append(0)
            t6.append(0)
            t7.append(0)
            t8.append(0)
            t9.append(0)
        if df.iloc[i, 1] <0 and df.iloc[i, 2] ==0:  # 倒车
            t1.append(0)
            t2.append(0)
            t3.append(1)
            t4.append(0)
            t5.append(0)
            t6.append(0)
            t7.append(0)
            t8.append(0)
            t9.append(0)
        if df.iloc[i, 1] < 0 and df.iloc[i, 2] >0:  # 倒车向左
            t1.append(0)
            t2.append(1)
            t3.append(0)
            t4.append(0)
            t5.append(0)
            t6.append(0)
            t7.append(0)
            t8.append(0)
            t9.append(0)
        if df.iloc[i, 1] < 0 and df.iloc[i, 2] <0:  # 倒车向右
            t1.append(1)
            t2.append(0)
            t3.append(0)
            t4.append(0)
            t5.append(0)
            t6.append(0)
            t7.append(0)
            t8.append(0)
            t9.append(0)
    df['t1']=t1
    df['t2']=t2
    df['t3']=t3
    df['t4']=t4
    df['t5']=t5
    df['t6']=t6
    df['t7']=t7
    df['t8'] = t8
    df['t9'] = t9
    return df

def stratified_sampling(data,rate):
    '''分层抽样'''
    #计算抽样总数
    total_samples=int(len(data)*rate)
    # 计算每个层的比例
    strata_counts = data['combined'].value_counts(normalize=True)
    strata_sample_sizes = (strata_counts * total_samples).round().astype(int)
    # 创建空的DataFrame来存储最终的分层样本
    test = pd.DataFrame()
    # 进行分层抽样
    for stratum, sample_size in strata_sample_sizes.items():
        # 从每个层中抽取样本
        stratum_samples = data[data['combined'] == stratum].sample(n=sample_size)
        # 将抽取的样本添加到最终的DataFrame中
        test = pd.concat([test, stratum_samples])
    train = data.drop(test.index)
    return train,test
