#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-05-21 09:51
@Author  : red
@Site    : 
@File    : export_csv_data.py
@Software: PyCharm
"""
import pandas as pd
from utils import sql_util as sql


def get_data():
	# sql_str = "select n, a , pc, cn, hi, pi, upi, t from AMiner_Author limit 1000"
	sql_str = "select index_id, pc, cn, hi, pi, upi from AMiner_Author limit 3000"
	data = sql.queryall(sql_str)
	print(data)
	return data


def export_csv_data():
	columns = ['index_id', 'pc', 'cn', 'hi', 'pi', 'upi']
	data_frame = pd.DataFrame(get_data())
	data_frame.to_csv("../resources/data/author.csv", index=False, sep='\t', columns=columns)


if __name__ == '__main__':
	export_csv_data()
