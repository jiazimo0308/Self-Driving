#!/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/3/10
import tensorflow as tf
import numpy as np
def dataset_in():
    train = np.load('/Users/jiazimo/PycharmProjects/Pycharm_graduation_design/数据预处理/train.npz')
    trainset=train['dataset']
    trainlabel=train['dataset_labels']
    test = np.load('/Users/jiazimo/PycharmProjects/Pycharm_graduation_design/数据预处理/test.npz')
    testset=test['dataset']
    testlabel=test['dataset_labels']
    return trainset,trainlabel,testset,testlabel
def normalized_img(trainset,trainlabel,testset,testlabel):
    trainset=trainset.astype('float')
    trainset /= 255.0
    testset = testset.astype('float')
    testset /= 255.0
    trainlabel = trainlabel[:, [2,3,4,5,6,7,8,9,10]]
    testlabel = testlabel[:,[2,3,4,5,6,7,8,9,10]]
    return trainset,trainlabel,testset,testlabel
def only_set():
    '''数据集归一化，不存在特征数据集'''
    trainset, trainlabel, testset, testlabel=dataset_in()
    trainset,trainlabel,testset,testlabel=normalized_img(trainset,trainlabel,testset,testlabel)
    return trainset, trainlabel, testset, testlabel
#数据预处理
trainset, trainlabel, testset, testlabel=only_set()
model = tf.keras.models.load_model('/Users/jiazimo/PycharmProjects/Pycharm_graduation_design/自动驾驶行驶/模型/LeNet_5/LeNet_分类3.h5')
predictions = model.predict(testset)
print(predictions)
labels=[]
for i in predictions:
    max_value = np.max(i)
    i[i == max_value] = 1
    i[i != 1] = 0
    labels.append(i)
print(labels)
accuracy = np.mean(labels == testlabel)
print(f'Training Accuracy: {accuracy}')
