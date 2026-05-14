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

        self.validar_fecha_entrega(attrs)
        self.validar_conflicto_horario(attrs)

        return attrs

    def validar_fecha_entrega(self, attrs):
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

    def validar_conflicto_horario(self, attrs):
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