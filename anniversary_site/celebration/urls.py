from django.urls import path
from . import views

app_name = 'celebration'

urlpatterns = [
    path('home/', views.home, name='home'),  # Changed from empty to 'home/'
    path('welcome/', views.welcome, name='welcome'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
]