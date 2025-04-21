from django.urls import path
from .views import UserCreateAPIView, UserManageAPIView, CustomObtainAuthToken

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', CustomObtainAuthToken.as_view(), name='login'),
    path('me/', UserManageAPIView.as_view(), name='profile'),
]