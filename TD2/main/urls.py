from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.home, name='td2-home'),
    path('about', views.about, name='td2-about'),
]