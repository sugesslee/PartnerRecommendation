#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-04-18 12:46
@Author  : red
@Site    : 
@File    : insert_AMiner_Paper_to_sql.py
@Software: PyCharm
"""
import numpy as np
from utils import sql_util
import time


def get_data_from_txt(file_path):
	result = []
	strip = ['#index ', '#n ', '#a ', '#pc ', '#cn ', '#hi ', '#pi ', '#upi ', '#t ']
	with open(file_path, 'r', encoding='utf-8') as f:
		lines = f.readlines()
	for i in range(0, len(lines), 10):
		line = lines[i:i + 9]
		temp = []
		[temp.append(element.rstrip('\n')) for element in np.array(line)]
		tmp = []
		for j in range(len(temp)):
			tmp.append(temp[j].lstrip(strip[j]))
		result.append(tuple(tmp))
	print("[{}]--get data finally, data num is {}...".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
															 len(result)))
	return result


def insert_to_sql(data):
	truncate_sql = "truncate table AMiner_Paper"
	sql_util.execute(truncate_sql)
	sql_str = "insert into AMiner_Paper(index_id, n, a, pc, cn, hi, pi, upi, t) values(%s, %s, %s, %s, %s, %s, %s, " \
			  "%s, %s)"
	for i in range(0, len(data), 100):
		if i + 100 > len(data):
			insert_data = data[i:len(data - i)]
		else:
			insert_data = data[i:i + 100]
		result = sql_util.insertmany(sql_str, insert_data)
	print("[{}]--insert data num is {}...".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), result))


if __name__ == '__main__':
	data = get_data_from_txt('../resource/AMiner-Paper.txt')
	insert_to_sql(data)
