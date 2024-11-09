# !/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/2/18 16:56
import pandas as pd
import os
import numpy as np

'''
def rename_images(picturedatapath):
    ''''更改图片名称''''
    image_files = os.listdir(picturedatapath)
    image_files.sort()  # 确保图片文件按名称排
    count=1#计数器   重点
    #定义一个匹配表达式
    # 遍历所有文件
    for filename in image_files:
        if '_' in filename:
            continue
        else:
            if filename.lower().endswith('.jpg'):
                name, ext = os.path.splitext(filename)
                new_name = f"{name}_{count}{ext}"
                old_path = os.path.join(picturedatapath, filename)
                new_path = os.path.join(picturedatapath, new_name)
                os.rename(old_path, new_path)
                count += 1'''

def lenornor(data,picturedatapath):
    # 获取图片目录
    image_files = os.listdir(picturedatapath)
    image_files.sort()  # 确保图片文件按名称排序
    # 计算长度确保图片与CSV文件数据量相等
    picturenumber = len(image_files)
    if picturenumber == len(data):
        print('控制集与图像集数量相等')
    else:
        print('控制集与图像集数量不相等,数据集个数为'+str(len(data))+'图像集个数为'+str(picturenumber))

def time_diff(data,picturedatapath):
    '''筛选时间标签相同的数据时间标签不同的则进行删除'''
    image_names = {}
    for image_name in os.listdir(picturedatapath):
        if image_name.endswith('.jpg'):
            normalized_name = image_name.split('.')[0]
            image_names[normalized_name] = os.path.join(picturedatapath, image_name)
    matched_data = []
    unmatched_data=[]
    for names in data['time']:
        names=str(int(names))
        if names in image_names:
            matched_data.append(names)
        else:
            unmatched_data.append(names)
    if len(unmatched_data)==0 and len(matched_data)==len(image_names):
        print('数据集完全匹配')
    else:
        if len(matched_data) == 0:
            print('数据集全部不一致请重新采集')
            return None
        deleted_count = 0
        if len(matched_data)!=0:
            print('匹配数据量为'+str(len(matched_data)))
            data = data[~data['time'].isin(list(map(int, unmatched_data)) )]
            for name in image_names:
                if name not in matched_data:
                    unmatched_path=image_names[name]
                    if os.path.exists(unmatched_path):
                        os.remove(unmatched_path)
                        deleted_count+=1
        print('数据一致共删除'+str(deleted_count)+'张图片')
    return data

def car_label(data):
    '''统计运行工况'''
    # 创建组合列
    length=len(data)
    data['combined'] = (data['t1'].astype(str) +data['t2'].astype(str)+data['t3'].astype(str)
                        +data['t4'].astype(str)+data['t5'].astype(str) +data['t6'].astype(str)
                        +data['t7'].astype(str)+data['t8'].astype(str)+data['t9'].astype(str))
    #获得标签位置全为0的数据所在的行，行所对应的图片名称
    rows_to_remove = data['combined'] == '000000001'
    # 获取这些行中 'image_path' 列的值
    selected_column_values = data.loc[rows_to_remove, 'time'].tolist()
    # 删除 'combined' 列值为 '0000' 的行
    data = data[~rows_to_remove]
    #为了数据均衡进行1000标签的删除
    count_1001 = sum(data['combined'] == '000001000')
    count_1010 = sum(data['combined'] == '000000100')
    min_count = min(count_1001, count_1010)
    #获得需要删除数据的量
    count_1000= sum(data['combined'] == '000000010')
    delet_1000=count_1000-min_count
    #筛选出行'1000'
    rows_with_label_1000 = data[data['combined'] == '000000010']
    selected_rows = rows_with_label_1000.sample(n=delet_1000)
    selected_column_values2 = selected_rows['time'].tolist()
    selected_column_values= selected_column_values + selected_column_values2
    # 删除 'combined' 列值为 '1000' 的行
    data = data.drop(selected_rows.index)
    if count_1010>count_1001:
        delet_1010=count_1010-min_count
        rows_with_label_1010 = data[data['combined'] == '000000100']
        selected_rows1= rows_with_label_1010.sample(n=delet_1010)
        selected_column_values3= selected_rows1['time'].tolist()
        data = data.drop(selected_rows1.index)
        selected_column_values = selected_column_values +selected_column_values3
    if count_1001>count_1010:
        delet_1001 = count_1001 - min_count
        rows_with_label_1001 = data[data['combined'] == '000001000']
        selected_rows2 = rows_with_label_1001.sample(n=delet_1001)
        selected_column_values4 = selected_rows2['time'].tolist()
        data = data.drop(selected_rows2.index)
        selected_column_values = selected_column_values + selected_column_values4
    length2 = len(selected_column_values)
    length3=len(data)
    print('原表长为'+str(length)+',找到'+str(length2)+'个无用数据和均衡杂值'+'删除后表长为'+str(length3))
    return data,selected_column_values

def rm_image(rm_list,picturedatapath):
    rm_count=0#计数器
    for image_name in rm_list:
        filename=str(int(image_name))+".jpg"
        image_path=os.path.join(picturedatapath,filename)
        try:
            if os.path.exists(image_path):
                os.remove(image_path)
                rm_count+=1
        except Exception as e:
            print(f'删除图片{image_path}时出现错误')
    if rm_count==len(rm_list):
        print('删除成功，共删除'+str(rm_count)+'张')
    else:
        print('删除失败')

    '''
    # 对剩下的数据重新排序
    image_files = [f for f in os.listdir(picturedatapath) if f.lower().endswith('.jpg')]
    image_files.sort()
    count = 0
    for filename in image_files:
        name, ext = os.path.splitext(filename)
        prefix = name.split('_')[0]
        new_name = f"{prefix}_{count}{ext}"
        old_path = os.path.join(picturedatapath, filename)
        new_path = os.path.join(picturedatapath, new_name)
        # 重命名文件
        os.rename(old_path, new_path)
        count += 1  # 更新计数器'''








