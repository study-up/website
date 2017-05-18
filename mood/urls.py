#!/usr/bin/env python
# encoding:utf-8
# @Author  :may

from django.conf.urls import url
from mood.views import MoodCrl

moodcrl = MoodCrl()

urlpatterns = [
        url('^$', moodcrl.index, name='mood_index'),
]
