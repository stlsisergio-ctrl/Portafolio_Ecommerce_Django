from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('confirmar/', views.confirmar_compra, name='confirmar'), # <-- Nueva ruta
]