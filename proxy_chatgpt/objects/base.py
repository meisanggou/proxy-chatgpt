#! /usr/bin/env python
# coding: utf-8

from mysqldb_rich.db2 import DB
import time
import uuid

from proxy_chatgpt.utils.database_config import MysqlConfig
from proxy_chatgpt.utils.singleton import Singleton


class UnsetValue(Singleton):

    @classmethod
    def get_instance(cls):
        return cls()

    @classmethod
    def is_unset(cls, value):
        return value == cls.get_instance()

    @classmethod
    def not_unset(cls, value):
        return not cls.is_unset(value)


class DBObject(object):
    db_config = MysqlConfig()
    table_file = None

    def __init__(self):
        self.db = DB(conf_path=self.db_config.config_path)


class BaseObject(object):
    model = None
    uuid_col = None

    @property
    def now_time(self):
        return time.time()

    def query(self, session, **kwargs):
        query = session.query(self.model)
        if kwargs:
            query = query.filter_by(**kwargs)
        return query

    def create(self, session, **kwargs):
        if hasattr(self.model, 'update_time'):
            kwargs['update_time'] = self.now_time
        if hasattr(self.model, 'add_time'):
            kwargs['add_time'] = self.now_time
        if self.uuid_col:
            kwargs[self.uuid_col] = str(uuid.uuid4())
        print(kwargs)
        obj = self.model(**kwargs)
        obj.save(session)
        return obj

    def get_all(self, session, **kwargs):
        return session.query(self.model).filter_by(**kwargs).all()

    def update(self, session, where_value, **kwargs):
        # kwargs['internal'] = 1 if kwargs['internal'] else 0
        if hasattr(self.model, 'update_time'):
            kwargs['update_time'] = self.now_time
        return session.query(self.model).filter_by(**where_value).update(
            kwargs)

    def delete(self, session, **kwargs):
        return session.query(self.model).filter_by(**kwargs).delete()
