import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from tienda.models import Producto

productos = [
    {"nombre": "Cápsula de Memoria", "precio": 1500, "desc": "Un dispositivo con estética Steins;Gate.", "stock": 10},
    {"nombre": "Espada de Autómata", "precio": 45000, "desc": "Réplica inspirada en diseños de NieR.", "stock": 5},
    {"nombre": "Kit de Topografía", "precio": 120000, "desc": "Herramientas de precisión para ingeniería.", "stock": 3},
    # Agrega aquí tantos como quieras...
]

for p in productos:
    Producto.objects.get_or_create(
        nombre=p['nombre'],
        precio=p['precio'],
        descripcion=p['desc'],
        stock=p['stock']
    )

print("¡Tienda poblada con éxito!")