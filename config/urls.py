from django.contrib import admin
from django.urls import path, include
from .doc_urls import urlpatterns as docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/department/', include('src.department.urls')),
    path('api/v1/personal/', include('src.personal.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
]
urlpatterns += docs_urls



