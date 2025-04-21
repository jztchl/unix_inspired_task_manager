from rest_framework import generics, permissions
from user.models import User
from user.serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed
import logging
logger = logging.getLogger(__name__)
class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserManageAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self): 
        return self.request.user
    
    def destroy(self, request, *args, **kwargs):
        logger.warning(f"User {request.user.username} attempted to delete their account.")
        raise MethodNotAllowed("DELETE", detail="User deletion is forbidden.")

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = token.user
        logger.info(f"User {user.username} logged in successfully.")
        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username,
            'email': user.email
        })