# Import all base settings
from .settings import *

# Override base settings for production

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Generate a new secret key for production
# You should generate a new one using:
# python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
SECRET_KEY = 't6#@07#tj+nvmin!t7qj0h-3=-ayyge&1(0r%k*!7v#23^9wf('  

# Configure allowed hosts
# Add your domain name(s) here
ALLOWED_HOSTS = ['1yearanni-DrPayne.pythonanywhere.com']

# Configure static files for production
STATIC_URL = '/static/'
STATIC_ROOT = '/home/drpayne/anniversary_site/staticfiles'

# Configure media files for production
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/drpayne/anniversary_site/media'

# Security settings
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'



# If you're using HTTPS (recommended):
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_HSTS_SECONDS = 31536000  # 1 year
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True

# Database - if you're using a different database in production
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'your_db_name',
#         'USER': 'your_db_user',
#         'PASSWORD': 'your_db_password',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }