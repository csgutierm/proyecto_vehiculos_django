# Generated by Django 4.0.5 on 2024-11-19 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'permissions': [('visualizar_catalogo', 'Puede visualizar el catálogo')], 'verbose_name': 'Vehículo', 'verbose_name_plural': 'Vehículos'},
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='categoria',
            field=models.CharField(choices=[('Particular', 'Particular'), ('Transporte', 'Transporte'), ('Carga', 'Carga')], default='Particular', max_length=20, verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='marca',
            field=models.CharField(choices=[('Fiat', 'Fiat'), ('Chevrolet', 'Chevrolet'), ('Ford', 'Ford'), ('Toyota', 'Toyota')], default='Ford', max_length=20, verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='modelo',
            field=models.CharField(max_length=100, verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='serial_carroceria',
            field=models.CharField(max_length=50, verbose_name='Serial carrocería'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='serial_motor',
            field=models.CharField(max_length=50, verbose_name='Serial motor'),
        ),
    ]