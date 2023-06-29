from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, response, status
from .serializers import DepartmentSerializer, DepartmentPersonalSerializer
from django.db.models import Sum, Count, Q
from . import models


class DeportmentViewset(ModelViewSet):
    serializer_class = DepartmentSerializer
    permission_classes = (permissions.AllowAny, )
    queryset = models.Department.objects.all()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        data = models.Department.objects.aggregate(salary_sum=Sum('personal__salary'), count_personal=Count('personal'))
        response.data.append(data)
        return response


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


