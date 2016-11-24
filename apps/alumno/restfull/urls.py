from django.conf.urls import url, include
from rest_framework import routers

from .views import AlumnoViewSet

router = routers.DefaultRouter()
router.register(r'alumno', AlumnoViewSet)

urlpatterns = [
    url(r'^', include(router.urls), name='alumno'),
]
