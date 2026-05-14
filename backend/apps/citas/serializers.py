from rest_framework import serializers

from .models import Cita, EstadoCita


class CitaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cita

        fields = [
            'id',
            'fecha_programada',
            'proveedor',
            'linea_producto',
            'estado',
            'fecha_entrega',
            'observaciones',
            'creado_por',
            'creado_en',
            'actualizado_en',
        ]

        read_only_fields = (
            'id',
            'creado_por',
            'creado_en',
            'actualizado_en',
        )

    def validate_fecha_programada(self, value):
        from django.utils import timezone

        if value < timezone.now():
            raise serializers.ValidationError(
                'La fecha programada no puede estar en el pasado.'
            )

        return value

    def validate(self, attrs):
        estado = attrs.get('estado')
        fecha_entrega = attrs.get('fecha_entrega')

        if (
            estado == EstadoCita.ENTREGADA
            and not fecha_entrega
        ):
            raise serializers.ValidationError(
                {
                    'fecha_entrega': (
                        'Las citas entregadas requieren fecha_entrega.'
                    )
                }
            )

        return attrs