from django.shortcuts import render, redirect
from .models import Producto
from .carrito import Carrito

def catalogo(request):
    # Pedimos todos los productos a la base de datos
    productos = Producto.objects.all()
    # Los enviamos al archivo HTML llamado 'catalogo.html'
    return render(request, 'tienda/catalogo.html', {'productos': productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect('catalogo') # Recarga la página tras agregar
def ver_carrito(request):
    # Simplemente renderizamos la página del carrito. 
    # Los datos ya están en la sesión y los sacaremos directamente en el HTML.
    return render(request, 'tienda/carrito.html')
def confirmar_compra(request):
    carrito = Carrito(request)
    carrito.limpiar() # Vaciamos el carrito
    # Aquí podríamos redirigir a una página de "Gracias", pero por ahora volveremos al catálogo
    return redirect('catalogo')