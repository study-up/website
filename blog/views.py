from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from .models import Note
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime


class BlogCtl(View):
    def index(self, request):
        note_list = Note.published.all()
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
        return render(request, 'blog/detail.html', {'note': note})

