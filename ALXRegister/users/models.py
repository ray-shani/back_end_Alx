from django.db import models

class UserProfile(models.Model):
    STATUS_CHOICES = [
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('alumni', 'Alumni'),
        ('community', 'Community Member'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.status})"
