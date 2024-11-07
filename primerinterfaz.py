import tkinter as tk
from tkinter import messagebox
 
def sumar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        suma = num1 + num2
        messagebox.showinfo("Resultado", f"La suma es: {suma}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def restar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resta = num1 - num2
        messagebox.showinfo("Resultado", f"La resta es: {resta}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def multiplicar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        mult = num1 * num2
        messagebox.showinfo("Resultado", f"El producto es: {mult}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def dividir():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        div = num1 / num2
        messagebox.showinfo("Resultado", f"La division es: {div}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
 
 
ventana = tk.Tk()
ventana.title("Calculadora de Suma")
ventana.geometry("300x200")
 
label_num1 = tk.Label(ventana, text="Número 1:", bg="pink", fg="black", font=("Arial", 12),padx=10, pady=15, relief="sunken")
label_num1.grid(row=0, column=0)
entry_num1 = tk.Entry(ventana, font=("Arial", 12), bd=2, relief="sunken")
entry_num1.grid(row=1, column=0)
 
label_num2 = tk.Label(ventana, text="Número 2:", bg="pink", fg="black", font=("Arial", 12),padx=10, pady=15,relief="sunken")
label_num2.grid(row=0, column=3)
entry_num2 = tk.Entry(ventana, font=("Arial", 12), bd=2, relief="sunken")
entry_num2.grid(row=1, column=3)

label_num3 = tk.Label(ventana, text="",padx=60, pady=10)
label_num3.grid(row=0, column=1)
label_num6= tk.Label(ventana, text="",padx=60, pady=10)
label_num6.grid(row=1, column=2)

boton_sumar = tk.Button(ventana, text="Sumar", command=sumar, bg="lightblue", fg="black")
boton_sumar.grid(row=2, column=0)

boton_restar = tk.Button(ventana, text="Restar", command=restar, bg="lightblue", fg="black")
boton_restar.grid(row=2, column=1)

boton_multiplicar = tk.Button(ventana, text="Multiplicar", command=multiplicar, bg="lightblue", fg="black")
boton_multiplicar.grid(row=2, column=2)

boton_division = tk.Button(ventana, text="Dividir", command=dividir, bg="lightblue", fg="black")
boton_division.grid(row=2, column=3)

ventana.mainloop()


