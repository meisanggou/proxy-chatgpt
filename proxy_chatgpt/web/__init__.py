# !/usr/bin/env python
# coding: utf-8
from flask_helper import Flask2

from proxy_chatgpt.utils.log import getLogger

__author__ = 'zhouhenglc'


LOG = getLogger()

def get_app():
    app = Flask2(__name__, log=LOG)
    app.real_ip()
    return app
