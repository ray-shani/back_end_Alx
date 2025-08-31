from django.contrib import admin
from django.urls import path, include
from django.http import api_root


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('', api_root),  
]
