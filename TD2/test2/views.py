from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
    'author': 'Magomed',
    'date_posted': 'December',
    'title': 'Post #1',
    'content': 'Content of post #1'
    },
    {
    'author': 'Ahmed',
    'date_posted': 'November',
    'title': 'Post #2',
    'content': 'Content of post #2'
    },
]

def func():
    for x in range(50):
        print (x)
    return x

def home(request):
    context = {
        'posts': posts,
        }
    return render(request, "test2/home.html", context) # I can put the third argument here, called context to put some information into the templates

def about(request):
       
    return render(request, "test2/about.html")