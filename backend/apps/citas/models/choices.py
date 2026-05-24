from django.db import models
class LineaProductoChoices(models.TextChoices):
    CAMISETAS = 'camisetas', 'Camisetas'
    PANTALONES = 'pantalones', 'Pantalones'
    ZAPATOS = 'zapatos', 'Zapatos'
    ACCESORIOS = 'accesorios', 'Accesorios'


class EstadoCita(models.TextChoices):
    PROGRAMADA = 'programada', 'Programada'
    EN_PROCESO = 'en_proceso', 'En proceso'
    ENTREGADA = 'entregada', 'Entregada'
    CANCELADA = 'cancelada', 'Cancelada'
