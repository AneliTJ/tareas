import random
class Medico:
    id_medico = 0
    nombre =""
    ano_nacimiento= 0
    direccion = ""
    rfc = ""
    def __init__(self, nombre, rfc, ano_nacimiento, direccion):
        self.id_medico = random.randint(1,10000)
        self.nombre =nombre 
        self.ano_nacimiento = ano_nacimiento
        self.rfc= rfc
        self.direccion = direccion
    def mostrar_informacion_medicos(self):
          print("Nombre: ",self.nombre,"Año de nacimiento: ",self.ano_nacimiento,"Direccion: ", self.direccion, "RFC: ", self.rfc,"ID:", self.id_medico)