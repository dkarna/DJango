from rest_framework import serializers, exceptions
from .models import *
from django.contrib.auth.models import User, Group
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

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

class ProfileSerializer(serializers.Serializer):
    class Meta:
        model = Profile
        fields = ('id', 'firstname', 'midname', 'lastname','address')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username","")
        password = data.get("password","")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    msg = "User is not enabled."
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with the given credentials"
                raise exceptions.ValidationError(msg)
        else:
            msg='Must provide both username and password.'
            raise exceptions.ValidationError(msg)
        return data