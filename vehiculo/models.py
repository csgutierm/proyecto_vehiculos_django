from django.db import models

class Vehiculo(models.Model):
    MARCAS = [
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    ]

    CATEGORIAS = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    ]

    marca = models.CharField(verbose_name='Marca', max_length=20, choices=MARCAS, default='Ford')
    modelo = models.CharField(verbose_name='Modelo', max_length=100)
    serial_carroceria = models.CharField(verbose_name='Serial carrocería', max_length=50)
    serial_motor = models.CharField(verbose_name='Serial motor', max_length=50)
    categoria = models.CharField(verbose_name='Categoría', max_length=20, choices=CATEGORIAS, default='Particular')
    precio = models.DecimalField(verbose_name='Precio', max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    fecha_modificacion = models.DateTimeField(verbose_name='Fecha de modificación', auto_now=True)
    
    class Meta:
        verbose_name = 'Vehículo'
        verbose_name_plural = 'Vehículos'

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.categoria})"
