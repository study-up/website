from django.shortcuts import render
from django.views.generic.base import View
from guestbook.models import Blessing


class MessageBoard(View):
    def index(self, request):
        messages = Blessing.objects.all()
        return render(request, 'guestbook/msg_board.html', {'messages': messages})
