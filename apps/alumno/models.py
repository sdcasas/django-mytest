from django.db import models

from apps.users.models import AuthSignature


class Persona(models.Model):
    CHOICES_SEXO = (
        ('masculino', 'Masculino'),
        ('femenino', 'Femeninno')
    )

    apellido = models.CharField(max_length=40, blank=True)
    nombre = models.CharField(max_length=300)
    dni = models.CharField(max_length=8, unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=10, choices=CHOICES_SEXO, default=' ', null=True, blank=True)

    class Meta:
        abstract = True


class Alumno(Persona, AuthSignature):
    legajo = models.PositiveIntegerField(unique=True, blank=False, null=False)

    class Meta(object):
        ordering = ('dni', 'apellido', 'nombre')

    def __str__(self):
        return '%s %s' % (self.apellido.upper(), self.nombre.upper())


class Docente(Persona, AuthSignature):

    class Meta(object):
        ordering = ('dni', 'apellido', 'nombre')

    def __str__(self):
        return '%s %s' % (self.apellido.upper(), self.nombre.upper())
