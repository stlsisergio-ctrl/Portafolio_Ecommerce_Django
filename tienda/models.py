from django.db import models
from django.core.validators import MinValueValidator

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0.01)] # Validación: precio > 0 
    )
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    imagen_url = models.URLField(blank=True, null=True) 

    def __str__(self):
        return self.nombre