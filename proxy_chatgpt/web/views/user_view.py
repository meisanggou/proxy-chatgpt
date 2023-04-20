# !/usr/bin/env python
# coding: utf-8
from flask_helper.view import View

__author__ = 'zhouhenglc'


user_view = View('user', __name__, url_prefix='/user')

@user_view.route('/login', methods=['POST'])
def user_login():
    return {'status': True}
