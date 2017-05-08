from django.shortcuts import render
from django.views.generic.base import View
from .models import Note


class BlogCtl(View):
    def index(self, request):
        notes = Note.published.all()
        return render(request, 'blog/index.html', {'notes': notes})
