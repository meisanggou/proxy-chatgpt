# !/usr/bin/env python
# coding: utf-8
import sqlalchemy
from proxy_chatgpt.db.models import Base


__author__ = 'zhouhenglc'


class SysUserModel(Base):

    __tablename__ = 'sys_user'

    user_no = sqlalchemy.Column(sqlalchemy.INT(), primary_key=True,
                                autoincrement=True)
    user_name = sqlalchemy.Column(sqlalchemy.String(), unique=True)
    password = sqlalchemy.Column(sqlalchemy.String(), nullable=True)
    role = sqlalchemy.Column(sqlalchemy.INT())
    nick_name = sqlalchemy.Column(sqlalchemy.String())
    wx_id = sqlalchemy.Column(sqlalchemy.String())
    creator = sqlalchemy.Column(sqlalchemy.String())
    email = sqlalchemy.Column(sqlalchemy.String())
    tel = sqlalchemy.Column(sqlalchemy.String())
    avatar_url = sqlalchemy.Column(sqlalchemy.String())
    add_time = sqlalchemy.Column(sqlalchemy.INT())
