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
	sql_str = "select n, a , pc, cn, hi, pi, upi, t from AMiner_Author limit 1000"
	data = sql.queryall(sql_str)
	return data


def export_csv_data():
	data_frame = pd.DataFrame(get_data())
	data_frame.to_csv("../resource/author.csv", index=False, sep=',', header=False)


if __name__ == '__main__':
	export_csv_data()
