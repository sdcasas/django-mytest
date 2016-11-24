from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User     # para poder usar el modelo user generado por django


# modelo abstracto que pretende agregar campos extra a un modelo real
class AuthSignature(models.Model):
    created_by = models.ForeignKey(
        User,
        related_name='%(class)s_created',
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    created_on = models.DateTimeField(
        # auto_now_add=True,
        blank=True,
        default=timezone.now()
    )
    modified_by = models.ForeignKey(
        User,
        null=True, blank=True,
        related_name='%(class)s_modiefied',
        on_delete=models.CASCADE,
    )
    modified_on = models.DateTimeField(
        # auto_now_add=True,
        blank=True,
        default=timezone.now,
        null=True,
    )

    class Meta:
        abstract = True
