import uuid

from django.contrib.auth.models import User
from django.db import models

from .choices import EstadoCita
 
from .validators import validate_fecha_entrega_requerida, validate_fecha_programada
from apps.terceros.models import Tercero

class Cita(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    fecha_programada = models.DateTimeField()
    proveedor = models.ForeignKey(
        Tercero,
        on_delete=models.PROTECT,
        related_name='citas'
    )
    linea_producto = models.ForeignKey(
        'linea_producto.LineaProducto',
        on_delete=models.PROTECT,
        related_name='citas',
        null=True,
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

    def clean(self):
        validate_fecha_programada(self.fecha_programada)
        validate_fecha_entrega_requerida(
            self.estado,
            self.fecha_entrega,
        )

    def __str__(self):
        return (
            f'{self.linea_producto} - '
            f'{self.proveedor} - '
            f'{self.estado}'
        )

    class Meta:
        ordering = ['-fecha_programada']
        db_table = 'citas'
        indexes = [
            models.Index(fields=['estado']),
            models.Index(fields=['proveedor']),
            models.Index(fields=['linea_producto']),
            models.Index(fields=['fecha_programada']),
        ]
