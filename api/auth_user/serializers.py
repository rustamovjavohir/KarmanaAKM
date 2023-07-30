from rest_framework import serializers

from apps.auth_user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'full_name',
            'email',
            'phone_number',
            'is_active',
            'is_staff',
            'is_superuser',
        )
