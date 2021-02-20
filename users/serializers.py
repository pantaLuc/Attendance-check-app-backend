from rest_framework import serializers
from .models import User, Role, Permission


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class PermissionRelatedField(serializers.StringRelatedField):
    def to_representation(self, value):
        return PermissionSerializer(value).data

    def to_internal_value(self, data):
        return data


class RoleRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return RoleSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)


class RoleSerializer(serializers.ModelSerializer):
    permissions = PermissionRelatedField(many=True)

    class Meta:
        model = Role
        fields = "__all__"

    def create(self, validated_data):
        permissions = validated_data.pop('permissions', None)
        # return a dictionnary
        instance = self.Meta.model(**validated_data)
        instance.save()
        # normal array
        instance.permissions.add(*permissions)
        instance.save()
        return instance


class UsersSerializer(serializers.ModelSerializer):
    role = RoleRelatedField(queryset=Role.objects.all(), many=False)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'password',
            'role'
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

    def update(self, validated_data):
        password = validated_data.pop('password', None)
        # retourner un dictionnaire
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
