from django.shortcuts import render
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UsersSerializer
from .models import User


@api_view(['post'])
def signup(request):
    data = request.data
    if data['password'] != data["password_confirm"]:
        raise exceptions.APIException("le mot de passe ne convient pas")
    serializer = UsersSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


# Methode signin
@api_view(['post'])
def signin(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed("user is not found ")
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed("incorret password")
    return Response("sucess")


@api_view(['GET'])
def users(reques):
    serializer = UsersSerializer(User.objects.all(), many=True)
    return Response(serializer.data)
