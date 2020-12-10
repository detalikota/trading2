from django.shortcuts import render
from django.http import HttpResponse
from .models import Post2


def home(request):
    context = {
        'posts': Post2.objects.all()
        }
    return render(request, "test2/home.html", context) # I can put the third argument here, called context to put some information into the templates

def about(request):
       
    return render(request, "test2/about.html")