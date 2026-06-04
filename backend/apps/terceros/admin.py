from django.contrib import admin

# Register your models here.
from .models import Tercero
@admin.register(Tercero)
class TerceroAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'numero_documento',
        'tipo_documento',
        'tipo_persona',
        'proveedor',
        'cliente',
        'socio',
        'activo',
    )
    list_filter = ('proveedor', 'cliente', 'socio', 'activo')
    search_fields = ('nombre', 'numero_documento')