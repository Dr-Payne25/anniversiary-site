from django.contrib import admin
from .models import Photo, MenuItem, AboutUs

# Register the Photo model
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_taken', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'caption')

# Register the MenuItem model
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'course')
    list_filter = ('course',)
    search_fields = ('name', 'description')

# Register the AboutUs model
@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('your_name', 'partner_name', 'anniversary_date')