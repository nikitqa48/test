from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, status
from rest_framework.response import Response
from src.personal import models
from .serializers import CustomUserSerializer
from .pagination import StandardResultsSetPagination


class PersonalViewSet(ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = models.CustomUser.objects.all()
    pagination_class = StandardResultsSetPagination
    filterset_fields = ['department', 'last_name']
    permission_classes = [permissions.IsAuthenticated]


