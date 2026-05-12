from django.db import models
import uuid
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

#   Modelo para representar las citas de entrega de productos a los proveedores
class ProveedorChoices(models.TextChoices):
    A = 'A', 'Proveedor A'
    B = 'B', 'Proveedor B'
    C = 'C', 'Proveedor C'

#   Modelo para representar las líneas de productos que se entregarán a los proveedores
class LineaProductoChoices(models.TextChoices):
    CAMISETAS = 'camisetas', 'Camisetas'
    PANTALONES = 'pantalones', 'Pantalones'
    ZAPATOS = 'zapatos', 'Zapatos'
    ACCESORIOS = 'accesorios', 'Accesorios'

#   Modelo para representar el estado de las citas de entrega
class EstadoCita(models.TextChoices):
    PROGRAMADA = 'programada', 'Programada'
    EN_PROCESO = 'en_proceso', 'En proceso'
    ENTREGADA = 'entregada', 'Entregada'
    CANCELADA = 'cancelada', 'Cancelada'

#   Modelo principal para representar las citas de entrega de productos a los proveedores
class Cita(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    fecha_programada = models.DateTimeField()
    proveedor = models.CharField(
        max_length=1,
        choices=ProveedorChoices.choices
    )
    linea_producto = models.CharField(
        max_length=20,
        choices=LineaProductoChoices.choices
    )
    estado = models.CharField(
        max_length=20,
        choices=EstadoCita.choices,
        default=EstadoCita.PROGRAMADA
    )
    fecha_entrega = models.DateTimeField(
        null=True,
        blank=True
    )
    observaciones = models.TextField(
        null=True,
        blank=True
    )
    creado_por = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='citas'
    )
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

class Meta:
    #orderar por fecha_programada descendente para mostrar las citas más próximas primero
    ordering = ['-fecha_programada']
    #nombre de la tabla en la base de datos
    db_table = 'citas'
    #índices para mejorar el rendimiento de las consultas por estado, proveedor,
    # línea de producto y fecha programada
    indexes = [
        models.Index(fields=['estado']),
        models.Index(fields=['proveedor']),
        models.Index(fields=['linea_producto']),
        models.Index(fields=['fecha_programada']),
    ]

    #Validaciones personalizadas para asegurar que la fecha programada
    #no esté en el pasado y que las citas entregadas tengan una fecha de entrega
    def clean(self):
        if self.fecha_programada < timezone.now():
            raise ValidationError(
                'La fecha programada no puede estar en el pasado.'
            )

        if (
            self.estado == EstadoCita.ENTREGADA
            and not self.fecha_entrega
        ):
            raise ValidationError(
                'Las citas entregadas requieren fecha_entrega.'
            )

    def __str__(self):
        return (
            f'{self.linea_producto} - '
            f'{self.proveedor} - '
            f'{self.estado}'
        )