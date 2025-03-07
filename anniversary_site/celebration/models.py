# celebration/models.py
from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')
    caption = models.TextField(blank=True)
    date_taken = models.DateField(blank=True, null=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order']

class MenuItem(models.Model):
    COURSE_CHOICES = [
        ('appetizer', 'Appetizer'),
        ('main', 'Main Course'),
        ('dessert', 'Dessert'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu/')
    course = models.CharField(max_length=10, choices=COURSE_CHOICES)
    background_story = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.get_course_display()}: {self.name}"
    
    class Meta:
        ordering = ['course']

class AboutUs(models.Model):
    your_name = models.CharField(max_length=100)
    your_bio = models.TextField()
    your_image = models.ImageField(upload_to='about/')
    
    partner_name = models.CharField(max_length=100)
    partner_bio = models.TextField()
    partner_image = models.ImageField(upload_to='about/')
    
    relationship_story = models.TextField()
    anniversary_date = models.DateField()
    
    def __str__(self):
        return f"About {self.your_name} & {self.partner_name}"