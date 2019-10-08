import os
from registroAlumno import Alumno
from registroNota import Nota
from registroMatricula import Matricula


def matriculaAlumno():
    os.system("cls")
    print()
    print("\t\t******************************************")
    print("\t\t\tTabla total de registros")
    print("\t\t******************************************")
    matricula = Matricula("","","","","")
    matricula.mostrarMatricula()
    print()
    print("\t\t***************************************************")
    print("\t\t\t\tTabla total de Notas")
    print("\t\t***************************************************")
    nota = Nota("","","","","","")
    nota.mostrarNotaParaAlumno()
    print()
    print("\t***************************************************")
    print("\t\t\tDatos del Alumno")
    print("\t***************************************************")
    alumno = Alumno("","","")
    alumno.mostrarDatosAlumno()
    print()
    print("\t***************************************************")
    print("\t\t\tMatricula del Alumno")
    print("\t***************************************************")
    print()
    print("Ingrese el periodo Escolar")
    print()
    print("1.- 2019 - I")
    print("2.- 2019 - II") 
    print("3.- 2019 - III")
    print()
    while True:
        try:
            periEsco = input("Elija un periodo Escolar: ")
            if periEsco.isdigit():
                periEsco = int(periEsco)
                if periEsco == 1:
                    print("Periodo Esolar registrado")
                    periEsco = '2019 - I'
                    break
                if periEsco == 2:
                    print("Periodo Esolar registrado")
                    periEsco = '2019 - II'
                    break
                if periEsco == 3:
                    print("Periodo Esolar registrado")
                    periEsco = '2019 - III'
                    break
        except ValueError:
            os.system("cls")
            print(f"\nERROR!, '{periEsco}': No es una opcion corecta. Solo se permiten Digitos.\n")
            print("Selecciona Correctamente")
    print()
    print("Ingrese el salon: ")
    print()
    print("1.-  1ro A | 2.-  1ro B | 3.-  1ro C")
    print("4.-  2do A | 5.-  2do B | 6.-  2do C")
    print("7.-  3ro A | 8.-  3ro B | 9.-  3ro C")
    print("10.- 4to A | 11.- 4to B | 12.- 4to C")
    print("13.- 5to A | 14.- 5to B | 15.- 5to C")
    print("16.- 6to A | 17.- 6to B | 18.- 6to C")
    print()
    while True:
        try:
            salon = input("Elija un Salon Segun Edad: ")
            if salon.isdigit():
                salon = int(salon)
                if salon == 1: 
                    print("Salon: Grado Y Seccion - Registrado")
                    salon = '1ro A'
                    break
                if salon == 2: 
                    print("Salon: Grado Y Seccion - Registrado")
                    salon = '1ro B'
                    break
                if salon == 3: 
                    print("Salon: Grado Y Seccion - Registrado")
                    salon = '1ro A'
                    break
                if salon == 4: 
                    print("Salon: Grado Y Seccion - Registrado")
                    salon = '1ro A'
                    break
                if salon == 5: 
                    print("Salon: Grado Y Seccion - Registrado")
                    salon = '1ro A'
                    break
                if salon == 6: 
                    print("Salon: Grado Y Seccion - Registrado")
                    salon = '1ro A'
                    break
                if salon == 7: 
                    print("Salon: Grado Y Seccion - Registrado")
                    salon = '1ro A'
                    break
                if salon == 8: 
                    print("Salon: Grado Y Seccion - Registrado")
                    salon = '1ro A'
                    break
                if salon == 9: 
                    print("Salon: Grado Y Seccion - Registrado")
                    salon = '1ro A'
                    break
                if salon == 10: 
                    print("Salon: Grado Y Seccion - Registrado")
                    salon = '1ro A'
                    break
                if salon == 11: 
                    print("Salon: Grado Y Seccion - Registrado")
                    salon = '1ro A'
                    break
                if salon == 12: 
                    print("Salon: Grado Y Seccion - Registrado")
                    salon = '1ro A'
                    break
                if salon == 13: 
                    print("Salon: Grado Y Seccion - Registrado")
                    salon = '1ro A'
                    break
                if salon == 14: 
                    print("Salon: Grado Y Seccion - Registrado")
                    salon = '1ro A'
                    break
                if salon == 15: 
                    print("Salon: Grado Y Seccion - Registrado")
                    salon = '1ro A'
                    break
                if salon == 16: 
                    print("Salon: Grado Y Seccion - Registrado")
                    salon = '1ro A'
                    break
                if salon == 17: 
                    print("Salon: Grado Y Seccion - Registrado")
                    salon = '1ro A'
                    break
                if salon == 18: 
                    print("Salon: Grado Y Seccion - Registrado")
                    salon = '1ro A'
                    break
        except ValueError:
            os.system("cls")
            print(f"\nERROR!, '{salon}': No es una opcion corecta. Solo se permiten Digitos.\n")
            print("Selecciona Correctamente")
    print()
    print("Turno Del Estudiante: ")
    print("1.- Mañana")
    print("2.- Tarde")
    print()
    while True:
        try:
            turno = input("Elija un Turno: ")
            if turno.isdigit():
                turno = int(turno)
                if turno == 1: 
                    turno = 'Mañana'
                    print(f"Turno: {turno} - Registrado")
                    break
                if turno == 2: 
                    turno = 'Tarde'
                    print(f"Turno: {turno} - Registrado")
                    break
        except ValueError:
            os.system("cls")
            print(f"\nERROR!, '{turno}': No es una opcion corecta. Solo se permiten Digitos.\n")
            print("Selecciona Correctamente")
    print()
    print("Seleccionar ID del Alumno Que no Esta Registrado: ")
    alumno.mostrarDatosAlumno()
    print()
    print("Id Del Alumno No registrado: ")
    ide = int(input("Elija El ultimo ID: "))
    print()
    print("Alumno Agregado")
    print()
    print("Seleccionar un ID de la nota del Alumno que no esta Registrado")
    nota.mostrarNotaParaAlumno()
    print("Id de la nota No registrada: ")
    notas = int(input("Elija El ultimo ID: "))
    print()
    print("Nota Agregada")
    print()
    print("RESULTADO FINAL")
    print("Periodo Escolar: ",periEsco,"\nSalon: ",salon,"\nTurno: ",turno,"\nAlumno: ",ide,"\nNota: ",notas)
    print()
    print("Matricula registrada con Exito")
    matricula = Matricula(periEsco,salon,turno,ide,notas)
    matricula.agregarMatricula(matricula)