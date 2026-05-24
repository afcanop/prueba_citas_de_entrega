from rest_framework import serializers

from ..models import Cita
from .validators import (
    validate_fecha_programada,
    validar_conflicto_horario,
    validar_fecha_entrega,
)


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
        return validate_fecha_programada(value)

    def validate(self, attrs):

        self.validar_fecha_entrega(attrs)
        self.validar_conflicto_horario(attrs)

        return attrs

    def validar_fecha_entrega(self, attrs):
        return validar_fecha_entrega(attrs)

    def validar_conflicto_horario(self, attrs):
        return validar_conflicto_horario(attrs)
