# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_info, name='user-info'),
    path('create/', views.create_user, name='create-user'),
    path('list/', views.get_users, name='user-list'),
]
