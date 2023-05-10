# !/usr/bin/env python
# coding: utf-8
from contextlib import contextmanager
from flask import g
from flask import has_app_context
from flask_login import login_required

from flask_helper.view import View

from proxy_chatgpt.db import session


__author__ = 'zhouhenglc'


class Context(object):

    def __init__(self):
        self._session = None

    @property
    def session(self):
        return self._session

    @session.setter
    def session(self, s):
        if has_app_context():
            g.session = s
        self._session = s


class View2(View):

    def __init__(self, name, import_name, **kwargs):
        auth_required = kwargs.pop('auth_required', False)
        super().__init__(name, import_name, **kwargs)
        if auth_required:
            @self.before_request
            @login_required
            def before_request():
                pass

    @classmethod
    @contextmanager
    def view_context_func(cls):
        with session.use_session() as _session:
            context = Context()
            context.session = _session
            yield context