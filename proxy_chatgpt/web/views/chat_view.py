# !/usr/bin/env python
# coding: utf-8
from flask import request

from flask_helper.view import View

from proxy_chatgpt.objects.api import ChatGPTAPI


__author__ = 'zhouhenglc'

chat_view = View('chat', __name__, url_prefix='/chat')
chat_api = ChatGPTAPI()


@chat_view.route('/completions', methods=['POST'])
def start_chat():
    data = request.json
    message = data['message']
    if not message:
        message = "Hello!"
    else:
        res = chat_api.create(message)
        print(res)
        message = res['choices'][0]['message']['content']
    reply_data = {'responses': [message]}
    return {'status': True, 'data': reply_data}
