#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-04-18 00:01
@Author  : red
@Site    : 
@File    : stoc_grad_ascent.py
@Software: PyCharm
"""
from utils.sigmoid_util import sigmoid
from load_data.load_data import load_data_set
import matplotlib.pyplot as plt
import numpy as np
import random

"""
函数说明:绘制数据集

Parameters:
    weights - 权重参数数组
"""


def plot_best_fit(weights):
	data_mat, label_mat = dataMat, labelMat  # 加载数据集
	data_arr = np.array(data_mat)  # 转换成numpy的array数组
	n = np.shape(dataMat)[0]  # 数据个数
	xcord1 = []
	ycord1 = []  # 正样本
	xcord2 = []
	ycord2 = []  # 负样本
	for i in range(n):  # 根据数据集标签进行分类
		if int(label_mat[i]) == 1:
			xcord1.append(data_arr[i, 1])
			ycord1.append(data_arr[i, 2])  # 1为正样本
		else:
			xcord2.append(data_arr[i, 1])
			ycord2.append(data_arr[i, 2])  # 0为负样本
	fig = plt.figure()
	ax = fig.add_subplot(111)  # 添加subplot
	ax.scatter(xcord1, ycord1, s=20, c='red', marker='s', alpha=.5)  # 绘制正样本
	ax.scatter(xcord2, ycord2, s=20, c='green', alpha=.5)  # 绘制负样本
	x = np.arange(-3.0, 3.0, 0.1)
	y = (-weights[0] - weights[1] * x) / weights[2]
	ax.plot(x, y)
	plt.title('BestFit')  # 绘制title
	plt.xlabel('X1')
	plt.ylabel('X2')  # 绘制label
	plt.show()


'''
函数说明:改进的随机梯度上升算法
Parameters:
    dataMatrix - 数据数组
    classLabels - 数据标签
    numIter - 迭代次数
Returns:
    weights - 求得的回归系数数组(最优参数)
'''


def stoc_grad_ascent1(data_matrix, class_labels, num_iter=150):
	m, n = np.shape(data_matrix)
	weights = np.ones(n)  # 参数初始化
	for j in range(num_iter):
		data_index = list(range(m))
		for i in range(m):
			alpha = 4 / (1.0 + j + i) + 0.01  # 降低alpha的大小，每次减小1/(j+i)。
			rand_index = int(random.uniform(0, len(data_index)))  # 随机选取样本
			h = sigmoid(sum(data_matrix[rand_index] * weights))  # 选择随机选取的一个样本，计算h
			error = class_labels[rand_index] - h  # 计算误差
			weights = weights + alpha * error * data_matrix[rand_index]  # 更新回归系数
			del (data_index[rand_index])  # 删除已经使用的样本
	return weights  # 返回


if __name__ == '__main__':
	dataMat, labelMat = load_data_set('../resource/testSet.txt')
	weights = stoc_grad_ascent1(np.array(dataMat), labelMat)
	plot_best_fit(weights)
