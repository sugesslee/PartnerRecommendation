#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-04-17 23:41
@Author  : red
@Site    : 
@File    : grad_ascent.py
@Software: PyCharm
"""
from load_data.load_data import load_data_set
from utils.sigmoid_util import sigmoid
import numpy as np
import matplotlib.pyplot as plt


def stoc_grad_ascent0(data_matrix, class_labels):
	m, n = np.shape(data_matrix)
	alpha = 0.01
	weights = np.ones(n)

	for i in range(m):
		h = sigmoid(sum(data_matrix[i] * weights))
		error = class_labels[i] - h
		weights = weights + alpha * error * data_matrix[i]
	return weights


# 画出数据集和logistic回归最佳拟合直线的函数
def plot_best_fit(weights):
	data_mat, label_mat = dataMat, labelMat
	data_arr = np.array(data_mat)
	n = np.shape(data_arr)[0]

	xcord1 = []
	xcord2 = []
	ycord1 = []
	ycord2 = []

	for i in range(n):
		if int(label_mat[i]) == 1:
			xcord1.append(data_arr[i, 1])
			ycord1.append(data_arr[i, 2])
		else:
			xcord2.append(data_arr[i, 1])
			ycord2.append(data_arr[i, 2])

	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
	ax.scatter(xcord2, ycord2, s=30, c='green')
	x = np.arange(-3.0, 3.0, 0.1)
	y = (-weights[0] - weights[1] * x) / weights[2]
	ax.plot(x, y)
	plt.xlabel('X1')
	plt.ylabel('X2')
	plt.show()


if __name__ == '__main__':
	dataMat, labelMat = load_data_set('../resource/testSet.txt')
	weights = stoc_grad_ascent0(np.array(dataMat), labelMat)
	plot_best_fit(weights)
