# !/usr/bin/env python
# coding: utf-8
import os
import openai
__author__ = 'zhouhenglc'


class ChatGPTAPI(object):
    _inst = None
    def __new__(cls, *args, **kwargs):
        if not cls._inst:
            cls._inst = super().__new__(cls)
        return cls._inst

    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        proxy = os.getenv('OPENAI_PROXY')
        if proxy:
            openai.proxy = proxy

    def create(self, message):
        _msg = {'role': 'user', 'content': message}
        return self.create2(_msg)

    def create2(self, messages):
        response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=messages,
          temperature=0.9,
          max_tokens=500,
          top_p=1,
          frequency_penalty=0.0,
          presence_penalty=0.6,
          # stop=["\n"]
        )
        return response
