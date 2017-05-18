#!/usr/bin/env python
# encoding:utf-8
# @Author  :may

from django import forms
from blog.models import Note, Comment
from pagedown.widgets import AdminPagedownWidget


class NoteForm(forms.ModelForm):
    body = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Note
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
