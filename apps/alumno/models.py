# import datetime

from django.db.models import Model, CharField, DateField, PositiveIntegerField

from apps.users.models import AuthSignature


class Persona(Model):

    CHOICES_SEXO = (
        ('masculino', 'Masculino'),
        ('femenino', 'Femeninno')
    )

    apellido = CharField(max_length=40)
    nombre = CharField(max_length=300)
    dni = CharField(max_length=8, unique=True)
    fecha_nacimiento = DateField(
        blank=True,
        null=True,
        # format=''
    )
    sexo = CharField(
        max_length=10,
        blank=True,
        choices=CHOICES_SEXO,
        default='',
        null=True,
    )

    class Meta:
        abstract = True


class Alumno(Persona, AuthSignature):
    legajo = PositiveIntegerField(unique=True, blank=False, null=False)

    class Meta(object):
        ordering = ('dni', 'apellido', 'nombre')

    def __str__(self):
        return '%s %s' % (self.apellido.upper(), self.nombre.upper())



class Docente(Persona, AuthSignature):

    class Meta(object):
        ordering = ('dni', 'apellido', 'nombre')

    def __str__(self):
        return '%s %s' % (self.apellido.upper(), self.nombre.upper())
