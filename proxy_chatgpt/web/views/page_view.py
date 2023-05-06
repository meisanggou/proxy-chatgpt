# !/usr/bin/env python
# coding: utf-8
from datetime import datetime
from flask import g
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from flask_helper.view import View
from flask_login import login_required
from proxy_chatgpt.web import login_manager


__author__ = 'zhouhenglc'

url_prefix = '/'
page_view = View('page', __name__, url_prefix=url_prefix)
login_manager.login_view = "page.page_login"


@page_view.route('/')
@login_required
def page_view_index():
    return render_template('chat.html', user_name=g.user_name)


@page_view.route('/login')
def page_login():
    return render_template('login.html')


@page_view.route('/vip')
@login_required
def page_view_vip_index():
    return render_template('chat.html', is_vip=True)


@page_view.route("/password", methods=["GET"])
def password_page():
    _prefix = '/user'
    if "user_name" in g:
        return render_template("password.html", url_prefix=_prefix)
    elif "change_token" in session and "expires_in" in session and "user_name" in session:
        expires_in = session["expires_in"]
        if expires_in > datetime.now():
            return render_template("password.html", user_name=session["user_name"],
                                   change_token=session["change_token"], url_prefix=url_prefix)
    return redirect(url_for(login_manager.login_view))


@page_view.route("/register", methods=["GET"])
@login_required
def register_page():
    # if g.user_role & control.role_value["user_new"] <= 0:
    #     return u"用户无权限操作"
    check_url = "/user/register/check"

    return render_template("register.html", url_prefix='/user',
                           check_url=check_url)
