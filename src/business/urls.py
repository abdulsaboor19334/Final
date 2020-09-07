from django.urls import path
from .views import dashboard, campaign_create, campaign_detail

app_name = 'business'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('create/', campaign_create, name='create'),
    path('detail/', campaign_detail, name='detail'),
]