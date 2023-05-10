# !/usr/bin/env python
# coding: utf-8
import sys
from proxy_chatgpt.objects.user import UserObject

__author__ = 'zhouhenglc'


def main(*args):
    user = UserObject()
    if len(args > 3):
        user_name = args[0]
        password = args[1]
        role = args[2]
    elif len(args > 2):
        user_name = args[0]
        password = args[1]
        role = 1
    else:
        print('no do anything')
        return
    user.new_user(user_name, password, role=role)


if __name__ == '__main__':
    main(sys.argv[1:])
