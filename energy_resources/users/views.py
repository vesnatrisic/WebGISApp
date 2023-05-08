from .serializer import RegisterSerializer, ChangePasswordSerializer, MyTokenObtainPairSerializer, UserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.utils import timezone


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserStatusView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        # Set the last_visit field to the current date and time
        self.request.user.last_visit = timezone.now()
        self.request.user.save()
        return self.request.user


class ChangePasswordView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user

