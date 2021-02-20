from django.shortcuts import render
from rest_framework import exceptions, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import UsersSerializer, PermissionSerializer, RoleSerializer
from .models import User, Permission, Role
from .authentication import access_tokens, JwtAuthenticatedUser


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

    response = Response()
    # je genere le json web tken
    token = access_tokens(user)
    #  je set le cookie
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }
    return response

# j ' obtiens l 'authenticated user


class AuthenticateUSer(APIView):
    authentication_classes = [JwtAuthenticatedUser]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UsersSerializer(request.user)
        return Response({
            'data': serializer.data
        })


@api_view(['post'])
def signout(reques):
    response = Response()
    response.delete_cookie(key='jwt')
    response.data = {
        "detail": "sucess"
    }
    return response


@api_view(['GET'])
def users(reques):
    serializer = UsersSerializer(User.objects.all(), many=True)
    return Response(serializer.data)

# Obtenir les permissions


class PermissionAPIView(APIView):
    authentication_classes = [JwtAuthenticatedUser]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = PermissionSerializer(Permission.objects.all(), many=True)
        return Response({
            "data": serializer.data
        })


# Definir un viewSet Pour gerer les Roles

class RoleViewSet(viewsets.ViewSet):
    authentication_classes = [JwtAuthenticatedUser]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = RoleSerializer(Role.objects.all(), many=True)
        return Response({
            "data": serializer.data
        })

    def retrieve(self, request, pk=None):
        pass

    def create(self, request):
        serializer = RoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "detail": serializer.data
        })

    def update(self, request, pk=None):
        pass

    def delete(self, request, pk=None):
        pass
