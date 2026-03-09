from django.db import models  # ¡Esta es la línea que falta!
from django.core.validators import MinValueValidator

class Producto(models.Model):
    # Definimos las 3 temáticas para tu tienda multidimensional
    TEMATICAS = [
        ('AUTOMATA', 'Archivo del Autómata'),
        ('LAB', 'Laboratorio Dimensional'),
        ('NUBES', 'Ciudad en las Nubes'),
    ]
    
    nombre = models.CharField(max_length=200)
    tematica = models.CharField(
        max_length=10, 
        choices=TEMATICAS, 
        default='NUBES'
    )
    descripcion = models.TextField()
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0.01)]
    )
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    imagen_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre