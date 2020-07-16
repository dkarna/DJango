from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, viewsets
from django.contrib.auth.models import User, Group
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import PetSerializer, UserSerializer, ProfileSerializer
from django.contrib.auth import authenticate

class ProfileViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        #queryset=Profile.objects.filter(user=user)
        queryset = Profile.objects.all()
        return queryset
    serializer_class = ProfileSerializer

class PetViewSet(viewsets.ModelViewSet):
    #def get(self,request):
    def get_queryset(self):
        user=self.request.user
        queryset = Pet.objects.filter(petuser=user)
        return queryset
    serializer_class = PetSerializer

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({'token': user.auth_token.key})
        else:
            return Response({'error': 'Wrong credentials'}, status=status.HTTP_400_BAD_REQUEST)