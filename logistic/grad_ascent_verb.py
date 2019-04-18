#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-04-17 14:21
@Author  : red
@Site    : 
@File    : grad_ascent_verb.py
@Software: PyCharm
"""
from utils.sigmoid_util import sigmoid
from load_data.load_data import load_data_set
import numpy as np
import matplotlib.pyplot as plt

'''
1 Logistic回归介绍
       假设现在有一些数据点，我们用一条直线对这些点进行拟合（该线称为最佳拟合直线），这个拟合过程就称作回归。利用Logistic回归进行分类的主要思想是：根据现有数据对分类边界线建立回归公式，以此进行分类。这里的“回归”一词源于最佳拟合，表示要找到最佳拟合参数集。训练分类器时的做法就是寻找最佳拟合参数，使用的是最优化算法。

1.1
Logistic回归的一般过程
(1)
收集数据：采用任意方法收集数据。
(2)
准备数据：由于需要进行距离计算，因此要求数据类型为数值型。另外，结构化数据格式则最佳。
(3)
分析数据：采用任意方法对数据进行分析。
(4)
训练算法：大部分时间将用于训练，训练的目的是为了找到最佳的分类回归系数。
(5)
测试算法：一旦训练步骤完成，分类将会很快。
(6)
使用算法：首先，我们需要输入一些数据，并将其转换成对应的结构化数值；接着，基于训练好的回归系数就可以对这些数值进行简单的回归计算，判定它们属于哪个类别；在这之后，我们就可以在输出的类别上做一些其他分析工作。

# %% md
2
基于
Logistic
回归和
Sigmoid
函数的分类
2.1
Logistic回归特点
优点：计算代价不高，易于理解和实现。
缺点：容易欠拟合，分类精度可能不高。
适用数据类型：数值型和标称型数据。
'''

'''
Logistic 逻辑回归梯度上升优化算法
梯度上升算法在每次更新回归系数(最优参数)时，都需要遍历整个数据集。
假设，我们使用的数据集一共有100个样本。那么，dataMatrix就是一个100*3的矩阵。每次计算h的时候，都要计算dataMatrix*weights这个矩阵乘法运算，要进行100*3次乘法运算和100*2
次加法运算。同理，更新回归系数(最优参数)weights时，也需要用到整个数据集，要进行矩阵乘法运算。总而言之，该方法处理100
个左右的数据集时尚可，但如果有数十亿样本和成千上万的特征，那么该方法的计算复杂度就太高了。
'''


def grad_ascent(data_mat_in, class_labels):
	# convert to numpy matrix
	data_matrix = np.mat(data_mat_in)
	label_mat = np.mat(class_labels).transpose()
	m, n = np.shape(data_matrix)
	alpha = 0.001
	max_cycles = 500
	weights = np.ones((n, 1))
	for k in range(max_cycles):
		h = sigmoid(data_matrix * weights)
		error = (label_mat - h)
		weights = weights + alpha * data_matrix.transpose() * error
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
	weights = grad_ascent(dataMat, labelMat)
	plot_best_fit(weights.getA())
