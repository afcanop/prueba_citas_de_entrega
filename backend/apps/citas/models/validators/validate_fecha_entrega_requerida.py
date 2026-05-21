from django.core.exceptions import ValidationError

from ..choices import EstadoCita


def validate_fecha_entrega_requerida(estado, fecha_entrega):
    if estado == EstadoCita.ENTREGADA and not fecha_entrega:
        raise ValidationError(
            'Las citas entregadas requieren fecha_entrega.'
        )
