# celebration/models.py
from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=100)  # Stores the photo title, limited to 100 characters
    image = models.ImageField(upload_to='photos/')  # Stores the actual image file, saved in a 'photos' directory
    caption = models.TextField(blank=True)  # Optional text description for the photo
    date_taken = models.DateField(blank=True, null=True)  # Optional date when the photo was taken
    order = models.IntegerField(default=0)  # Controls the display order in the carousel
    
    def __str__(self):
        return self.title  # Shows the title when this object is referenced in the admin interface
    
    class Meta:
        ordering = ['order']  # Automatically sorts photos by the 'order' field when queried

class MenuItem(models.Model):
    # Defines the available course types as choices for the course field
    COURSE_CHOICES = [
        ('appetizer', 'Appetizer'),  # ('database_value', 'Human-readable label')
        ('main', 'Main Course'),
        ('dessert', 'Dessert'),
    ]
    
    name = models.CharField(max_length=100)  # Name of the dish
    description = models.TextField()  # Detailed description of the dish
    image = models.ImageField(upload_to='menu/')  # Photo of the dish, saved in a 'menu' directory
    course = models.CharField(max_length=10, choices=COURSE_CHOICES)  # Type of course (appetizer, main, dessert)
    background_story = models.TextField(blank=True)  # Optional story about why this dish is special
    
    def __str__(self):
        # Returns a string like "Main Course: Grilled Salmon" for admin interface
        return f"{self.get_course_display()}: {self.name}"
    
    class Meta:
        ordering = ['course']  # Automatically sorts menu items by course type when queried

class AboutUs(models.Model):
    your_name = models.CharField(max_length=100)  # Your name
    your_bio = models.TextField()  # Biographical information about you
    your_image = models.ImageField(upload_to='about/')  # Your photo, saved in an 'about' directory
    
    partner_name = models.CharField(max_length=100)  # Your girlfriend's name
    partner_bio = models.TextField()  # Biographical information about your girlfriend
    partner_image = models.ImageField(upload_to='about/')  # Your girlfriend's photo
    
    relationship_story = models.TextField()  # The story of your relationship
    anniversary_date = models.DateField()  # Your anniversary date for calculation and display
    
    def __str__(self):
        # Returns a string like "About John & Jane" for admin interface
        return f"About {self.your_name} & {self.partner_name}"