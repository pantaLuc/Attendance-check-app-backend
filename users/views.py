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
