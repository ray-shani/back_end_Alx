from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to ALX Hub Access API. Go to /api/users/ to manage users.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('', home),  # Root URL
]
