from django.urls import path
from .views import dashboard, campaign_create, campaign_detail, campaign_list

app_name = 'business'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('create/', campaign_create, name='create'),
    path('detail/<id>/', campaign_detail, name='detail'),
    path('list/', campaign_list, name='list'),
    path('fulfill/', campaign_list, name='fulfill'),
]
