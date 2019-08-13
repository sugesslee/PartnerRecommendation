#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2018-12-21 17:43
@Author  : red
@Site    : 
@File    : logger_util.py
@Software: PyCharm
Python 日志工具包
"""
import logging.handlers

log_file = '../logs/output.log'

fmt = '%(asctime)s - %(levelname)s - %(filename)s#%(funcName)s():%(lineno)s - %(name)s - %(message)s'

# 实例化handler
handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=5)
formatter = logging.Formatter(fmt)  # 实例化formatter
handler.setFormatter(formatter)  # 为handler添加formatter

logger = logging.getLogger("main")  # 获取名为tst的logger
logger.addHandler(handler)  # 为logger添加handler
logger.setLevel(logging.DEBUG)  # 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'

if __name__ == '__main__':
    logger.info("process the %d thread file total num is %d", 100, 100)
    logger.info("log is %s", "log")
    logger.debug("first message debug")
    logger.info("first message info")
    logger.warning("first message warning")
    logger.error("first message error")
    logger.critical("first message critical")
