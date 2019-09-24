from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import customUser
from .serializers import CustomUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = customUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated,)