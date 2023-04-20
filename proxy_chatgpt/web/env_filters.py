# !/usr/bin/env python
# coding: utf-8


__author__ = 'zhouhenglc'


def make_static_url(filename, static_prefix_url='/static'):
    return static_prefix_url + "/" + filename


def make_default_static_url(filename):
    return "/static/" + filename


def make_static_html(filename, static_prefix_url='/static'):
    if filename.startswith("http"):
        src = filename
        default_src = filename
    else:
        src = make_static_url(filename, static_prefix_url)
        default_src = make_default_static_url(filename)
    if filename.endswith(".js"):
        html_s = "<script type=\"text/javascript\" src=\"%s\" onerror=\"this.src='%s'\"></script>" % (src, default_src)
    else:
        html_s = "<link rel=\"stylesheet\" href=\"%s\" onerror=\"this.href='%s'\">" % (src, default_src)
    return html_s
