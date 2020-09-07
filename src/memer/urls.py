from django.urls import path
from .views import task_list, detail, dashboard

app_name = 'memer'

urlpatterns = [
    path('task_list/', task_list, name='task_list'),
    path('detail/', detail, name='detail'),
    path('dashboard/', dashboard, name='dashboard'),
]