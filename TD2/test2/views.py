from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
    'p': 'My first post',
    'a': 'Magomed',
    'd': 'July',
    },
    {
    'p': 'My second post',
    'a': 'John',
    'd': 'April', 
    },
]

def func():
    for x in range(50):
        print (x)
    return x

def test(request):
    return render(request, "test2/home.html") # I can put the third argument here, called context to put some information into the templates

def about(request):
    
    context = {
        'posts': posts,
        }
    
    return render(request, "test2/about.html", context)