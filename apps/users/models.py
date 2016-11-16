from datetime import datetime                   # para poner valor por defecto en campo fecha

from django.db import models
from django.contrib.auth.models import User     # para poder usar el modelo user generado por django


# modelo abstracto que pretende agregar campos extra a un modelo real
class AuthSignature(models.Model):
    created_by = models.ForeignKey(User, related_name='created', on_delete=models.CASCADE)
    created_on = models.DateTimeField(
        # auto_now_add=True,
        blank=True,
        default=datetime.now
    )
    modified_by = models.ForeignKey(User, null=True, blank=True, related_name='modiefied', on_delete=models.CASCADE)
    modified_on = models.DateTimeField(
        # auto_now_add=True,
        blank=True,
        # default=datetime.now
        null=True,
    )

    class Meta:
        abstract = True
