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
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import mean_squared_error, mean_absolute_error
plt.rcParams['font.sans-serif']=['SimSun']
plt.rcParams['axes.unicode_minus']=False

def dataset_in():
    train = np.load('/kaggle/input/cardata99/train.npz')
    trainset=train['dataset']
    trainlabel=train['dataset_labels']
    test = np.load('/kaggle/input/cardata99/test.npz')
    testset=test['dataset']
    testlabel=test['dataset_labels']
    return trainset,trainlabel,testset,testlabel

def normalized_img(trainset,trainlabel,testset,testlabel):
    trainset=trainset.astype('float')
    trainset /= 255.0
    testset = testset.astype('float')
    testset /= 255.0
    trainlabel = trainlabel[:, [0,1]]
    testlabel = testlabel[:,[0,1]]
    #trainlabel = trainlabel.astype(float)
    #testlabel = testlabel.astype(float)
    return trainset,trainlabel,testset,testlabel

def only_set():
    '''数据集归一化，不存在特征数据集'''
    trainset, trainlabel, testset, testlabel=dataset_in()
    trainset,trainlabel,testset,testlabel=normalized_img(trainset,trainlabel,testset,testlabel)
    return trainset, trainlabel, testset, testlabel

trainset, trainlabel, testset, testlabel=only_set()
#print(trainset.shape)
# 创建一个Adam优化器实例，设置学习率为0.01
optimizer = tf.keras.optimizers.Adam(learning_rate=0.00000001)
#模型建立(LeNet-5)
model=models.Sequential()
model.add(layers.Conv2D(6, (5, 5), activation='relu', input_shape=(150, 200, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(16, (5, 5), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(120, (5, 5), activation='relu'))
# 添加全连接层
model.add(layers.Flatten())
model.add(layers.Dense(84, activation='relu'))
model.add(layers.Dense(2,activation='linear'))
model.compile(loss='mean_squared_error',optimizer=optimizer,metrics=['mae'])
#拟合网络
early_stopper = EarlyStopping(monitor='val_mae', patience=10, verbose=1, mode='min', restore_best_weights=True)
history=model.fit(trainset,trainlabel,epochs=300,batch_size=100,validation_data=(testset,testlabel),callbacks=[early_stopper])
model.save('LeNet_huigui.h5')
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
acc = history_dict['mae'][3:]
val_acc = history_dict['val_mae'][3:]
plt.plot(epochs, acc, 'bo', label='Training Mae')
plt.plot(epochs, val_acc, 'b', label='Testing Mae')
plt.xlabel('Epoche')
plt.ylabel('Mae')
plt.legend(fontsize=14)
plt.show()

predicted_labels = model.predict(testset)
mse = mean_squared_error(testlabel, predicted_labels)
mae = mean_absolute_error(testlabel, predicted_labels)
print("整体MSE:", mse)
print("整体MAE:", mae)