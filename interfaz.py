import tkinter as tk
from tkinter import messagebox, ttk
from producto import Producto
from tienda import Tienda
from excepciones import MiError, escribir_nombre, cantidad_invalido, precio_invalido
tienda=Tienda()

def registrar_producto():
    try:
        nombre = str(entry_nombre.get())
        escribir_nombre(nombre)
        precio = float(entry_precio.get())
        precio_invalido(precio)
        cantidad = int(entry_cantidad.get())
        cantidad_invalido(cantidad)
        producto=Producto(nombre=nombre, precio=precio, cantidad=cantidad)
        tienda.registrar_producto(producto)
        messagebox.showinfo("Informacion: ", producto.mostrar_info_producto())
    
    except MiError as e:
        messagebox.showerror("Error ",{e})

def mostrar_producto():
    tienda.mostrar_productos()


ventana = tk.Tk()
ventana.title("Tienda")
notebook=ttk.Notebook(ventana)

pestaña1=tk.Frame(notebook)
pestaña2=tk.Frame(notebook)

notebook.add(pestaña1, text="Registrar")
notebook.add(pestaña2, text="Mostrar producto")

notebook.pack(fill="both", expand=True)

label_nombre = tk.Label(pestaña1, text="Nombre:", bg="lightblue", fg="black", font=("Arial", 12),padx=10, pady=15, relief="sunken")
label_nombre.grid(row=0, column=0)
entry_nombre = tk.Entry(pestaña1, font=("Arial", 12), bd=2, relief="sunken")
entry_nombre.grid(row=0, column=1)

label_precio = tk.Label(pestaña1, text="Precio:", bg="lightblue", fg="black", font=("Arial", 12),padx=10, pady=15, relief="sunken")
label_precio.grid(row=1, column=0)
entry_precio = tk.Entry(pestaña1, font=("Arial", 12), bd=2, relief="sunken")
entry_precio.grid(row=1, column=1)

label_cantidad = tk.Label(pestaña1, text="Cantidad:", bg="lightblue", fg="black", font=("Arial", 12),padx=10, pady=15, relief="sunken")
label_cantidad.grid(row=2, column=0)
entry_cantidad = tk.Entry(pestaña1, font=("Arial", 12), bd=2, relief="sunken")
entry_cantidad.grid(row=2, column=1)

label_nombre2=tk.Label(pestaña2, text="Productos", bg="lightblue", fg="black", font=("Arial", 12),padx=10, pady=15, relief="sunken")
label_nombre2.grid(row=0,column=2)

boton_registrar = tk.Button(pestaña1, text="Registrar", command=registrar_producto, bg="lightblue", fg="black")
boton_registrar.grid(row=3, column=1)

boton_mostrar = tk.Button(pestaña2, text="Mostrar producto", command=mostrar_producto, bg="lightblue", fg="black")
boton_mostrar.grid(row=3, column=2)


ventana.mainloop()