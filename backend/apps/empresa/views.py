from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Dominio, Empresa
from .serializers import DominioSerializer, EmpresaListSerializer, EmpresaSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'list':
            return EmpresaListSerializer
        return EmpresaSerializer


class DominioViewSet(viewsets.ModelViewSet):
    queryset = Dominio.objects.all()
    serializer_class = DominioSerializer
    permission_classes = [AllowAny]
