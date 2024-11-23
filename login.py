import tkinter as tk
from tkinter import messagebox
import mysql.connector
 
def verificar_usuario():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
 
    try:
        conn = mysql.connector.connect(
            host='localhost',      
            user='root',          
            password='',  
            database='proyecto'    
            )
 
        cursor = conn.cursor()
 
        cursor.execute('''
            SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s
        ''', (usuario, contraseña))
 
        usuario = cursor.fetchone()

        if usuario:
            rol = usuario[5].lower()
            if rol== "administrador":
                messagebox.showinfo("Login exitoso", f"Bienvenido {usuario[1]}")
                abrir_admin_ventana()
            elif rol=="usuario":
                messagebox.showinfo("Login exitoso", f"Bienvenido {usuario[1]}")
                abrir_usuario_ventana()
        else:
            messagebox.showerror("Error", "Usuario o contraseña no encontrados.")
  
    except mysql.connector.Error as err:
        messagebox.showerror("Error de conexión", f"Error: {err}")
   
    finally:
        if conn.is_connected():
            conn.close()  



def abrir_admin_ventana():
    root.withdraw()
    
    ventana_admin = tk.Toplevel(root)
    ventana_admin.title("Administrador")
    
    def regresar_a_login():
        ventana_admin.destroy()  
        root.deiconify()  

    boton_regresar = tk.Button(ventana_admin, text="Salir", command=regresar_a_login)
    boton_regresar.pack(pady=20)

def abrir_usuario_ventana():
    root.withdraw()
    
    ventana_usuario = tk.Toplevel(root)
    ventana_usuario.title("Usuario")
    
    def regresar_a_login():
        ventana_usuario.destroy()  
        root.deiconify()  

    boton_regresar = tk.Button(ventana_usuario, text="Salir", command=regresar_a_login)
    boton_regresar.pack(pady=20)

root= tk.Tk()
root.title("Login")
root.geometry("300x200") 

label_usuario = tk.Label(root, text="Usuario:")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(root, width=30)
entry_usuario.pack(pady=5)
 
label_contraseña = tk.Label(root, text="Contraseña:")
label_contraseña.pack(pady=5)
entry_contraseña = tk.Entry(root, width=30, show="*")
entry_contraseña.pack(pady=5)

btn_login = tk.Button(root, text="Login", command=verificar_usuario)
btn_login.pack(pady=20)
 
root.mainloop()