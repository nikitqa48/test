from rest_framework import routers
from .views import ProjectModelViewSet

router = routers.DefaultRouter()

router.register('', ProjectModelViewSet, basename='project')