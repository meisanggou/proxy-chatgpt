# !/usr/bin/env python
# coding: utf-8
import random

from proxy_chatgpt.db.models import chat as chat_model
from proxy_chatgpt.objects import base

__author__ = 'zhouhenglc'


class ChatFlow(base.BaseObject):
    model = chat_model.ChatFlowModel

    def gen_flow_no(self):
        return int(self.now_time * 100000 + random.randint(0, 99))

    def new(self, session, user_no, prompt_tokens, completion_tokens, ip):
        kwargs = {'flow_no': self.gen_flow_no(), 'user_no': user_no,
                  'prompt_tokens': prompt_tokens,
                  'completion_tokens': completion_tokens,
                  'ip': ip, 'tags': 1}
        return self.create(session, **kwargs)
