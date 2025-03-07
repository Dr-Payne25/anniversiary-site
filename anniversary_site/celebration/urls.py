from django.urls import path
from . import views

app_name = 'celebration'

urlpatterns = [
    path('', views.index_redirect, name='index'),  # Redirect root to welcome
    path('home/', views.home, name='home'),  # Home moved to /home/
    path('welcome/', views.welcome, name='welcome'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
]