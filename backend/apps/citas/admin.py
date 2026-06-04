from django.contrib import admin

from .models import Cita, LineaProducto


@admin.register(LineaProducto)
class LineaProductoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'slug',
    )
    search_fields = (
        'nombre',
        'slug',
    )
    prepopulated_fields = {
        'slug': ('nombre',),
    }


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