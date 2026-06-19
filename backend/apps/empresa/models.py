import uuid

from django.db import models
from django_tenants.models import DomainMixin, TenantMixin


class EstadoChoices(models.TextChoices):
    ACTIVO = 'activo', 'Activo'
    INACTIVO = 'inactivo', 'Inactivo'
    SUSPENDIDO = 'suspendido', 'Suspendido'


class PlanChoices(models.TextChoices):
    FREE = 'free', 'Free'
    BASICO = 'basico', 'Básico'
    PREMIUM = 'premium', 'Premium'
    ENTERPRISE = 'enterprise', 'Enterprise'


class Empresa(TenantMixin):
    schema_name = models.CharField(max_length=63, unique=True)
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    nombre = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    nit = models.CharField(max_length=50, unique=True)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    estado = models.CharField(
        max_length=20,
        choices=EstadoChoices.choices,
        default=EstadoChoices.ACTIVO
    )
    plan = models.CharField(
        max_length=20,
        choices=PlanChoices.choices,
        default=PlanChoices.FREE
    )
    timezone = models.CharField(max_length=50, default='America/Bogota')
    logo = models.URLField(blank=True, null=True)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    auto_create_schema = True

    class Meta:
        db_table = 'empresas'
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nombre


class Dominio(DomainMixin):
    class Meta:
        db_table = 'dominios'
        verbose_name = 'Dominio'
        verbose_name_plural = 'Dominios'

    def __str__(self):
        return self.domain
