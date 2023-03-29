# !/usr/bin/env python
# coding: utf-8
import sys

from proxy_chatgpt.web import get_app

__author__ = 'zhouhenglc'


app = get_app()


if __name__ == '__main__':
    port = 2405
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    app.run(host="0.0.0.0", port=port,)
