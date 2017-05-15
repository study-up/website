#!/usr/bin/env python
# encoding:utf-8
# @Author  :may

from django.conf.urls import url
from guestbook.views import MessageBoard

msgctl = MessageBoard()
urlpatterns = [
    url(r'^$', msgctl.index, name='msg_index'),
]
