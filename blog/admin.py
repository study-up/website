#!/usr/bin/env python
# encoding:utf-8

from django.contrib import admin
from .models import Note, Comment


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'status')
admin.site.register(Note, NoteAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'note', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
admin.site.register(Comment, CommentAdmin)
