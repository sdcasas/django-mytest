from django.db import models

from apps.users.models import AuthSignature


class Persona(models.Model):
    apellido = models.CharField(max_length=40, blank=True)
    nombre = models.CharField(max_length=300)
    dni = models.CharField(max_length=8, unique=True)

    class Meta:
        abstract = True


class Alumno(Persona, AuthSignature):
    pass

    class Meta(object):
        ordering = ('dni', 'apellido', 'nombre')

    def __str__(self):
        return '%s %s' % (self.apellido.upper(), self.nombre.upper())


class Docente(Persona, AuthSignature):
    pass

    class Meta(object):
        ordering = ('dni', 'apellido', 'nombre')

    def __str__(self):
        return '%s %s' % (self.apellido.upper(), self.nombre.upper())
