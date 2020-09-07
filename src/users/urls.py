from django.urls import path
from .views import profile_create

app_name = 'user'

urlpatterns = [
    path('profile_create/', profile_create, name='profile_create'),
]