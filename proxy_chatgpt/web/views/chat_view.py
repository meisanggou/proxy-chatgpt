# !/usr/bin/env python
# coding: utf-8
from flask import request

from flask_helper.view import View

__author__ = 'zhouhenglc'

chat_view = View('chat', __name__, url_prefix='/chat')


@chat_view.route('/completions', methods=['POST'])
def start_chat():
    data = request.json
    message = data['message']
    if not message:
        message = "Hello!"
    reply_data = {'responses': [message]}
    return {'status': True, 'data': reply_data}
