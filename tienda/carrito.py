class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            # Si no hay carrito en la sesión, creamos un diccionario vacío
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

    def agregar(self, producto):
        producto_id = str(producto.id)
        if producto_id not in self.carrito.keys():
            self.carrito[producto_id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
            }
        else:
            self.carrito[producto_id]["cantidad"] += 1
        self.guardar()

    def guardar(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True