#!/usr/bin/env python
# encoding:utf-8
# @Author  :may

from django import template
from blog.models import Note
from django.db.models import Count
register = template.Library()


@register.simple_tag
def total_posts():
    return Note.published.count()


@register.inclusion_tag('blog/date_latest_notes.html')
def show_date_notes(count=5):
    latest_notes = Note.published.order_by('-publish')[:count]
    return {'latest_notes': latest_notes}


@register.assignment_tag
def get_most_commented_posts(count=10):
    return Note.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
