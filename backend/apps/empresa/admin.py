from django.contrib import admin

from .models import Dominio, Empresa


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nombre', 'slug', 'nit', 'email',
        'estado', 'plan', 'fecha_vencimiento',
    )
    list_filter = ('estado', 'plan')
    search_fields = ('nombre', 'slug', 'nit', 'email')
    prepopulated_fields = {'slug': ('nombre',)}


@admin.register(Dominio)
class DominioAdmin(admin.ModelAdmin):
    list_display = ('id', 'domain', 'tenant', 'is_primary')
    list_filter = ('is_primary',)
    search_fields = ('domain',)
