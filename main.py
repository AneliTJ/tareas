from paciente import Paciente
from hospital import Hospital
from medico import Medico
hospital = Hospital()

paciente_uno = Paciente("Juan", 76, 2004, 1.78, "Av. Madero")
paciente_dos = Paciente("Jonathan", 70, 2007, 1.90, "Av. Madero")
hospital.registrar_paciente(paciente=paciente_uno)
hospital.registrar_paciente(paciente=paciente_dos)

medico_uno = Medico("Alberto",1900, "hncbuiwasdbhjk","Av. Periodismo")
medico_dos = Medico("Roberto",2000, "hncbuiwasdcdnk","Av. Periodismo")

hospital.registrar_medico(medico=medico_uno)
hospital.registrar_medico(medico=medico_dos)



while True:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Bienvenido ¿Quieres....")
    print("1.Agregar medico")
    print("2.Agregar paciente")
    print("3.Mostrar paciente menor de edad")
    print("4.Mostrar paciente mayor de edad")
    print("5.Mostrar medicos")
    print("6.Mostrar pacientes")
    print("7.Eliminar medico")
    print("8.Eliminar paciente")
    print("9.Salir")

    opcion = int(input("Ingresa la opción que deseas: "))

#nombre, rfc, ano_nacimiento, direccion
    if opcion == 1:
        nombre = input("Introduce el nombre: ")
        rfc = input("Introduce el RFC: ")
        ano_nacimiento = int(input("Introduce el año de nacimiento: "))
        direccion = input("Introduce la direccion: ")
        nuevo_medico=Medico(nombre, rfc, ano_nacimiento, direccion)
        hospital.registrar_medico(nuevo_medico)
        print ("Medico agregado")


    elif opcion == 2:
        nombre = input("Introduce el nombre: ")
        peso = int(input("Introduce el peso: "))
        ano_nacimiento = int(input("Introduce el año de nacimiento: "))
        estatura= float(input("Introduce la estatura: "))
        direccion = input("Introduce la direccion: ")
        nuevo_paciente=Paciente(nombre, peso, ano_nacimiento, estatura, direccion)
        hospital.registrar_paciente(nuevo_paciente)
        nuevo_paciente.clasificar_pacientes_edad()
            

    elif opcion == 3:
        menores, _ = hospital.clasificar_pacientes()
        print("Pacientes menores de edad:")
        for paciente in menores:
            paciente.mostrar_informacion_pacientes()

    elif opcion == 4:
        _, mayores = hospital.clasificar_pacientes()
        print("Pacientes mayores de edad:")
        for paciente in mayores:
            paciente.mostrar_informacion_pacientes()

    elif opcion == 5:
        print("\nMedicos:")
        hospital.mostrar_medicos()

    elif opcion == 6:
        print("\nPacientes:")
        hospital.mostrar_pacientes()

    elif opcion == 7:
        id_medico = int(input("introduce el id del medico que desees eliminar: "))
        hospital.eliminar_medico(id_medico)

    elif opcion == 8:
        id_paciente = int(input("introduce el id del paciente que desees eliminar: "))
        hospital.eliminar_paciente(id_paciente)

    else:
        print("********************************Espero todo haya ido bien, vuelve pronto*************************************")
        break

    