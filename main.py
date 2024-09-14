from curso import Curso
from estudiante import Estudiante

curso_uno =Curso("Procesos de fabricacion", 323, "Javier")
curso_dos = Curso ("Calculo Integral", 285, "Aburto")
curso_tres = Curso ("Estatica", 295, "Ponciano")
curso_cuatro =Curso ("Programacion basica", 287, "Roque")

estudiante_uno = Estudiante(1,"Ari", 20,"Estatica" )
estudiante_dos = Estudiante(2, "Sol", 20, "Procesos de fabricación")

estudiante_uno.agregar_curso(curso_tres)
estudiante_dos.agregar_curso(curso_uno)

def buscar_id(id_estudiante):
    if estudiante_uno.id_estudiante == id_estudiante:
        return estudiante_uno
    elif estudiante_dos.id_estudiante == id_estudiante:
        return estudiante_dos
    else:
        return
    
while True:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Bienvenido ¿Quieres....")
    print("1.Mostrar datos")
    print("2.Agregar materias")
    print("3.Salir")
    opcion = int(input("Ingresa la opción que deseas: "))


    if opcion == 1:
        id_estudiante = int(input("introduce el numero de control"))
        id_elegido =buscar_id(id_estudiante)
        if id_elegido:
            id_elegido.mostrar_info_estudiante()

        else:
            print("Intenta otro ID, ya que el introducido no es correcto o no existe")


    elif opcion == 2:
        id_estudiante = int(input("introduce el numero de control: "))
        id_elegido =buscar_id(id_estudiante)
        if id_elegido:
            nombre_curso = input("Introduce la materia que deseas agregar: ")
            id_curso = int(input("Introduce el ID del curso: "))
            instructor = input("Introduce el profesor del Curso: ")
            nuevo_curso = Curso(nombre_curso, id_curso, instructor)
            id_elegido.agregar_curso(nuevo_curso)
        else:
            print("Intenta otro ID, ya que el introducido no es correcto o no existe")

    elif opcion == 3:
        print("Hasta la proxima")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        break

    else:
        print("Creo que te equivocaste, vuelve a intentarlo")
