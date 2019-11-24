from .serializers import CustomUserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from eventFinderApp.models import Event
from .models import CustomUser
from .serializers import CustomUserSerializer, EventSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('email')
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return CustomUser.objects.filter(pk=user.id)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
