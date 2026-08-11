from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from core import views

urlpatterns = [
    path("api/register", views.RegisterView.as_view(), name="register"),
    path("api/login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/retseptlar", views.RetseptListCreateAPIView.as_view(), name="retseptlar"),
    path(
        "api/retseptlar/<int:pk>",
        views.RetseptRetrieveUpdateDestroyAPIView.as_view(),
        name="retsept",
    ),
]