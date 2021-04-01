from django.urls import path, include
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('users', views.user_action, name='users'),
    path('update/<pk>', views.user_action, name='update_user'),
    path('add', views.user_action, name='add_user'),
    path('login', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name='refresh_token'),
    path('<pk>', views.user_action, name='user'),
    path('delete/<pk>', views.user_action, name='delete_user')
]
