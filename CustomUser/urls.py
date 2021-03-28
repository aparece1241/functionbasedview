from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('users', views.get_all_user, name='users'),
    path('add', views.add_user, name='add_user'),
    path('login', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name='refresh_token')
]
