# !/usr/bin/env python
# coding: utf-8
from flask_login import login_required

from flask_helper.view import View


__author__ = 'zhouhenglc'


class View2(View):

    def __init__(self, name, import_name, **kwargs):
        auth_required = kwargs.pop('auth_required', False)
        super().__init__(name, import_name, **kwargs)
        if auth_required:
            @self.before_request
            @login_required
            def before_request():
                pass
