#!/usr/bin/env python
# encoding:utf-8
# @Author  :may

from django.conf.urls import url
from views import BlogCtl

blog = BlogCtl()

urlpatterns = [
    url(r'^$', blog.index, name='note_list'),
]
