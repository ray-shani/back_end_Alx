# users/urls.py
from django.urls import path
from .views import UserProfileListCreateView, UserProfileRetrieveUpdateDeleteView

urlpatterns = [
    path('users/', UserProfileListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserProfileRetrieveUpdateDeleteView.as_view(), name='user-detail'),
]
