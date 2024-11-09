from producto import Producto
from typing import List

class Almacen:
    lista_productos : List[Producto]

    def calcular_costo(self):
        pass

    def mostrar_productos(self):
        for producto in self.lista_productos:
            print(producto.mostrar_info_producto())

# calcular_valor_total(): Calcula el valor total del inventario para ese producto, multiplicando la cantidad por el precio.
# mostrar_detalles(): Devuelve un string con los detalles del producto, como su nombre, precio, cantidad y valor total.