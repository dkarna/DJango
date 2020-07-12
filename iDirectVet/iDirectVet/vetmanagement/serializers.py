from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User, Group
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username','email','password')

    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        users_group = Group.objects.get(name='vetclient')
        users_group.user_set.add(user)
        return user

class VetClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = VetClient
        fields = '__all__'

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = VetPet
        fields = '__all__'
        #fields = ('petname','species','sex','dob')

class ClientOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VetClientOwner
        fields = '__all__'

