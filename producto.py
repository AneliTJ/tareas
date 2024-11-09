

class Producto:
    nombre: str
    precio: float
    cantidad: int = 0

    def mostrar_info_producto(self):
        print(f"El nombre del producto {self.nombre}")
        print(f"El precio del producto {self.precio}")
        print(f"El cantidad del producto {self.cantidad}")

        
# nombre: El nombre del producto (de tipo str).
# precio: El precio del producto (de tipo float).
# cantidad: La cantidad disponible en inventario (de tipo int).
