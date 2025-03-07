from django.urls import path
from . import views

app_name = 'celebration'

urlpatterns = [
    path('', views.welcome, name='welcome'),  # Welcome is now the default
    path('home/', views.home, name='home'),   # Home is now at /home/
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
]