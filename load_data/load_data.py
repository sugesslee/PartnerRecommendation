#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-04-17 22:48
@Author  : red
@Site    : 
@File    : load_data.py
@Software: PyCharm
"""


def load_data_set(file_path):
	# 创建两个表
	data_mat = []
	label_mat = []

	with open(file_path) as f:
		lines = f.readlines()
		for line in lines:
			# 对当前行去除收尾空格，并按空格进行分离
			line_arr = line.strip().split()
			data_mat.append([1.0, float(line_arr[0]), float(line_arr[1])])
			label_mat.append(int(line_arr[2]))
	return data_mat, label_mat
