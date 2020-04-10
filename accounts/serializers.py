from rest_framework import serializers
from accounts.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(read_only=True, source="get_full_name")

    class Meta:
        model = CustomUser

        fields = ("id", "username", "full_name", "email")
