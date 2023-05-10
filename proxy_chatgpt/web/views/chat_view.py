# !/usr/bin/env python
# coding: utf-8
from flask import g
from flask import request
import json

from proxy_chatgpt.objects.api import ChatGPTAPI
from proxy_chatgpt.objects.chat import ChatFlow
from proxy_chatgpt.utils.log import getLogger
from proxy_chatgpt.web.view import View2


__author__ = 'zhouhenglc'

LOG = getLogger()

chat_view = View2('chat', __name__, url_prefix='/chat', auth_required=True)
chat_api = ChatGPTAPI()
chat_flow = ChatFlow()


@chat_view.route('/completions', methods=['POST'])
def start_chat():
    data = request.json
    message = data['message']
    if not message:
        message = "Hello!"
    else:
        res = chat_api.create(message)
        usage = res['usage']
        usage['ip'] = g.remote_addr
        LOG.info('[%s][usage] %s [usage]', g.user_no, json.dumps(usage))
        chat_flow.new(g.session, g.user_no, usage['prompt_tokens'],
                      usage['completion_tokens'], g.remote_addr)
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
        LOG.info('[%s][usage] %s [usage]', g.user_no, json.dumps(usage))
        chat_flow.new(g.session, g.user_no, usage['prompt_tokens'],
                      usage['completion_tokens'], g.remote_addr)
        message = res['choices'][0]['message']['content']
    reply_data = {'responses': [message]}
    return {'status': True, 'data': reply_data}
