class Producto:
    nombre: str
    precio: float
    cantidad: int = 0

    def __init__(self, nombre:str, precio: float, cantidad:int):
        self.nombre= nombre
        self.precio=precio
        self.cantidad=cantidad

    def mostrar_info_producto(self):
        costo = self.cantidad * self.precio
        info=(f"\nEl nombre del producto {self.nombre},\nEl precio del producto {self.precio},\nEl cantidad del producto {self.cantidad}, \nEl costo total de los productos es {costo}")
        return info

    def calcular_costo_total(self):
        costo = self.cantidad * self.precio
        return costo

    

# nombre: El nombre del producto (de tipo str).
# precio: El precio del producto (de tipo float).
# cantidad: La cantidad disponible en inventario (de tipo int).
