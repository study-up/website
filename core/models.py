#!/usr/bin/env python
# encoding:utf-8
#@Author  :may

import uuid
from django.db import models


class BaseModel(models.Model):
    '''
    基本model
    '''
    id = models.UUIDField(unique=True, default=uuid.uuid4, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def _uuid(self, datetime_str):
        return uuid.uuid3(uuid.uuid4(), datetime_str)

    class Meta:
        abstract = True
        ordering = ('created',)

    @classmethod
    def create(cls, **kwargs):
        obj = cls()
        for key in cls._meta.get_all_field_names():
            get_val = kwargs.get(key)
            if get_val:
                setattr(obj, key, get_val)
        return obj

    def update(self, **kwargs):
        for key in self._meta.get_all_field_names():
            if key not in ("id", "created"):
                get_val = kwargs.get(key)
                if get_val:
                    setattr(self, key, get_val)
        return self
