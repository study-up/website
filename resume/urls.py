#!/usr/bin/env python
# encoding:utf-8
# @Author  :may


from django.conf.urls import url
from resume.views import ResumeCrl

resumecrl = ResumeCrl()

urlpatterns = [
        url('^$', resumecrl.index, name='resume_index'),
]
