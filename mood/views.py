from django.shortcuts import render
from django.views.generic.base import View


class MoodCrl(View):
    def index(self, request):
        return render(request, 'mood/index.html')
