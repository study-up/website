#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  :may

from django.db import models
from core.models import BaseModel
from django.utils import timezone
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Note(BaseModel):
    STATUS = (('draft', 'Draft'), ('published', 'Published'))
    title = models.CharField(max_length=200)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)  # 发布时间
    status = models.CharField(max_length=10, choices=STATUS, default='draft')  # 标记笔记状态，暂分为草稿和发布
    images = models.ImageField(upload_to='img', null=True)
    objects = models.Manager()  # 默认的查询集
    published = PublishedManager()  # 自定义的查询集
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.id])


class Comment(BaseModel):
    note = models.ForeignKey(Note, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.note)


