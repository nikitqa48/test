from rest_framework import routers
from .views import PersonalViewSet

router = routers.DefaultRouter()

router.register('', PersonalViewSet, basename='personal')