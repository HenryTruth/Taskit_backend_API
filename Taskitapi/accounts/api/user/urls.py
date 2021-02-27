from django.contrib import admin
from django.urls import path, include

from .views import UserDetailAPIView, UserStatusAPIView

app_name = "user"

urlpatterns = [
    path('<username>/', UserDetailAPIView.as_view(), name='detail'),
    path('<username>/todos/', UserStatusAPIView.as_view(), name='todos-list'),
]