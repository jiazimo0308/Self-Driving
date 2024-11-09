# !/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/2/18 21:49

import os
import numpy as np
import pandas as pd
from PIL import Image,ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def pack(data,picturedatapath):
    '''数据集打包'''
    dataset=[]
    datasetlabel=[]
    #便利标签数据集
    for index,row in data.iterrows():
        filename = str(int(row['time'])) + ".jpg"
        image_path = os.path.join(picturedatapath, filename)
        img = Image.open(image_path)
        img = np.array(img)
        dataset.append(img)
        # 判断标签
        linear_x = row['linear_x']
        angular_z = row['angular_z']
        t1=row['t1']
        t2 = row['t2']
        t3 = row['t3']
        t4 = row['t4']
        t5 = row['t5']
        t6 = row['t6']
        t7 = row['t7']
        t8= row['t8']
        t9 = row['t9']

        label_list=[linear_x,angular_z,t1,t2,t3,t4,t5,t6,t7,t8,t9]
        datasetlabel.append(label_list)
    return dataset,datasetlabel




