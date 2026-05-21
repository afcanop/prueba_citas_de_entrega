from rest_framework import serializers

from ...models import EstadoCita


def validar_fecha_entrega(attrs):
    estado = attrs.get('estado')
    fecha_entrega = attrs.get('fecha_entrega')

    if estado == EstadoCita.ENTREGADA and not fecha_entrega:
        raise serializers.ValidationError(
            {
                'fecha_entrega': (
                    'Las citas entregadas requieren fecha_entrega.'
                )
            }
        )

    return attrs
