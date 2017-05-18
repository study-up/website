#!/usr/bin/env python
# encoding:utf-8
# @Author  :may

from django import forms
from guestbook.models import Blessing


class BlessingForm(forms.ModelForm):
    class Meta:
        model = Blessing
        fields = ('name', 'content')
