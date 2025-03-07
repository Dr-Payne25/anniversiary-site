from django.shortcuts import render
from .models import Photo, MenuItem, AboutUs

def home(request):
    photos = Photo.objects.all()
    try:
        about = AboutUs.objects.first()
        anniversary_date = about.anniversary_date
    except AboutUs.DoesNotExist:
        anniversary_date = None
    
    return render(request, 'celebration/home.html', {
        'photos': photos,
        'anniversary_date': anniversary_date
    })

def menu(request):
    appetizers = MenuItem.objects.filter(course='appetizer')
    mains = MenuItem.objects.filter(course='main')
    desserts = MenuItem.objects.filter(course='dessert')
    
    return render(request, 'celebration/menu.html', {
        'appetizers': appetizers,
        'mains': mains,
        'desserts': desserts
    })

def about(request):
    try:
        about_us = AboutUs.objects.first()
    except AboutUs.DoesNotExist:
        about_us = None
    
    return render(request, 'celebration/about.html', {
        'about_us': about_us
    })