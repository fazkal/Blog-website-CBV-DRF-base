from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = "accounts"

urlpatterns = [
   
    
    # login jwt, get username and password give access and refresh token:
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt-create"),

    # get refresh token and give new access token:
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),

    # logout jwt:
    path('jwt/logout', views.LogoutView.as_view(),name='jwt-logout'),


]