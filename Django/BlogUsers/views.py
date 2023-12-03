from django.shortcuts import render
from .models import *
# Create your views here.

def my_authors(request):
    all = Author.objects.all()
    return render(request, 'authors.html', {'all':all})

def oneauthor(request, id):
    one_author = Author.objects.get(pk=id)
    post_count = one_author.post_set.count()
    comment_count = one_author.comment_set.count()
    return render(request, 'oneauthor.html', {'one_author':one_author, 'post_count': post_count, 'comment_count': comment_count})