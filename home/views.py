from django.shortcuts import render
from blog.models import Note
from guestbook.models import Blessing


def index(request):
    notes = Note.published.all()[:9]
    blessings = Blessing.objects.all()[:12]
    return render(request, 'home/index.html', {'notes': notes, 'blessings': blessings})
