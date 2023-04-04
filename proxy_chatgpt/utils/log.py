# !/usr/bin/env python
# coding: utf-8
import logging
from logging import Formatter, StreamHandler
from logging.handlers import WatchedFileHandler

import os
import sys


__author__ = 'zhouhenglc'

LOG_LEVEL = logging.INFO
LOG_FILE = os.getenv('LOG_PATH')

fmt = Formatter('%(asctime)s:%(levelname)s:%(message)s')

if LOG_FILE:
    file_handler = WatchedFileHandler(LOG_FILE)
    file_handler.level = logging.DEBUG
    file_handler.setFormatter(fmt)
else:
    file_handler = None

console_handle = StreamHandler(sys.stdout)
console_handle.level = logging.DEBUG
console_handle.setFormatter(fmt)


def set_logger_as_root(name):
    logger = logging.getLogger(name)
    if file_handler:
        logger.addHandler(file_handler)
    else:
        logger.addHandler(console_handle)
    logger.setLevel(LOG_LEVEL)
    logger.propagate = False
    return logger


def getLogger(name='proxy-chatgpt'):
    logger = logging.getLogger(name)
    return logger


set_logger_as_root(None)
set_logger_as_root('proxy-chatgpt')
