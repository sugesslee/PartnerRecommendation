#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-04-18 20:40
@Author  : red
@Site    :
@File    : K-means.py
@Software: PyCharm
"""

import random

import numpy as np
import matplotlib.pyplot as plt


def show_fig():
    data = load_data()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(data[:, 0], data[:, 1])
    plt.show()


def cal_distance(node1, node2):
    """
    计算两个向量之间的欧式距离
    :param node1:
    :param node2:
    :return:
    """
    return np.sqrt(np.sum(np.square(node1 - node2)))


def load_data():
    """
    加载数据
    , usecols=(1, 2, 3, 4, 5)
    :return:
    """
    data = np.loadtxt("../resources/data/author.csv", skiprows=1)
    return data


def init_k_node(data, k):
    """
    随机初始化k个数据返回
    :param data:
    :param k:
    :return:
    """
    # np.delete删除数组行或列 axis=1列 axis=0行
    data = list(np.delete(data, [0], axis=1))

    return random.sample(data, k)


def get_clusters(data, k_centroids):
    """
    计算各个节点所属的簇类
    :param data:
    :param k_centroids:
    :return:
    """
    cluster_dict = dict()
    k = len(k_centroids)
    for node in data:
        # 计算节点node与k个质心的距离，选取距离最近的，并将节点加入相应簇类中
        cluster_idx = -1
        min_dis = float("inf")
        for idx in range(k):
            centroid = k_centroids[idx]
            print(node[1:])
            print(centroid)
            distance = cal_distance(node[1:], centroid)
            if distance < min_dis:
                min_dis = distance
                cluster_idx = idx

        if cluster_idx not in cluster_dict.keys():
            cluster_dict[cluster_idx] = []
        cluster_dict[cluster_idx].append(node[1:])  # 加入对应类别中
    return cluster_dict


def get_centroids(cluster_dict):
    """
    重新计算k个质心
    :param cluster_dict:
    :return:
    """
    new_k_centroids = []
    for cluster_idx in cluster_dict.keys():
        new_centroid = np.mean(cluster_dict[cluster_idx], axis=0)
        new_k_centroids.append(new_centroid)
    return new_k_centroids


def get_variance(centroids, cluster_dict):
    """
    计算各个簇集合的均方误差
    将簇类中各个节点与质心的距离累加求和
    :param centroids:
    :param cluster_dict:
    :return:
    """
    accumulate_sum = 0.0
    for cluster_idx in cluster_dict.keys():
        centroid = centroids[cluster_idx]
        distance = 0.0
        for node in cluster_dict[cluster_idx]:
            distance += cal_distance(node, centroid)
        accumulate_sum += distance
    return accumulate_sum


def show_cluster(centroids, cluster_dict):
    """
    展示聚类结果
    :param centroids:
    :param cluster_dict:
    :return:
    """
    color_mark = ['or', 'ob', 'og', 'ok', 'oy', 'ow']
    centroid_mark = ['dr', 'db', 'dg', 'dk', 'dy', 'dw']

    for key in cluster_dict.keys():
        plt.plot(centroids[key][0], centroids[key][1], centroid_mark[key], markersize=12)  # 质心点
        for node in cluster_dict[key]:
            plt.plot(node[0], node[1], color_mark[key])
    plt.show()


def main():
    data = load_data()
    centroids = init_k_node(data, 4)
    cluster_dict = get_clusters(data, centroids)
    new_var = get_variance(centroids, cluster_dict)
    old_var = 1

    # 当两次聚类的误差小于某个值时，说明质心基本稳定
    while abs(new_var - old_var) >= 0.00001:
        centroids = get_centroids(cluster_dict)
        cluster_dict = get_clusters(data, centroids)
        old_var = new_var
        new_var = get_variance(centroids, cluster_dict)
        show_cluster(centroids, cluster_dict)
    print(cluster_dict)


if __name__ == '__main__':
    show_fig()
    main()
