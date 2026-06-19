from django.contrib import admin

from .models import Cita


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'proveedor',
        'linea_producto',
        'estado',
        'fecha_programada',
    )
    list_filter = ('proveedor', 'linea_producto', 'estado')
    search_fields = ('proveedor__nombre', 'linea_producto__nombre')