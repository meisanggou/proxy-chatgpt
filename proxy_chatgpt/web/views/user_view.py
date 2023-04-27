# !/usr/bin/env python
# coding: utf-8
from flask import request
from flask import session

from flask_helper.view import View
from flask_login import login_user

from proxy_chatgpt.objects.user import UserObject
from proxy_chatgpt.web import User

__author__ = 'zhouhenglc'


user_view = View('user', __name__, url_prefix='/user')
user_m = UserObject()


@user_view.route('/login', methods=['POST'])
def user_login():
    request_data = request.json
    user_name = request_data["user_name"]
    password = request_data["password"]
    r_code, info = user_m.user_confirm(password, user=user_name)
    if r_code == -3:
        return {"status": False, "data": "内部错误"}
    elif r_code == -2:
        return {"status": False, "data": "账号不存在"}
    elif r_code == -1:
        return {"status": False, "data": "密码不正确"}
    session["role"] = info["role"]

    user = User()
    user.user_name = info["user_name"]
    login_user(user, remember=False)
    if "next" in request_data and request_data["next"] != "":
        return {"status": True, "data": {"location": request_data["next"], "user_name": user.user_name}}
    if session["role"] == 0:
        return {"status": False, "data": "您还没有任何权限，请联系管理员授权"}
    else:
        return {"status": True, "data": {"location": "/", "user_name": user.user_name}}
