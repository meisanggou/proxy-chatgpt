# !/usr/bin/env python
# coding: utf-8
import sys
from proxy_chatgpt.objects.user import UserObject

__author__ = 'zhouhenglc'

def main(*args):
    user = UserObject()
    if len(args >= 3):
        user_name = args[0]
        password = args[1]
        role = args[2]


if __name__ == '__main__':
    main(sys.argv[1:])
