from django.shortcuts import render
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['post'])
def signup(request):
    data = request.data
    if data['password'] != data["password_confirm"]:
        raise exceptions.APIException("le mot de passe ne convient pas")
    serializer = UserSerializer(data = data)
    serializer.is_valid(raise_exception = True)
    serializer.save()
    return Response(serializer.data)

