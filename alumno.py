import os
from registroAlumno import Alumno
from registroNota import Nota
from registroMatricula import Matricula

def registroAlumnos():
    os.system("cls")
    print("Registrar Alumno:")
    print()
    print("Tabla de Alumnos Registrados")
    #DECLARO LAS CLASES QUE MOSTRARE
    mnota = Nota("","","","","","")
    mostrar = Alumno("","","")
    #MUESTRA LA TABLA DE ALUMNOS REGISTRADOS
    print("Registro de alumnos:\n")
    mostrar.listarAlumno()
    #MUESTRA LA TABLA DE LAS NOTAS DE LOS ALUMNOS REGISTRADOS
    print("\nNotas Del Alumno:\n")
    mnota.mostrarNotaParaAlumno()
    #FORMULARIO PARA REGISTRAR ALUMNOS Y SUS NOTAS
    #REGISTRAMOS ALUMNOS
    print()
    print("Ingresar datos del alumno para registrarlo: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    print()
    print("Seleccionar Curso para agregar Notas")
    print()
    print("1.- Lenguaje - Maritza Fernandez")
    print("2.- Matematica - julitza Martinez")
    print("3.- C.T.A - Jhordan Bustamande")
    print("4.- Programacion - Milagros Gonzales")
    print("5.- Algoritmos Geneticos - Isabel Fernandez")
    print()
    while True:
        try:
            op = input("Elige Un Curso, Solo digita el Numero del Curso: ")
            if op.isdigit():
                op = int(op)
                if op == 1:
                    print("Curso registrado")
                    op = 'Lenguaje - Maritza Fernandez'
                    break
                if op == 2:
                    print("Curso registrado")
                    op = 'Matematica - julitza Martinez'
                    break
                if op == 3:
                    print("Curso registrado")
                    op = 'C.T.A - Jhordan Bustamande'
                    break
                if op == 4:
                    print("Curso registrado")
                    op = 'Programacion - Milagros Gonzales'
                    break
                if op == 5:
                    print("Curso registrado")
                    op = 'Algoritmos Geneticos - Isabel Fernandez'
                    break
        except ValueError:
            os.system("cls")
            print(f"\nERROR!, '{op}': No es una opcion corecta. Solo se permiten Digitos.\n")
            print("Selecciona Correctamente")
    #REGISTRAMOS NOTAS
    print()
    print("Ingresar Notas")
    notas = []
    for n in range(1,5):
        nota = input(f"Nota Nro {n}: ")
        notas.append(nota)
    n1 = int(notas[0])
    n2 = int(notas[1])
    n3 = int(notas[2])
    n4 = int(notas[3])
    prom = (n1+n2+n3+n4)/4
    prome = prom
    print()
    print("Alumnos registrado","\n\nCurso: ",op," \nNombre: ",nombre,
          "\nApellido: ",apellido,"\nEdad: ",edad,"\n\nNotas:\n\nNota 1: ",n1,
          "\nNota 2: ",n2,"\nNota 3: ",n3,"\nNota 4: ",n4,"\nPromedio: ",prom)
    print()
    print("Registro del Alumno y Notas agregados correctamente.")
    #AGREGA A LOS ALUMNOS
    registro = Alumno(nombre, apellido, edad)
    registro.agregarAlumno(registro)
    print("Alumno Registrado...")
    #AGREGA AL PROFESOR Y A LOS ALUMNOS
    mnota = Nota(op,n1,n2,n3,n4,prome)
    mnota.agregarNota(mnota)