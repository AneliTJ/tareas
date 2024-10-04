import random
class Consulta:
    id = 0
    fecha_hora=""
    consultorio = ""
    medico = ""
    paciente = ""
    def __init__(self,fecha_hora, consultorio, medico, paciente):
        self.id_consultas =random.randint(1, 10000)
        self.fecha_hora = fecha_hora 
        self.consultorio = consultorio 
        self.medico = medico
        self.paciente = paciente
    def mostrar_informacion_consultas(self):
          print("ID:", self.id_consultas, "fecha y hora: ",self.fecha_hora,"Consultorio: ",self.consultorio,"Paciente: ", self.paciente, "Medico: ", self.medico)