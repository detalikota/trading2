from django.shortcuts import render


# Create your views here.
posts = [
    {
        'author': 'Magomed',
        'title': 'Post #1',
        'content': 'My content of the post #1',
        'date_posted': 'November 30, 2020'
    },
    {
        'author': 'Gamzat',
        'title': 'Post #2',
        'content': 'My content of the post #2',
        'date_posted': 'December 1, 2020'
    },
    {
        'author': 'Ruslan',
        'title': 'Post #3',
        'content': 'My content of the post #2',
        'date_posted': 'December 1, 2020'
    }
]

def home(request):
    
    return render(request, 'main/home.html')

def about(request):
    context = {
        'cat': posts
    }
    return render(request, 'main/about.html', context)