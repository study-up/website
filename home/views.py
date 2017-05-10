from django.shortcuts import render
from blog.models import Note


def index(request):
    notes = Note.published.all()
    return render(request, 'home/index.html', {'notes': notes})
