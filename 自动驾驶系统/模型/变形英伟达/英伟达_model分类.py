#!/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/3/6
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from sklearn.metrics import mean_squared_error, mean_absolute_error
from tensorflow.keras.callbacks import EarlyStopping
# 添加L1正则化的Dense层
plt.rcParams['font.sans-serif']=['SimSun']
plt.rcParams['axes.unicode_minus']=False

def dataset_in():
    train = np.load('/kaggle/input/newestcardata/train.npz')
    trainset=train['dataset']
    trainlabel=train['dataset_labels']
    test = np.load('/kaggle/input/newestcardata/test.npz')
    testset=test['dataset']
    testlabel=test['dataset_labels']
    return trainset,trainlabel,testset,testlabel

def normalized_img(trainset,trainlabel,testset,testlabel):
    trainset=trainset.astype('float')
    trainset /= 255.0
    testset = testset.astype('float')
    testset /= 255.0
    trainlabel = trainlabel[:, [2,3,4,5]]
    testlabel = testlabel[:,[2,3,4,5]]
    return trainset,trainlabel,testset,testlabel

def only_set():
    '''数据集归一化，不存在特征数据集'''
    trainset, trainlabel, testset, testlabel=dataset_in()
    trainset,trainlabel,testset,testlabel=normalized_img(trainset,trainlabel,testset,testlabel)
    return trainset, trainlabel, testset, testlabel

trainset, trainlabel, testset, testlabel=only_set()

# 创建一个Adam优化器实例，设置学习率为0.01
optimizer = tf.keras.optimizers.Adam(learning_rate=0.00000001)
#模型建立(LeNet-5)
model=models.Sequential()
model.add(layers.Conv2D(24, (5, 5), activation='elu', strides=(2, 2),input_shape=(150,200,1)))
model.add(layers.Conv2D(36, (5, 5), activation='elu', strides=(2, 2)))
model.add(layers.Conv2D(48, (5, 5), activation='elu', strides=(2, 2)))
model.add(layers.Conv2D(64, (3, 3),activation='elu'))
model.add(layers.Conv2D(64, (3, 3),activation='elu'))
model.add(layers.Dropout(0.5))  # Dropout将在训练过程中每次更新参数时随机断开一定百分比（p）的输入神经元连接
model.add(layers.Flatten())
model.add(layers.Dense(250, activation='elu'))
model.add(layers.Dense(4, activation='softmax'))
model.compile(loss='categorical_crossentropy',optimizer=optimizer,metrics=['acc'])#mean_squared_error,mae,categorical_crossentropy
#拟合网络
early_stopper = EarlyStopping(monitor='val_acc', patience=10, verbose=1, mode='max', restore_best_weights=True)
history=model.fit(trainset,trainlabel,epochs=100,batch_size=100,validation_data=(testset,testlabel),callbacks=[early_stopper])
model.save('英伟达_fenlei.h5')
# 绘制训练损失和验证损失
history_dict = history.history
loss_values = history_dict['loss'][3:]
val_loss_values = history_dict['val_loss'][3:]
epochs = range(1, len(loss_values) + 1)
plt.plot(epochs, loss_values, 'bo', label='Training loss')
plt.plot(epochs, val_loss_values, 'b', label='Testing loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(fontsize=14)
plt.show()

# 清空图像绘制下一幅 训练精度和验证精度
plt.clf()
acc = history_dict['acc'][3:]
val_acc = history_dict['val_acc'][3:]
plt.plot(epochs, acc, 'bo', label='Training Acc')
plt.plot(epochs, val_acc, 'b', label='Testing Acc')
plt.xlabel('Epoche')
plt.ylabel('Acc')
plt.legend(fontsize=14)
plt.show()