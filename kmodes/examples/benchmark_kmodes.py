#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-05-20 11:22
@Author  : red
@Site    : 
@File    : benchmark_kmodes.py
@Software: PyCharm
"""
import timeit

import numpy as np

from kmodes.kmodes import KModes
from kmodes.utils.dissim import ng_dissim

# number of clusters
K = 20
# no. of points
N = int(1e5)
# no. of dimensions
M = 10
# no. of times test is repeated
T = 3

data = np.random.randint(1, 1000, (N, M))


def huang():
	KModes(
		n_clusters=K,
		init='Huang',
		n_init=1,
		verbose=2
	).fit_predict(data)


def huang_ng_dissim():
	KModes(
		n_clusters=K,
		init='Huang',
		cat_dissim=ng_dissim,
		n_init=1,
		verbose=2
	).fit_predict(data)


def cao():
	KModes(
		n_clusters=K,
		init='Cao',
		verbose=2
	).fit_predict(data)


if __name__ == '__main__':

	for cm in ('huang', 'huang_ng_dissim', 'cao'):
		print(cm.capitalize() + ': {:.2} seconds'.format(
			timeit.timeit(cm + '()',
						  setup='from __main__ import ' + cm,
						  number=T)))
