class Curso:

    def __init__(self, nombre_curso, id_curso, instructor):
        self.nombre_curso = nombre_curso
        self.id_curso= id_curso
        self.instructor= instructor

    def mostrar_info_curso(self):
        print("Nombre de la materia: ", self.nombre_curso, "ID de la materia: ", self.id_curso, "Nombre del profesor: ", self.instructor)
        return self.mostrar_info_curso

