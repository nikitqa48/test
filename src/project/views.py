from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectSerializer, NestedProjectSerializer
from .models import Project


class ProjectModelViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return NestedProjectSerializer
        return ProjectSerializer
