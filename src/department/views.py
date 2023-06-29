from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, response, status
from .serializers import DepartmentSerializer, DepartmentPersonalSerializer
from django.shortcuts import render, get_object_or_404
from src.personal.models import CustomUser
from . import models


class DeportmentViewset(ModelViewSet):
    serializer_class = DepartmentSerializer
    permission_classes = (permissions.AllowAny, )
    queryset = models.Department.objects.all()

    def destroy(self, request, pk, *args, **kwargs):
        personal = get_object_or_404(CustomUser, id=self.request.query_params.get('personal'))
        personal.department = None
        personal.save()
        return response.Response(status.HTTP_204_NO_CONTENT)


class DepartmentPersonalView(ModelViewSet):
    serializer_class = DepartmentPersonalSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Department.objects.all()

    def destroy(self, request, pk, *args, **kwargs):
        serializer = DepartmentPersonalSerializer(data=request.data)
        serializer.is_valid()
        if serializer.errors:
            return response.Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        for member in serializer.validated_data['personal']:
            member.department = None
            member.save()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

        # if serializer.is_valid():q
        #     print('ok')

