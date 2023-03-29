# !/usr/bin/env python
# coding: utf-8
from flask import render_template
from flask_helper.view import View

__author__ = 'zhouhenglc'

page_view = View('page', __name__, url_prefix='/')


@page_view.route('/')
def page_view_index():
    return render_template('chat.html')