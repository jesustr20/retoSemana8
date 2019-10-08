import os
import alumno
import matricula

def menuPrincipal():
    os.system("cls")
    print("\t\t\t\t//////////////////////////////////////////////////////////////////")
    print("\t\t\t\t****************** Bienvenidos a la Institucion ******************")
    print("\t\t\t\t//////////////////////////////////////////////////////////////////")
    print()
    while True:
        print("Seleccione una opcion:")
        print("1.- Registrar Alumno.")
        print("2.- Ver Matricula.")
        print("Horario de Cursos - No disponible (Estamos Trabajando)")
        print("3.- Salir")
        opcion = input("Elegir una opcion: ")
        if opcion.isdigit():
            opcion = int(opcion)
            try:
                if opcion == 1:
                    os.system("CLS")
                    print("Acceso al Registro de Alumnos")
                    menuAlumnos()
                    break
                if opcion == 2:
                    os.system("CLS")
                    print("Acceso a Matricula")
                    menuMatricula()
                    break
                if opcion == 3:
                    os.system("cls")
                    print("Te has desconectado...")
                    exit()
                    break
                if opcion != 3:
                    os.system("cls")
                    print(f"ERROR!: {opcion}: Numero no aceptado.")
            except ValueError:
                print("Error, Solo numeros.")
        else:
            os.system("cls")
            print(f"\nERROR!, '{opcion}': No es una opcion corecta. Solo se permiten Digitos.\n")
            print("\t\t\t\t//////////////////////////////////////////////////////////////////")
            print("\t\t\t\t****************** Bienvenidos a la Institucion ******************")
            print("\t\t\t\t//////////////////////////////////////////////////////////////////")


def menuAlumnos():
    os.system("cls")
    print("\t\t\t\t////////////////////////////////////////////////////////////////////////")
    print("\t\t\t\t****************** Bienvenidos al Registro de Alumnos ******************")
    print("\t\t\t\t////////////////////////////////////////////////////////////////////////")
    print()
    while True:
        print("Seleccione una opcion:")
        print("1.- Registrar Alumno.")
        print("2.- Volver al Menu Inicial.")
        print("3.- Salir")
        opcion = input("Elegir una opcion: ")
        if opcion.isdigit():
            opcion = int(opcion)
            try:
                if opcion == 1:
                    alumno.registroAlumnos()
                if opcion == 2:
                    menuPrincipal()
                    break
                if opcion == 3:
                    os.system("cls")
                    print("Te has desconectado...")
                    exit()
                    break
                if opcion != 3:
                    os.system("cls")
                    print(f"ERROR!: {opcion}: Numero no aceptado.")
            except ValueError:
                print("Error, Solo numeros.")
        else:
            os.system("cls")
            print(f"\nERROR!, '{opcion}': No es una opcion corecta. Solo se permiten Digitos.\n")
            print("\t\t\t\t////////////////////////////////////////////////////////////////////////")
            print("\t\t\t\t****************** Bienvenidos al Registro de Alumnos ******************")
            print("\t\t\t\t////////////////////////////////////////////////////////////////////////")


def menuMatricula():
    os.system("cls")
    print("\t\t\t\t///////////////////////////////////////////////////////////////////")
    print("\t\t\t\t****************** Bienvenidos al Menu Matricula ******************")
    print("\t\t\t\t///////////////////////////////////////////////////////////////////")
    print()
    while True:
        print("Seleccione una opcion:")
        print("1.- Ver el Reporte de Matriculas")
        print("2.- Volver al Menu Inicial.")
        print("3.- Salir")
        opcion = input("Elegir una opcion: ")
        if opcion.isdigit():
            opcion = int(opcion)
            try:
                if opcion == 1:
                    matricula.matriculaAlumno()
                    break
                if opcion == 2:
                    menuPrincipal()
                    break
                if opcion == 3:
                    os.system("cls")
                    print("Te has desconectado...")
                    exit()
                    break
                if opcion != 3:
                    os.system("cls")
                    print(f"ERROR!: {opcion}: Numero no aceptado.")
            except ValueError:
                print("Error, Solo numeros.")
        else:
            os.system("cls")
            print(f"\nERROR!, '{opcion}': No es una opcion corecta. Solo se permiten Digitos.\n")
            print("\t\t\t\t///////////////////////////////////////////////////////////////////")
            print("\t\t\t\t****************** Bienvenidos al Menu Matricula ******************")
            print("\t\t\t\t///////////////////////////////////////////////////////////////////")