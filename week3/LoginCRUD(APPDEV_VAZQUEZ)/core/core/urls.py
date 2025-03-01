from django.contrib import admin  # Django admin module
from django.urls import path, include       # URL routing
from authentication.views import *  # Import views from the authentication app
from django.conf import settings   # Application settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # Static files serving

# Define URL patterns
urlpatterns = [
    path('home/', home, name="recipes"),      # Home page
    path("admin/", admin.site.urls),          # Admin interface
    path('login/', login_page, name='login_page'),    # Login page
    path('register/', register_page, name='register'), # Registration page
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')) 
]
