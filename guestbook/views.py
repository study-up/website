#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  :may

from django.shortcuts import render
from django.views.generic.base import View
from guestbook.models import Blessing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from guestbook.forms import BlessingForm
from django.contrib import messages


class MessageBoard(View):
    def index(self, request):
        if request.method == 'POST':
            form = BlessingForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, '提交成功')
            else:
                messages.add_message(request, messages.ERROR, form.errors.as_text())
        else:
            form = BlessingForm()
        msgs = Blessing.objects.all()
        msg_count = msgs.count()
        paginator = Paginator(msgs, 10)
        page = request.GET.get('page')
        try:
            msgs = paginator.page(page)
        except PageNotAnInteger:
            msgs = paginator.page(1)
        except EmptyPage:
            msgs = paginator.page(paginator.num_pages)
        return render(request, 'guestbook/msg_board.html', {'msgs': msgs, 'page': msgs, 'form': form,
                                                            'msg_count': msg_count})
