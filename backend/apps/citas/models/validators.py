from django.core.exceptions import ValidationError
from django.utils import timezone

from .choices import EstadoCita


def validate_fecha_programada(fecha_programada):
    if fecha_programada < timezone.now():
        raise ValidationError(
            'La fecha programada no puede estar en el pasado.'
        )


def validate_fecha_entrega_requerida(estado, fecha_entrega):
    if estado == EstadoCita.ENTREGADA and not fecha_entrega:
        raise ValidationError(
            'Las citas entregadas requieren fecha_entrega.'
        )
