from django.urls import path
from .views import (RegistrationAPIView, LoginAPIView,
                    ProfileView, ProfileEditView)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', ProfileView.as_view(), name='profile-view'),
    path('profile/edit/', ProfileEditView.as_view(), name='profile-edit'),

]
