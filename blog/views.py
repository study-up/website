from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from .models import Note


class BlogCtl(View):
    def index(self, request):
        notes = Note.published.all()
        return render(request, 'blog/index.html', {'notes': notes})

    def note_detail(self, request, year, month, day, uid):
        print 'cc',year,month
        # note = Note.published.filter(publish__month=month)
        note = get_object_or_404(Note, id=uid, status='published', publish__year=year, publish__month=month,
                                 publish__day=day)
        return render(request, 'blog/detail.html', {'note': note})

