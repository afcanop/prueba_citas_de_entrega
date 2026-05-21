from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_fecha_programada(fecha_programada):
    if fecha_programada < timezone.now():
        raise ValidationError(
            'La fecha programada no puede estar en el pasado.'
        )
