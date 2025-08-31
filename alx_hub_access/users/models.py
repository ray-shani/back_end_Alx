# users/models.py
from django.db import models

class UserProfile(models.Model):
    STATUS_CHOICES = [
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('alumni', 'Alumni'),
        ('community', 'Community Member'),
    ]
    
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    check_in_time = models.DateTimeField(auto_now_add=True)
    check_out_time = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.status})"
