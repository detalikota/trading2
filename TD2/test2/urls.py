from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='test_home'),
    path('about/', views.about, name='test_about')
]
