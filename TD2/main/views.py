from django.shortcuts import render
from .models import Post

# Create your views here.
""" posts = [
    {
        'author': 'detalikota',
        'title': 'Post #1',
        'content': 'My content of the post #1',
        'date_posted': 'November 30, 2020'
    },
    {
        'author': 'test2',
        'title': 'Post #2',
        'content': 'My content of the post #2',
        'date_posted': 'December 1, 2020'
    },
    {
        'author': 'test1',
        'title': 'Post #3',
        'content': 'My content of the post #2',
        'date_posted': 'December 1, 2020'
    }
] """

def home(request):
    
    return render(request, 'main/home.html')

def about(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'main/about.html', context)