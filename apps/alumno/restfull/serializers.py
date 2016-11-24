from rest_framework import serializers

from ..models import Alumno


class AlumnoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alumno
        fields = (
            'legajo',
            'dni',
            'apellido',
            'nombre',
            'fecha_nacimiento',
            'sexo',
        )
