from django.urls import path
from .views import (
    RegisterView,
    CustomTokenObtainPairView,
    ProfileUpdateView,
    ChangePasswordView,
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/", ProfileUpdateView.as_view(), name="profile_update"),
    path("change-password/", ChangePasswordView.as_view(), name="change_password"),
]
