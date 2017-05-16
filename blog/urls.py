#!/usr/bin/env python
# encoding:utf-8
# @Author  :may

from django.conf.urls import url
from views import BlogCtl

blog = BlogCtl()

urlpatterns = [
    url(r'^$', blog.index, name='note_list'),
    url(r'^tag/(?P<tag_slug>[-\w]+)$', blog.index, name='note_list_by_tag'),
    url(r'^detail/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<uid>[-\w]+)/$', blog.note_detail,
        name='note_detail'),
]
