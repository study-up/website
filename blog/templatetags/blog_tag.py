#!/usr/bin/env python
# encoding:utf-8
# @Author  :may

from django import template
from blog.models import Note
register = template.Library()


@register.simple_tag
def total_posts():
    return Note.published.count()
