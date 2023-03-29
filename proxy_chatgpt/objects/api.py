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
        openai.proxy = "http://127.0.0.1:1080"

    def create(self, message):
        response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[{'role': 'user', 'content': message}],
          temperature=0.9,
          max_tokens=500,
          top_p=1,
          frequency_penalty=0.0,
          presence_penalty=0.6,
          # stop=["\n"]
        )
        return response
