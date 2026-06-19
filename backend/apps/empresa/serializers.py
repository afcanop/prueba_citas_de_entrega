from rest_framework import serializers

from .models import Dominio, Empresa


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        exclude = ['schema_name']


class EmpresaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = [
            'id', 'nombre', 'slug', 'nit', 'email',
            'estado', 'plan', 'fecha_vencimiento', 'created_at',
        ]


class DominioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dominio
        fields = '__all__'
