#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-04-18 23:01
@Author  : red
@Site    : 
@File    : get_author_data_to_txt.py
@Software: PyCharm
"""
from utils import sql_util


# 获取数据时剔除无效数据
def get_data_from_sql():
	sql_str = "select pc, cn, hi, pi, upi from AMiner_Author where pc<>0 and cn<>0 and hi <>0 and pi<>0 and upi <> 0 " \
			  "limit 100000"
	data_result = sql_util.queryall(sql_str)
	return data_result


def write_data_txt(file_path, data):
	with open(file_path, 'w') as w:
		for element in data:
			pc = element.get('pc')
			cn = element.get('cn')
			hi = element.get('hi')
			pi = element.get('pi')
			upi = element.get('upi')
			line = pc + ',' + cn + ',' + hi + ',' + pi + ',' + upi
			w.write(line)
			w.write('\n')


if __name__ == '__main__':
	data = get_data_from_sql()
	write_data_txt('../resource/author_k-means_data.txt', data)
