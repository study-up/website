from django.shortcuts import render
from django.views.generic.base import View
from mood.models import Mood


class MoodCrl(View):
    def index(self, request):
        moods = Mood.objects.all()
        return render(request, 'mood/index.html', {'moods': moods})
