from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, response, status
from .serializers import DepartmentSerializer, DepartmentPersonalSerializer
from django.db.models import Sum, Count
from . import models


class DeportmentViewset(ModelViewSet):
    serializer_class = DepartmentSerializer
    permission_classes = (permissions.AllowAny, )
    queryset = models.Department.objects.all()

    def list(self, request, *args, **kwargs):
        res = super().list(request, *args, **kwargs)
        data = models.Department.objects.aggregate(salary_sum=Sum('personal__salary'), count_personal=Count('personal'))
        res.data.append(data)
        return res


class DepartmentPersonalView(ModelViewSet):
    serializer_class = DepartmentPersonalSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Department.objects.all()

    def destroy(self, request, pk, *args, **kwargs):
        serializer = DepartmentPersonalSerializer(data=request.data)

        def remove_department(user):
            user.department = None
            user.save()
        if serializer.is_valid():
            personal = serializer.validated_data['personal']
            map(remove_department, personal)
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        return response.Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)



