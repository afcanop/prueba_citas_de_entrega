from rest_framework import serializers

from ...models import Cita


def validar_conflicto_horario(attrs):
    proveedor = attrs.get('proveedor')
    fecha_programada = attrs.get('fecha_programada')

    existe_cita = Cita.objects.filter(
        proveedor=proveedor,
        fecha_programada=fecha_programada
    ).exists()

    if existe_cita:
        raise serializers.ValidationError(
            {
                'fecha_programada': (
                    'Ya existe una cita para este proveedor '
                    'en esa fecha.'
                )
            }
        )

    return attrs
