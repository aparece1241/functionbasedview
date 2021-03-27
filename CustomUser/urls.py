from django.urls import path
from . import views

urlpatterns = [
    path('users', views.get_all_user, name='users'),
    path('add', views.add_user, name='add_user'),
]
