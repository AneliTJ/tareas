from producto import Producto
from typing import List
from tkinter import messagebox

class Tienda:
    lista_productos : List[Producto] = []

    def mostrar_productos(self):
        info= ""
        costo_total= 0
        for producto in self.lista_productos:
            info += producto.mostrar_info_producto()
            costo_total += producto.calcular_costo_total()
        
        messagebox.showinfo("Informacion: ", f"{info}\n Valor total: {costo_total}")

    def registrar_producto(self, producto:Producto):
        self.lista_productos.append(producto)
