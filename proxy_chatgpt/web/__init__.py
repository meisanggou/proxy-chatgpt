# !/usr/bin/env python
# coding: utf-8
from flask import session

from flask_helper import Flask2
from flask_login import LoginManager
from flask_login import UserMixin

from proxy_chatgpt.utils.log import getLogger
from proxy_chatgpt.web import env_filters

__author__ = 'zhouhenglc'


LOG = getLogger()
login_manager = LoginManager()
login_manager.session_protection = 'strong'


class User(UserMixin):
    user_name = ""

    def get_id(self):
        return self.user_name


@login_manager.user_loader
def load_user(user_name):
    user = User()
    user.user_name = user_name
    if "role" not in session:
        session["role"] = 0
    user.role = session["role"]
    return user


def get_app():
    app = Flask2(__name__, log=LOG)
    app.secret_key = 'Proxy-ChatGPT0427'

    login_manager.init_app(app)
    app.real_ip()
    env = app.jinja_env
    env.filters['make_static_html'] = env_filters.make_static_html
    env.filters['make_static_url'] = env_filters.make_static_url
    return app
