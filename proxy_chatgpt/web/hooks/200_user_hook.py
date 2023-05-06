# !/usr/bin/env python
# coding: utf-8
from flask import g
from flask import request

from flask_login import current_user

from flask_helper.flask_hook import FlaskHook

__author__ = 'zhouhenglc'


class UserHook(FlaskHook):
    priority = 200

    def before_request(self):
        if current_user.is_authenticated:
            g.user_role = current_user.role
            g.user_name = current_user.user_name
            self.log.info('receive request: user:%s role:%s method:%s full_path:%s',
                     g.user_name, g.user_role, request.method, request.full_path)
        else:
            g.user_role = 0
            g.user_name = None
