# !/usr/bin/env python
# coding: utf-8
from flask_helper import Flask2
from flask_login import LoginManager

from proxy_chatgpt.utils.log import getLogger
from proxy_chatgpt.web import env_filters

__author__ = 'zhouhenglc'


LOG = getLogger()
login_manager = LoginManager()
login_manager.session_protection = 'strong'


def get_app():
    app = Flask2(__name__, log=LOG)
    login_manager.init_app(app)
    app.real_ip()
    env = app.jinja_env
    env.filters['make_static_html'] = env_filters.make_static_html
    env.filters['make_static_url'] = env_filters.make_static_url
    return app
