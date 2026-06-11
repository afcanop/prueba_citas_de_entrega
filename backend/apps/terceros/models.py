import uuid

from django.db import models
from django_tenants.models import DomainMixin, TenantMixin


class TipoDocumentoChoices(models.TextChoices):
    CC = 'CC', 'Cédula'
    NIT = 'NIT', 'NIT'
    CE = 'CE', 'Cédula Extranjería'
    PAS = 'PAS', 'Pasaporte'

class TipoPersonaChoices(models.TextChoices):
    NATURAL = 'N', 'Natural'
    JURIDICA = 'J', 'Jurídica'

class Tercero(TenantMixin):
    schema_name = models.CharField(max_length=63, unique=True)
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
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
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    auto_create_schema = True

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'terceros'
        ordering = ['nombre']
        indexes = [
            models.Index(fields=['nombre']),
            models.Index(fields=['activo']),
            models.Index(fields=['cliente']),
            models.Index(fields=['proveedor']),
            models.Index(fields=['activo', 'cliente']),
            models.Index(fields=['activo', 'proveedor']),
        ]


class Dominio(DomainMixin):
    def __str__(self):
        return self.domain