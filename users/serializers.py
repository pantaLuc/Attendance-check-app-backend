from rest_framework import serializers
from .models import User, Role, Permission


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        field = "__all__"


class RoleSerializer(serializers.ModelSerializer):
    permission = PermissionSerializer(many=True)

    class Meta:
        model = Role
        fields = "__all__"


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
    # Methode pour

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # retourner un dictionnaire
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
