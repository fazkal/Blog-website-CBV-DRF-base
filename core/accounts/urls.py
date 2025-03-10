from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = "accounts"

urlpatterns = [
   
    # Registration (create) user:
    path(
        "registration/",
        views.RegistrationApiView.as_view(),
        name="registration",
    ),

    # Activation and verification user
    path(
        "activation/confirm/<str:token>",
        views.ActivationApiView.as_view(),
        name="activation",
    ),

    # login jwt, get username and password give access and refresh token:
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt-create"),

    # get refresh token and give new access token:
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),

    # logout jwt:
    path('jwt/logout', views.LogoutView.as_view(),name='jwt-logout'),


]