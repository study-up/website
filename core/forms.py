#!/usr/bin/env python
# encoding:utf-8
# @Author  :may
from django import forms


class BaseForm(forms.Form):
    def errors_to_string(self):
        json_msg = ':'.join(self.errors.as_text().split('\n'))
        return json_msg
