from rest_framework import serializers
from .models import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'password'
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }
