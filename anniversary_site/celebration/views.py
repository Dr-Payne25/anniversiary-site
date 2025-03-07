from django.shortcuts import render
from .models import Photo, MenuItem, AboutUs

def home(request):
    photos = Photo.objects.all()
    
    about = AboutUs.objects.first()
    anniversary_date = about.anniversary_date if about else None
    
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
    about_us = AboutUs.objects.first()
    
    return render(request, 'celebration/about.html', {
        'about_us': about_us
    })