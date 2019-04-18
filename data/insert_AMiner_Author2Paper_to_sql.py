#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-04-18 12:46
@Author  : red
@Site    : 
@File    : insert_AMiner_Author_to_sql.py
@Software: PyCharm
"""
from utils import sql_util
import time


def get_data_from_txt(file_path):
	result = []
	with open(file_path, 'r', encoding='utf-8') as f:
		lines = f.readlines()
		for line in lines:
			line_lst = str.split(line.rstrip('\n'), '\t')
			tmp = []
			[tmp.append(element.lstrip('#')) for element in line_lst]
			result.append(tuple(tmp))
	print("[{}]--get data finally, data num is {}...".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
															 len(result)))
	return result


def insert_to_sql(data):
	truncate_sql = "truncate table AMiner_Author2Paper"
	sql_util.execute(truncate_sql)
	sql_str = "insert into AMiner_Author2Paper(index_id, author_id, paper_id, position) values(%s, %s, %s, %s)"
	num = 0
	for i in range(0, len(data), 100):
		if i + 100 > len(data):
			insert_data = data[i:len(data - i)]
		else:
			insert_data = data[i:i + 100]
		result = sql_util.insertmany(sql_str, insert_data)
		num += result
		print("[{}]--insert data num is {}...".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), num))


if __name__ == '__main__':
	data = get_data_from_txt('../resource/AMiner-Author2Paper.txt')
	insert_to_sql(data)
