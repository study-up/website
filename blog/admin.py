#!/usr/bin/env python
# encoding:utf-8

from django.contrib import admin
from .models import Note


admin.site.register(Note)
