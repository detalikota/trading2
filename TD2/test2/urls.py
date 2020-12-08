from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('about/', views.about, name='test_about')
]
