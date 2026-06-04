from django.db import migrations, models
import django.db.models.deletion


def create_linea_producto_data(apps, schema_editor):
    Cita = apps.get_model('citas', 'Cita')
    LineaProducto = apps.get_model('citas', 'LineaProducto')

    valores = set(
        Cita.objects.order_by().values_list('linea_producto', flat=True)
    )

    for valor in valores:
        if not valor:
            continue
        LineaProducto.objects.create(
            slug=valor,
            nombre=valor.replace('_', ' ').capitalize(),
        )

    for cita in Cita.objects.all():
        if not cita.linea_producto:
            continue
        producto = LineaProducto.objects.get(slug=cita.linea_producto)
        cita.linea_producto_obj = producto
        cita.save(update_fields=['linea_producto_obj'])


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineaProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'linea_productos',
                'verbose_name': 'Línea de producto',
                'verbose_name_plural': 'Líneas de producto',
                'ordering': ['nombre'],
            },
        ),
        migrations.AddField(
            model_name='cita',
            name='linea_producto_obj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='citas', to='citas.lineaproducto'),
        ),
        migrations.RunPython(create_linea_producto_data, reverse_code=migrations.RunPython.noop),
        migrations.RemoveField(
            model_name='cita',
            name='linea_producto',
        ),
        migrations.RenameField(
            model_name='cita',
            old_name='linea_producto_obj',
            new_name='linea_producto',
        ),
    ]
