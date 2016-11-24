from rest_framework import viewsets

from .serializers import AlumnoSerializer

from ..models import Alumno


class AlumnoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Alumno.objects.all().order_by('apellido')
    serializer_class = AlumnoSerializer
