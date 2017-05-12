from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from blog.models import Note
from blog.forms import CommentForm
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
        comments = note.comments.filter(active=True)
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.note = note
                new_comment.save()
        else:
            comment_form = CommentForm()
        return render(request, 'blog/detail.html', {'note': note, 'comments': comments, 'comment_form': comment_form})

