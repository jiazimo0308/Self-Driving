# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2023/12/26 10:06
import cv2
import numpy as np
import pandas as pd
import glob
#
#对相机标定数据集进行读取
path='/Users/jiazimo/PycharmProjects/Pycharm_graduation_design/相机标定/相机标定数据集/calibration*.jpg'
#path1='/Users/jiazimo/PycharmProjects/Pycharm_graduation_design/相机标定/相机标定数据集/红绿灯11.jpg'
#/Users/jiazimo/PycharmProjects/Pycharm_graduation_design/相机标定/相机标定数据集
#

def camera_set(px,py,image):
    '''px:行，py:列，image:图片'''
    #读取图片(搜索路径下的所有文件)
    images=glob.glob(image)
    #print(images)
    if len(images)>0:
        print('数据集不为空共有'+str(len(images))+'张')
    else:
        print('数据集为空数据集')
    #创建坐标系点
    objp = np.zeros((px * py, 3), np.float32)
    objp[:, :2] = np.mgrid[0:px, 0:py].T.reshape(-1, 2)
    #真实坐标点和图像坐标点
    realporints=[]
    imageporints=[]
    #
    #读取图片
    for i in images:
        picture=cv2.imread(i)
        #图像大小尺寸
        img_size = (picture.shape[1], picture.shape[0])
        #图像灰度化处理
        gray = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
        #找到图像交点（ret=Tag)
        ret, corners = cv2.findChessboardCorners(gray, (px, py), None)
        #找到则加入list中
        if ret is True:
            picture_copy=picture.copy()
            cv2.drawChessboardCorners(picture_copy, (px, py), corners, ret)#坐标显示
            cv2.imwrite('佐证前后对比/识别标点.png', picture_copy)#保存图片
            realporints.append(objp)
            imageporints.append(corners)
    #获得相机内部参数矩阵(mtx,内部参数矩阵，dis畸变量，rvecs旋转量，tvecs平移量)
    ret1, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(realporints, imageporints, img_size, None, None)
    #
    '''
    # 获取新的相机矩阵和感兴趣区域
    h, w = gray.shape[:2]
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h),0, (w, h))
    picture1 = cv2.imread(path1)
    dst = cv2.undistort(picture1, mtx, dist, None, mtx)# 校正图像
    # 裁剪图像
    x, y, w, h = roi
    #dst = dst[y:y + h, x:x + w]
    cv2.imwrite('佐证前后对比/畸变矫正11的图像.png', dst)#畸变矫正'''
    # 将参数封装到字典中
    calibration = {'camera_matrix': mtx.tolist(), 'dist_coeff': dist.tolist(),
                   'r_vecs': [r.tolist() for r in rvecs], 't_vecs': [t.tolist() for t in tvecs]}
    # 将字典保存为JSON文件
    import json
    with open('/红绿灯识别与动作/距离目标距离判断/calibration.json', 'w') as f:
        json.dump(calibration, f)
    return ret1, mtx, dist, rvecs, tvecs

#图像畸变矫正并存入规定的文件夹下（考虑以下到时候数据标签的问题）
def undistortpicture(mtx, dist,need):
    '''mtx:内部参数矩阵, dist：畸变量, need需要矫正的图片'''
    return cv2.undistort(need, mtx, dist, None, mtx)
#
camera_set(7,11,path)


