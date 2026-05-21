from django.utils import timezone
from rest_framework import serializers


def validate_fecha_programada(value):
    if value < timezone.now():
        raise serializers.ValidationError(
            'La fecha programada no puede estar en el pasado.'
        )

    return value
