# Create your views here.
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView


class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)  # Allow anyone to access the login view
   