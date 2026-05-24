from django.db import models

# Create your models here.
from django.db import models


class TipoDocumentoChoices(models.TextChoices):
    CC = 'CC', 'Cédula'
    NIT = 'NIT', 'NIT'
    CE = 'CE', 'Cédula Extranjería'
    PAS = 'PAS', 'Pasaporte'

class TipoPersonaChoices(models.TextChoices):
    NATURAL = 'N', 'Natural'
    JURIDICA = 'J', 'Jurídica'

class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    proveedor = models.BooleanField(default=False)
    numero_documento = models.CharField(
        max_length=50,
        unique=True
    )
    tipo_documento = models.CharField(
        max_length=10,
        choices=TipoDocumentoChoices.choices
    )
    cliente = models.BooleanField(default=False)
    socio = models.BooleanField(default=False)
    tipo_persona = models.CharField(
        max_length=1,
        choices=TipoPersonaChoices.choices
    )
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'terceros'

        ordering = ['nombre']

        indexes = [

            # búsquedas por nombre
            models.Index(fields=['nombre']),

            # filtros por estado
            models.Index(fields=['activo']),

            # cliente/proveedor
            models.Index(fields=['cliente']),
            models.Index(fields=['proveedor']),

            # consultas combinadas
            models.Index(fields=['activo', 'cliente']),
            models.Index(fields=['activo', 'proveedor']),
        ]