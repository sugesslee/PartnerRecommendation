#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-04-17 22:53
@Author  : red
@Site    : 
@File    : sigmoid_util.py
@Software: PyCharm
"""
import numpy as np


def sigmoid(inx):
	return 1.0 / (1 + np.exp(-inx))
