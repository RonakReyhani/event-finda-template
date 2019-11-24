from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Event
from users.models import CustomUser
from .serializers import EventSerializer
from .serializers import CustomUserSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated,)


def get_queryset(self):
    user = self.request.user
    return CustomUser.objects.filter(pk=user.id)
