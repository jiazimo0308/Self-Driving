#!/usr/bin/env python
# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/4/3
import os
import cv2
import joblib
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

jump_path=os.path.join('数据集','转弯')
none_path=os.path.join('数据集','直行')
files = [os.path.join(jump_path, jump) for jump in os.listdir(jump_path)] + [os.path.join(none_path, none) for none in os.listdir(none_path)]
X = []
y = [0] * len(os.listdir(jump_path)) + [1] * len(os.listdir(none_path))
# 遍历jump目录下的图片
for file in files:
    x = cv2.imread(file).reshape(-1)
    X.append(x/255)
# 2、拆分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 3、定义模型
model = LogisticRegression(max_iter=500)
# 4、训练模型
model.fit(X_train, y_train)
# 5、评估模型
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
print(train_score, test_score)
joblib.dump(model, '道路识别.m')