from django.db import models


class LineaProducto(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=30, unique=True)

    class Meta:
        db_table = 'linea_productos'
        verbose_name = 'Línea de producto'
        verbose_name_plural = 'Líneas de producto'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
