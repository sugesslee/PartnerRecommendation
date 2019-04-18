#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-04-18 20:40
@Author  : red
@Site    : 
@File    : K-means.py
@Software: PyCharm
"""

from numpy import *
import matplotlib.pyplot as plt


def loadDataSet(fileName):
	dataSet = []
	f = open(fileName)
	for line in f.readlines():
		curLine = line.strip().split(',')  # 这里","表示以文件中数据之间的分隔符","分割字符串
		row = []
		for item in curLine:
			row.append(float(item))
		dataSet.append(row)

	return mat(dataSet)


# 求向量距离
def distEclud(vecA, vecB):
	return sqrt(sum(power(vecA - vecB, 2)))


# 随机生成k个点作为初始质心
# 若选择随机生成的点作为初始质心，则有可能导致后面更新质心时出现有的质心为 NaN(非数) 的情况
# def initCent(dataSet, k):
#     n = shape(dataSet)[1]  # n是列数
#     centroids = mat(zeros((k, n)))
#     for j in range(n):
#         minJ = min(dataSet[:, j])  # 找到第j列最小值
#         rangeJ = max(dataSet[:, j]) - minJ  # 求第j列最大值与最小值的差
#         centroids[:, j] = minJ + random.rand(k, 1) * rangeJ  # 生成k行1列的在(0, 1)之间的随机数矩阵
#     return centroids

# 选前k个点作为初始质心
def initCent(dataSet, k):
	data = []
	for i in range(k):
		data.append(dataSet[i].tolist())
	a = array(data)
	centroids = mat(a)
	return centroids


# K均值聚类算法实现
def KMeans(dataSet, k, distMeas=distEclud):
	m = shape(dataSet)[0]  # 数据集的行
	clusterAssment = mat(zeros((m, 2)))
	centroids = initCent(dataSet, k)
	clusterChanged = True
	while clusterChanged:
		clusterChanged = False
		for i in range(m):  # 遍历数据集中的每一行数据
			minDist = inf
			minIndex = -1
			for j in range(k):  # 寻找最近质心
				distJI = distMeas(centroids[j, :], dataSet[i, :])
				if distJI < minDist:  # 更新最小距离和质心下标
					minDist = distJI
					minIndex = j
			if clusterAssment[i, 0] != minIndex:
				clusterChanged = True
			clusterAssment[i, :] = minIndex, minDist ** 2  # 记录最小距离质心下标，最小距离的平方
		for cent in range(k):  # 更新质心位置
			ptsInClust = dataSet[nonzero(clusterAssment[:, 0].A == cent)[0]]  # 获得距离同一个质心最近的所有点的下标，即同一簇的坐标
			centroids[cent, :] = mean(ptsInClust, axis=0)  # 求同一簇的坐标平均值，axis=0表示按列求均值

	return centroids, clusterAssment


# 取数据的前两维特征作为该条数据的x , y 坐标，
def getXY(dataSet):
	import numpy as np
	m = shape(dataSet)[0]  # 数据集的行
	X = []
	Y = []
	for i in range(m):
		X.append(dataSet[i, 0])
		Y.append(dataSet[i, 1])
	return np.array(X), np.array(Y)


# 数据可视化
def showCluster(dataSet, k, clusterAssment, centroids):
	fig = plt.figure()
	plt.title("K-means")
	ax = fig.add_subplot(111)
	data = []

	for cent in range(k):  # 提取出每个簇的数据
		ptsInClust = dataSet[nonzero(clusterAssment[:, 0].A == cent)[0]]  # 获得属于cent簇的数据
		data.append(ptsInClust)

	for cent, c, marker in zip(range(k), ['r', 'g', 'b', 'y'], ['^', 'o', '*', 's']):  # 画出数据点散点图
		X, Y = getXY(data[cent])
		ax.scatter(X, Y, s=80, c=c, marker=marker)

	centroidsX, centroidsY = getXY(centroids)
	ax.scatter(centroidsX, centroidsY, s=1000, c='black', marker='+', alpha=1)  # 画出质心点
	ax.set_xlabel('X Label')
	ax.set_ylabel('Y Label')
	plt.show()


if __name__ == "__main__":
	cluster_Num = 3
	data = loadDataSet("../resource/author_k-means_data.txt")
	centroids, clusterAssment = KMeans(data, cluster_Num)
	showCluster(data, cluster_Num, clusterAssment, centroids)
