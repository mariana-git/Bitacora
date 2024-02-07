from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User

class bitacora(TimeStampedModel):
    tema = models.CharField(max_length=100)
    comentario = models.CharField(max_length=300)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tema}"

    class Meta:
        ordering = ['-created']
        verbose_name = 'bitacora'
        verbose_name_plural = 'bitacoras'
