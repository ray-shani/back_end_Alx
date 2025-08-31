from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status', 'check_in_time', 'check_out_time')
    list_filter = ('status',)
