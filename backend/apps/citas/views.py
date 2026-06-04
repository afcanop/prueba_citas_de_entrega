from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Cita
from .serializers import CitaSerializer


class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()

    serializer_class = CitaSerializer

    permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    filterset_fields = [
        'estado',
        'proveedor',
        'linea_producto',
        'linea_producto__slug',
    ]

    ordering_fields = [
        'fecha_programada',
        'creado_en',
    ]

    search_fields = [
        'proveedor__nombre',
        'linea_producto__nombre',
        'observaciones',
    ]

    def perform_create(self, serializer):
        serializer.save(
            creado_por=self.request.user
        )