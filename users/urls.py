# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_info, name='user-info'),
    path('create/', views.create_user, name='create-user'),
    path('list/', views.get_users, name='user-list'),
    
    path('edit/<int:user_id>/', views.get_user, name='get_user'),
    path('users/<int:user_id>/update/', views.update_user, name='update_user'),
    path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),
]
