from curso import Curso
from estudiante import Estudiante

curso_uno =Curso("Procesos de fabricacion", 323, "Javier")
curso_dos = Curso ("Calculo Integral", 285, "Aburto")
curso_tres= Curso("Estatica", 398, "Ponciano")
curso_cuatro =("Programacion basica", 287, "Roque")

estudiante_uno = Estudiante(1,"Ari", 20,"Estatica" )
estudiante_dos = Estudiante(2, "Sol", 20, "Procesos de fabricación")

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
    print("1.Agregar materias")
    print("2.Mostrar datos")
    print("3.Salir")
    opcion = input("Ingresa la opción que deseas: ")
    id_estudiante = input("introduce el numero de control")
    id_elegido =buscar_id(id_estudiante)

    if opcion == 1:
        if id_elegido:
            nombre_curso = input("Introduce la materia que deseas agregar: ")
            instructor = input("Introduce el profesor del Curso: ")
            id_curso = int(input("Introduce el ID del curso: "))
            nuevo_curso = Curso(nombre_curso, id_curso, instructor)
            id_elegido.agregar_curso(nuevo_curso)
        else:
            print("Intenta otro ID, ya que el introducido no es correcto o no existe")


    elif opcion == 2:
        if id_elegido:
            id_elegido.mostrar_inf_estudiante()

    elif opcion == 3:
        print("Hasta la proxima")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        break

    else:
        print("Creo que te equivocaste, vuelve a intentarlo")


        
        

