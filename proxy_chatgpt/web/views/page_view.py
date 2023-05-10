# !/usr/bin/env python
# coding: utf-8
import time

from flask import g
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from flask_helper.view import View
from flask_login import current_user
from flask_login import login_required
from flask_login import logout_user
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
    if current_user.is_authenticated is True:
        logout_user()
    return render_template('login.html')


@page_view.route('/vip')
@login_required
def page_view_vip_index():
    return render_template('chat.html', is_vip=True)


@page_view.route("/password", methods=["GET"])
def password_page():
    _prefix = '/user'
    if "user_name" in g and g.user_name:
        return render_template("password.html", url_prefix=_prefix)
    elif "change_token" in session and "expires_in" in session and "user_name" in session:
        print(session["expires_in"])
        expires_in = session["expires_in"]
        if expires_in > time.time():
            return render_template("password.html", user_name=session["user_name"],
                                   change_token=session["change_token"], url_prefix=_prefix)
    return redirect(url_for(login_manager.login_view))


@page_view.route("/register", methods=["GET"])
@login_required
def register_page():
    check_url = "/user/register/check"

    return render_template("register.html", url_prefix='/user',
                           check_url=check_url)
