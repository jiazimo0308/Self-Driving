# !/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/2/19 09:50
import numpy as np
import cv2

def dataset_in():
    train = np.load('/数据预处理/train.npz')
    trainset=train['dataset']
    trainlabel=train['dataset_labels']
    test = np.load('/数据预处理/test.npz')
    testset=test['dataset']
    testlabel=test['dataset_labels']
    print(testlabel)
    return trainset,trainlabel,testset,testlabel
dataset_in()
def normalized_img(trainset,trainlabel,testset,testlabel):
    trainset=trainset.astype('float')
    trainset /= 255.0
    testset = testset.astype('float')
    testset /= 255.0
    #merged_array = np.concatenate((testlabel, trainlabel), axis=0)
    #
    # 最小-最大归一化
    #min_vals = merged_array.min(axis=0)  # 按列计算最小值
    #max_vals = merged_array.max(axis=0)  # 按列计算最大值
    #trainlabel = (trainlabel - min_vals) / (max_vals - min_vals)
    #testlabel= (testlabel - min_vals) / (max_vals - min_vals)
    #取出第一列数据
    #trainlabel = trainlabel[:, 0]
    #testlabel =testlabel[:, 0]

    return trainset,testset,trainlabel,testlabel

def sift(set):
    sift = cv2.SIFT_create()
    sift_keypoints=[]
    for image in set:
        keypoints, descriptors = sift.detectAndCompute(image, None)
        # 如果没有检测到特征，则添加一个零向量
        if descriptors is None:
            descriptors = np.zeros((1, sift.descriptorSize()))
        sift_keypoints.append(descriptors)
    return sift_keypoints

def only_set():
    '''数据集归一化，不存在特征数据集'''
    trainset, trainlabel, testset, testlabel=dataset_in()
    trainset, testset,trainlabel, testlabel=normalized_img( trainset, trainlabel, testset, testlabel)
    return trainset, trainlabel, testset, testlabel