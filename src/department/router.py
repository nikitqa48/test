from rest_framework import routers
from .views import DeportmentViewset, DepartmentPersonalView


router = routers.DefaultRouter()
router.register('personal', DepartmentPersonalView, basename='personal')
router.register('', DeportmentViewset, basename='department')

