#!/usr/bin/env python
# encoding:utf-8
# @Author  :may

from django.conf.urls import url
from home.views import index


urlpatterns = [
    url(r'^$', index, name='home'),
]
