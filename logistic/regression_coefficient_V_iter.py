#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-04-17 22:44
@Author  : red
@Site    : 
@File    : regression_coefficient_V_iter.py
@Software: PyCharm
"""
from load_data.load_data import load_data_set
from utils.sigmoid_util import sigmoid
from matplotlib.font_manager import FontProperties
import numpy as np
import matplotlib.pyplot as plt

'''
由于改进的随机梯度上升算法，随机选取样本点，所以每次的运行结果是不同的。但是大体趋势是一样的。我们改进的随机梯度上升算法收敛效果更好。为什么这么说
呢？让我们分析一下。我们一共有100个样本点，改进的随机梯度上升算法迭代次数为150。而上图显示15000次迭代次数的原因是，使用一次样本就更新一下回归
系数。因此，迭代150次，相当于更新回归系数150*100=15000次。简而言之，迭代150次，更新1.5万次回归参数。从上图左侧的改进随机梯度上升算法回归效果
中可以看出，其实在更新2000次回归系数的时候，已经收敛了。相当于遍历整个数据集20次的时候，回归系数已收敛。训练已完成。

再让我们看看上图右侧的梯度上升算法回归效果，梯度上升算法每次更新回归系数都要遍历整个数据集。从图中可以看出，当迭代次数为300多次的时候，回归系数
才收敛。凑个整，就当它在遍历整个数据集300次的时候已经收敛好了。
'''


def grad_ascent(dataMatIn, classLabels):
	dataMatrix = np.mat(dataMatIn)  # 转换成numpy的mat
	labelMat = np.mat(classLabels).transpose()  # 转换成numpy的mat,并进行转置
	m, n = np.shape(dataMatrix)  # 返回dataMatrix的大小。m为行数,n为列数。
	alpha = 0.01  # 移动步长,也就是学习速率,控制更新的幅度。
	maxCycles = 500  # 最大迭代次数
	weights = np.ones((n, 1))
	weights_array = np.array([])
	for k in range(maxCycles):
		h = sigmoid(dataMatrix * weights)  # 梯度上升矢量化公式
		error = labelMat - h
		weights = weights + alpha * dataMatrix.transpose() * error
		weights_array = np.append(weights_array, weights)
	weights_array = weights_array.reshape(maxCycles, n)
	return weights.getA(), weights_array  # 将矩阵转换为数组，并返回


# 改进后的随机梯度上升算法
def stoc_grad_ascent1(data_matrix, class_labels, num_iter=150):
	m, n = np.shape(data_matrix)
	weights = np.ones(n)
	weights_array = np.array([])  # 存储每次更新的回归系数
	for j in range(num_iter):
		data_index = list(range(m))
		for i in range(m):
			alpha = 4 / (1.0 + j + i) + 0.000  # 降低alpha的大小，每次减小1/(j+i)

			rand_index = int(np.random.uniform(0, len(data_index)))  # 随机选取样本
			h = sigmoid(sum(data_matrix[rand_index] * weights))  # 选择随机选取的一个样本，计算h
			error = class_labels[rand_index] - h  # 计算误差
			weights = weights + alpha * error * data_matrix[rand_index]  # 更新回归系数
			weights_array = np.append(weights_array, weights, axis=0)  # 添加回归系数到数组中
			del (data_index[rand_index])
	weights_array = weights_array.reshape(num_iter * m, n)  # 改变维度
	return weights, weights_array


def plot_weights(weights_array1, weights_array2):
	# 设置汉字格式
	# font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
	font = FontProperties(fname=r"/Users/red/Library/Fonts/88761586021.ttc", size=14)
	# 将fig画布分隔成1行1列,不共享x轴和y轴,fig画布的大小为(13,8)
	# 当nrow=3,nclos=2时,代表fig画布被分为六个区域,axs[0][0]表示第一行第一列
	fig, axs = plt.subplots(nrows=3, ncols=2, sharex=False, sharey=False, figsize=(20, 10))
	x1 = np.arange(0, len(weights_array1), 1)
	# 绘制w0与迭代次数的关系
	axs[0][0].plot(x1, weights_array1[:, 0])
	axs0_title_text = axs[0][0].set_title(u'梯度上升算法：回归系数与迭代次数关系', FontProperties=font)
	axs0_ylabel_text = axs[0][0].set_ylabel(u'W0', FontProperties=font)
	plt.setp(axs0_title_text, size=20, weight='bold', color='black')
	plt.setp(axs0_ylabel_text, size=20, weight='bold', color='black')
	# 绘制w1与迭代次数的关系
	axs[1][0].plot(x1, weights_array1[:, 1])
	axs1_ylabel_text = axs[1][0].set_ylabel(u'W1', FontProperties=font)
	plt.setp(axs1_ylabel_text, size=20, weight='bold', color='black')
	# 绘制w2与迭代次数的关系
	axs[2][0].plot(x1, weights_array1[:, 2])
	axs2_xlabel_text = axs[2][0].set_xlabel(u'迭代次数', FontProperties=font)
	axs2_ylabel_text = axs[2][0].set_ylabel(u'W1', FontProperties=font)
	plt.setp(axs2_xlabel_text, size=20, weight='bold', color='black')
	plt.setp(axs2_ylabel_text, size=20, weight='bold', color='black')

	x2 = np.arange(0, len(weights_array2), 1)
	# 绘制w0与迭代次数的关系
	axs[0][1].plot(x2, weights_array2[:, 0])
	axs0_title_text = axs[0][1].set_title(u'改进的随机梯度上升算法：回归系数与迭代次数关系', FontProperties=font)
	axs0_ylabel_text = axs[0][1].set_ylabel(u'W0', FontProperties=font)
	plt.setp(axs0_title_text, size=20, weight='bold', color='black')
	plt.setp(axs0_ylabel_text, size=20, weight='bold', color='black')
	# 绘制w1与迭代次数的关系
	axs[1][1].plot(x2, weights_array2[:, 1])
	axs1_ylabel_text = axs[1][1].set_ylabel(u'W1', FontProperties=font)
	plt.setp(axs1_ylabel_text, size=20, weight='bold', color='black')
	# 绘制w2与迭代次数的关系
	axs[2][1].plot(x2, weights_array2[:, 2])
	axs2_xlabel_text = axs[2][1].set_xlabel(u'迭代次数', FontProperties=font)
	axs2_ylabel_text = axs[2][1].set_ylabel(u'W1', FontProperties=font)
	plt.setp(axs2_xlabel_text, size=20, weight='bold', color='black')
	plt.setp(axs2_ylabel_text, size=20, weight='bold', color='black')

	plt.show()


if __name__ == '__main__':
	dataMat, labelMat = load_data_set('../resource/testSet.txt')
	weights1, weights_array1 = stoc_grad_ascent1(np.array(dataMat), labelMat)

	weights2, weights_array2 = grad_ascent(dataMat, labelMat)
	plot_weights(weights_array1, weights_array2)
