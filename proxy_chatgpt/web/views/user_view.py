# !/usr/bin/env python
# coding: utf-8
from flask import g
from flask import redirect
from flask import request
from flask import session
from flask import url_for
import time
from werkzeug.security import gen_salt

from flask_helper.view import View
from flask_login import current_user
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
    elif r_code == 0 and info.get('is_default_password'):
        # password is default password
        session["user_name"] = info["user_name"]
        session["change_token"] = gen_salt(57)
        session["expires_in"] = time.time() + 300
        session['password'] = password
        return {"status": True, "data": {"location": "/password",
                                         "user_name": info["user_name"]}}
    session["role"] = info["role"]
    session['user_no'] = info['user_no']

    user = User()
    user.user_name = info["user_name"]
    user.user_no = info["user_no"]
    login_user(user, remember=False)
    if "next" in request_data and request_data["next"] != "":
        return {"status": True, "data": {"location": request_data["next"], "user_name": user.user_name}}
    if session["role"] == 0:
        return {"status": False, "data": "您还没有任何权限，请联系管理员授权"}
    else:
        return {"status": True, "data": {"location": "/", "user_name": user.user_name}}


@user_view.route("/password", methods=["POST"])
def set_password():
    user_name = request.form["user_name"]
    new_password= request.form["new_password"]
    confirm_password = request.form["confirm_password"]
    if new_password != confirm_password:
        return "两次输入密码不一致"
    if not user_m.password_is_strong(new_password):
        return '密码强度不符合要求！'
    if current_user.is_authenticated:
        old_password= request.form["old_password"]
        if old_password == new_password:
            return u"新密码不能和旧密码一样"
        result = user_m.change_password(user_name, old_password, new_password)
        if result is False:
            return "旧密码不正确"
        return redirect(url_for("page.page_login"))
    elif "change_token" in session and "expires_in" in session \
            and "user_name" in session and "password" in session:
        expires_in = session["expires_in"]
        if expires_in > time.time():
            change_token = request.form["change_token"]
            if change_token != session["change_token"]:
                return "Bad change_token"
            if user_name != session["user_name"]:
                return "Bad user_name"
            result = user_m.change_password(user_name, session["password"], new_password)
            if result is False:
                return "旧密码不正确"
            del session["user_name"]
            del session["change_token"]
            del session["expires_in"]
            del session["password"]
            return redirect(url_for("page.page_login"))
        else:
            return "更新密码超时，请重新登录"
    return "更新失败，请重新登录"


@user_view.route("/register", methods=["POST"])
def register():
    if not user_m.is_manager(g.user_role):
        return '无权限操作'
    request_data = request.form
    user_name = request_data['user_name']
    if len(user_name) < 5:
        return "账户名长度过短"
    nick_name = request_data['nick_name']
    user_role = request_data.get('user_role', None)
    result, message = user_m.new_user(user_name, "dms", nick_name,
                                      current_user.user_name, user_role)
    if result is False:
        return message
    return redirect(url_for("page.page_view_index"))


@user_view.route("/register/check", methods=["POST"])
def register_check():
    request_data = request.json
    check_name = request_data["check_name"]
    is_exist = user_m.user_exist(check_name)
    return {"status": True, "data": {"result": is_exist, "message": ""}}
