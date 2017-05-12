#!/usr/bin/env python
# encoding:utf-8
# @Author  :may

from django import forms
from blog.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
