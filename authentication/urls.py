from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name="Login API"),
    path('get_refresh_token', TokenRefreshView.as_view(), name="Refresh Token API")
]
