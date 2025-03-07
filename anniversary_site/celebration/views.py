from django.shortcuts import render, redirect
from .models import Photo, MenuItem, AboutUs

def site_entry(request):
    """Force redirect to welcome page on first visit"""
    if not request.session.get('visited', False):
        request.session['visited'] = True
        return redirect('celebration:welcome')
    else:
        return redirect('celebration:home')

def welcome(request):
    """Render the welcome/envelope page"""
    return render(request, 'celebration/welcome.html')

def home(request):
    """Render the home page with photos and anniversary date"""
    photos = Photo.objects.all()
    
    about = AboutUs.objects.first()
    anniversary_date = about.anniversary_date if about else None
    
    return render(request, 'celebration/home.html', {
        'photos': photos,
        'anniversary_date': anniversary_date
    })

def menu(request):
    """Render the menu page with menu items"""
    appetizers = MenuItem.objects.filter(course='appetizer')
    mains = MenuItem.objects.filter(course='main')
    desserts = MenuItem.objects.filter(course='dessert')
    
    return render(request, 'celebration/menu.html', {
        'appetizers': appetizers,
        'mains': mains,
        'desserts': desserts
    })

def about(request):
    """Render the about page with information about the couple"""
    about_us = AboutUs.objects.first()
    
    return render(request, 'celebration/about.html', {
        'about_us': about_us
    })