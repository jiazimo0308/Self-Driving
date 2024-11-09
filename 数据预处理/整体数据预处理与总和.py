# !/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/2/18 16:29

import os
import label_txt
import data_corrct
import image_pro
import dataset_come
import pandas as pd
import numpy as np

def list_files(directory,rate):
    '''数据集路径，训练集测试集划分'''
    data_time = []
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isdir(path):
            data_time.append(path)

    global rm_item,datanew,data_other
    rm_item=[]#需要删除的数据
    dataset_train = []
    dataset_train_label = []
    dataset_test = []
    dataset_test_label = []
    data_other=[]
    #获得所有路径
    for i in data_time:
        print(i)
        for filename2 in os.listdir(str(i)):
            if filename2.startswith('.'): # 跳过隐藏文件和文件夹
                continue
            path2=os.path.join(str(i),filename2)
            if path2.endswith('.txt'):#首先对label标签进行数据处理
                data_label=label_txt.txtlabelcsv(path2)#对数据进行CSV格式的转换
            else:
                print('处理之前的匹配情况------------------------------')
                data_corrct.lenornor(data_label, path2)  # 对比标签集与图像集数据量是否相等
                data_label=data_corrct.time_diff(data_label,path2)#对比标签集与图像集时间戳是否相差过大
                datanew, rm_item = data_corrct.car_label(data_label)
                data_corrct.rm_image(rm_item,path2)
                print('处理之后的匹配情况-----------------------------')
                data_corrct.lenornor(datanew, path2)  # 对比标签集与图像集数据量是否相等
                datanew=data_corrct.time_diff(datanew, path2)
                # 分层抽样训练集与测试集
                train,test=label_txt.stratified_sampling(datanew,rate)
                data_other.append(datanew)
                #图像进行处理
                image_pro.preprocess_images(path2)
        set_train,set_train_label=dataset_come.pack(train,path2)
        set_test,set_test_label=dataset_come.pack(test, path2)
        dataset_train.extend(set_train)
        dataset_train_label.extend(set_train_label)
        dataset_test.extend(set_test)
        dataset_test_label.extend(set_test_label)
        print('#######################################')

    alldata = pd.concat(data_other, ignore_index=True)
    maxx=alldata['linear_x'].max()
    minx = alldata['linear_x'].min()
    maxz=alldata['angular_z'].max()
    minz = alldata['angular_z'].min()
    print(alldata['combined'].value_counts())
    print('总数据量为'+str(len(alldata)))

    stats_dict = {
        'max_linear_x': maxx,
        'min_linear_x': minx,
        'max_angular_z': maxz,
        'min_angular_z': minz
    }
    stats_df = pd.DataFrame([stats_dict])
    stats_df.to_csv('标签最大最小值.csv', index=False)
    print('标签最大最小值保存成功')
    #
    dataset_train = np.array(dataset_train)
    dataset_train_label = np.array(dataset_train_label)
    dataset_test =np.array(dataset_test)
    dataset_test_label = np.array(dataset_test_label)
    #保存两个数据集
    np.savez('train.npz', dataset=dataset_train, dataset_labels=dataset_train_label)
    np.savez('test.npz', dataset=dataset_test, dataset_labels=dataset_test_label)
    print('数据保存成功！！！！！！！！！！！！！！！！！！！！！！！！！')


dataset_directory = '/Users/jiazimo/PycharmProjects/Pycharm_graduation_design/数据预处理/数据集'
list_files(dataset_directory,0.3)
