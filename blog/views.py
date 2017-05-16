#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  :may

from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from blog.models import Note
from blog.forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
import datetime
from taggit.models import Tag
from django.db.models import Count


class BlogCtl(View):
    def index(self, request, tag_slug=None):
        note_list = Note.published.all()
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            note_list = note_list.filter(tags__in=[tag])
        paginator = Paginator(note_list, 3)
        page = request.GET.get('page')
        try:
            notes = paginator.page(page)
        except PageNotAnInteger:
            notes = paginator.page(1)
        except EmptyPage:
            notes = paginator.page(paginator.num_pages)
        return render(request, 'blog/index.html', {'notes': notes, 'page': notes})

    def note_detail(self, request, year, month, day, uid):
        note = get_object_or_404(Note, id=uid, status='published',
                                 publish__startswith=datetime.date(int(year), int(month), int(day)))
        comments = note.comments.filter(active=True)
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.note = note
                new_comment.save()
                messages.add_message(request, messages.SUCCESS, '添加成功')
            else:
                messages.add_message(request, messages.ERROR, comment_form.errors.as_text())
        else:
            comment_form = CommentForm()
        note_tags_id = note.tags.values_list('id', flat=True)
        similar_note = Note.published.filter(tags__in=note_tags_id).exclude(id=uid)
        similar_posts = similar_note.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')
        return render(request, 'blog/detail.html', {'note': note, 'comments': comments, 'comment_form': comment_form,
                                                    'similar_posts': similar_posts})

