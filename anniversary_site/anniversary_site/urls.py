from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from celebration.views import site_entry

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', site_entry, name='entry'),  # This handles the root URL
    path('', include('celebration.urls')),  # This handles all other URLs from celebration app
]

# Add this to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)