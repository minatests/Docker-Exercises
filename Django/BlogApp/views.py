from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def my_home(request):
    all = Post.objects.all()
    return render(request, 'home.html', {'all':all})

# def my_authors(request):
#     all = Author.objects.all()
#     return render(request, 'authors.html', {'all':all})

# def oneauthor(request, id):
#     one_author = Author.objects.get(pk=id)
#     return render(request, 'oneauthor.html', {'one_author':one_author})

def my_posts(request):
    all = Post.objects.all()
    return render(request, 'posts.html', {'all':all})

def onepost(request, id):
    one_post = Post.objects.get(pk=id)
    all_comments = Comment.objects.filter(post = one_post.id)
    return render(request, 'onepost.html', {'one_post': one_post, 'all_comments': all_comments} )

def my_categories(request):
    all = Category.objects.all()
    return render(request, 'categories.html', {'all':all})

def onecategory(request, id):
    one_category = Category.objects.get(pk=id)
    return render(request, 'onecategory.html', {'one_category': one_category} )

def my_comments(request):
    all = Comment.objects.all()
    return render(request, 'comments.html', {'all':all})