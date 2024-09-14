from curso import Curso

class Estudiante:

     def __init__(self, id_estudiante, nombre, edad, curso):
            self.id_estudiante= id_estudiante
            self.nombre = nombre 
            self.edad = edad 
            self.cursos = []

     def agregar_curso(self,curso):
          self.cursos.append(curso)


     def mostrar_info_estudiante(self):
          print("Nombre: ",self.nombre,"Edad: ",self.edad, "ID:", self.id_estudiante)

          if self.cursos:
                for curso in self.cursos:
                      curso.mostrar_info_curso()

          else:
                print("No hay cursos agregados")


