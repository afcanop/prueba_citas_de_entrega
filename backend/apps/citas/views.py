from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Cita
from .serializers import CitaSerializer


class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()

    serializer_class = CitaSerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(
            creado_por=self.request.user
        )