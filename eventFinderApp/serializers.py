
from rest_framework import serializers
from .models import Event


from rest_framework import serializers
from .models import Event
from users.models import CustomUser


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('__all__')


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']
