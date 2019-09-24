from rest_framework import serializers
from .models import customUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = customUser
        fields = ['email', 'first_name']
