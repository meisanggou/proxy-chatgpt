# !/usr/bin/env python
# coding: utf-8
from flask import g
from flask import request
import json

from flask_helper.view import View

from proxy_chatgpt.objects.api import ChatGPTAPI
from proxy_chatgpt.utils.log import getLogger


__author__ = 'zhouhenglc'

LOG = getLogger()

chat_view = View('chat', __name__, url_prefix='/chat')
chat_api = ChatGPTAPI()


@chat_view.route('/completions', methods=['POST'])
def start_chat():
    data = request.json
    print(g.remote_addr)
    message = data['message']
    if not message:
        message = "Hello!"
    else:
        res = chat_api.create(message)
        usage = res['usage']
        usage['ip'] = g.remote_addr
        LOG.info('[usage] %s [usage]', json.dumps(usage))
        message = res['choices'][0]['message']['content']
    reply_data = {'responses': [message]}
    return {'status': True, 'data': reply_data}


@chat_view.route('/vip/completions', methods=['POST'])
def start_vip_chat():
    data = request.json
    messages = data['messages']
    if not messages:
        message = "Hello VIP!"
    else:
        res = chat_api.create2(messages)
        usage = res['usage']
        usage['ip'] = g.remote_addr
        LOG.info('[usage] %s [usage]', json.dumps(usage))
        message = res['choices'][0]['message']['content']
    reply_data = {'responses': [message]}
    return {'status': True, 'data': reply_data}
