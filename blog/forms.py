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

    def clean_title(self):
        try:
            note = Note.objects.get(title=self.cleaned_data.get('title'))
            if note:
                raise forms.ValidationError('博客名已存在')
        except Note.DoesNotExist:
            return self.cleaned_data.get('title')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
