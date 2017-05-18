from django.shortcuts import render
from django.views.generic.base import View


class ResumeCrl(View):
    def index(self, request):
        return render(request, 'resume/index.html')
