class MiError(Exception):
    def __init__(self,mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def escribir_nombre(nombre):
    if (nombre == ""):
        raise MiError("El nombre es invalido, pues viene vacio")
    else: 
        print(nombre)

def precio_invalido(precio):
    if (precio <= 0):
        raise MiError("El precio es invalido, ingresa un numero mayor que 0")
    else:
        print({precio})

def cantidad_invalido(cantidad):
    if (cantidad < 0):
        raise MiError("La cantidad es invalida, ingresa un numero mayor que 0")
    else:
        print({cantidad})

