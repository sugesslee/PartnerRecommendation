#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-08-01 13:48
@Author  : red
@Site    : 
@File    : agnes.py
@Software: PyCharm
"""
import time
# -*- coding:utf-8 -*-
import math
import pylab as pl


def dist(node1, node2):
    """
    计算欧几里得距离,node1,node2分别为两个元组
    :param node1:
    :param node2:
    :return:
    """
    return math.sqrt(math.pow(node1[0] - node2[0], 2) + math.pow(node1[1] - node2[1], 2))


def dist_min(cluster_x, cluster_y):
    """
    Single Linkage
    又叫做 nearest-neighbor ，就是取两个类中距离最近的两个样本的距离作为这两个集合的距离。
    :param cluster_x:
    :param cluster_y:
    :return:
    """
    return min(dist(node1, node2) for node1 in cluster_x for node2 in cluster_y)


def dist_max(cluster_x, cluster_y):
    """
    Complete Linkage
    这个则完全是 Single Linkage 的反面极端，取两个集合中距离最远的两个点的距离作为两个集合的距离。
    :param cluster_x:
    :param cluster_y:
    :return:
    """
    return max(dist(node1, node2) for node1 in cluster_x for node2 in cluster_y)


def dist_avg(cluster_x, cluster_y):
    """
    Average Linkage
    这种方法就是把两个集合中的点两两的距离全部放在一起求均值，相对也能得到合适一点的结果。
    :param cluster_x:
    :param cluster_y:
    :return:
    """
    return sum(dist(node1, node2) for node1 in cluster_x for node2 in cluster_y) / (len(cluster_x) * len(cluster_y))


def find_min(distance_matrix):
    """
    找出距离最近的两个簇下标
    :param distance_matrix:
    :return:
    """
    min = 1000
    x = 0;
    y = 0
    for i in range(len(distance_matrix)):
        for j in range(len(distance_matrix[i])):
            if i != j and distance_matrix[i][j] < min:
                min = distance_matrix[i][j];
                x = i;
                y = j
    return (x, y, min)


def AGNES(dataset, distance_method, k):
    """
    聚类算法模型
    :param dataset: 数据集
    :param distance_method: 计算簇类聚类的方法
    :param k: 目标簇类数目
    :return:
    """
    print(len(dataset))
    # 初始化簇类集合和距离矩阵
    cluster_set = []
    distance_matrix = []
    for node in dataset:
        cluster_set.append([node])
    print('original cluster set:')
    print(cluster_set)
    for cluster_x in cluster_set:
        distance_list = []
        for cluster_y in cluster_set:
            distance_list.append(distance_method(cluster_x, cluster_y))
        distance_matrix.append(distance_list)
    print('original distance matrix:')
    print(len(distance_matrix), len(distance_matrix[0]), distance_matrix)
    q = len(dataset)
    # 合并更新
    while q > k:
        id_x, id_y, min_distance = find_min(distance_matrix)
        cluster_set[id_x].extend(cluster_set[id_y])
        cluster_set.remove(cluster_set[id_y])
        distance_matrix = []

        for cluster_x in cluster_set:
            distance_list = []
            for cluster_y in cluster_set:
                distance_list.append(distance_method(cluster_x, cluster_y))
            distance_matrix.append(distance_list)
        q -= 1
    return cluster_set


def draw(cluster_set):
    """
    画图
    :param cluster_set:
    :return:
    """
    color_list = ['r', 'y', 'g', 'b', 'c', 'k', 'm']

    for cluster_idx, cluster in enumerate(cluster_set):
        coo_x = []  # x坐标列表
        coo_y = []  # y坐标列表

        for node in cluster:
            coo_x.append(node[0])
            coo_y.append(node[1])
        pl.scatter(coo_x, coo_y, marker='x', color=color_list[cluster_idx % len(color_list)], label=cluster_idx)

    pl.legend(loc='upper right')
    pl.show()


if __name__ == '__main__':
    # 数据集：每三个是一组分别是西瓜的编号，密度，含糖量
    data = """
    1,0.697,0.46,2,0.774,0.376,3,0.634,0.264,4,0.608,0.318,5,0.556,0.215,
    6,0.403,0.237,7,0.481,0.149,8,0.437,0.211,9,0.666,0.091,10,0.243,0.267,
    11,0.245,0.057,12,0.343,0.099,13,0.639,0.161,14,0.657,0.198,15,0.36,0.37,
    16,0.593,0.042,17,0.719,0.103,18,0.359,0.188,19,0.339,0.241,20,0.282,0.257,
    21,0.748,0.232,22,0.714,0.346,23,0.483,0.312,24,0.478,0.437,25,0.525,0.369,
    26,0.751,0.489,27,0.532,0.472,28,0.473,0.376,29,0.725,0.445,30,0.446,0.459"""

    # 数据处理 dataset是30个样本（密度，含糖量）的列表
    a = data.split(',')
    dataset = [(float(a[i]), float(a[i + 1])) for i in range(1, len(a) - 1, 3)]
    print(dataset)
    cluster_set = AGNES(dataset, dist_avg, 3)
    print('final cluster set:')
    print(cluster_set)
    draw(cluster_set)
