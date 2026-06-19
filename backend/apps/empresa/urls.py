from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DominioViewSet, EmpresaViewSet

router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'dominios', DominioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
