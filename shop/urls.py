from django.urls import path
from .views import RegistrationAPIView, LoginAPIView, ProductCreateView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
]
