# !/usr/bin/env python
# coding: utf-8
import sqlalchemy
from proxy_chatgpt.db.models import Base

__author__ = 'zhouhenglc'


class ChatFlowModel(Base):

    __tablename__ = 'chat_flows'

    flow_no = sqlalchemy.Column(sqlalchemy.INT(), primary_key=True)
    user_no = sqlalchemy.Column(sqlalchemy.INT(), primary_key=True)
    prompt_tokens = sqlalchemy.Column(sqlalchemy.INT())
    completion_tokens = sqlalchemy.Column(sqlalchemy.INT())
    ip = sqlalchemy.Column(sqlalchemy.String())
    tags = sqlalchemy.Column(sqlalchemy.INT(), default=1)
    update_time = sqlalchemy.Column(sqlalchemy.INT())
