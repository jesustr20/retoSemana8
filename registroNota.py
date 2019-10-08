from conex import Conexion

class Nota():
    def __init__(self, cursoprofesor_id, nota1, nota2, nota3, nota4, promedio):
        self.cursoprofesor_id = cursoprofesor_id
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.promedio = promedio
    
    def agregarNota(self, note):
        try:
            conex = Conexion()
            query = f'''
                INSERT INTO nota(cursoprofesor_id, nota1, nota2, nota3, nota4, promedio)
                VALUES ('{note.cursoprofesor_id}','{note.nota1}', '{note.nota2}', '{note.nota3}', '{note.nota4}', '{note.nota5}')
            '''
            conex.ejecutar_sentencia(query)
            conex.commit()
        except Exception as e:
            raise
            print(e)
        finally:
            conex.cerrar_conexion()


    #def actualizarAlumno(self, id_alumn, alumn):
    #    try:
    #        conex = Conexion()
    #        query = f'''
    #            UPDATE alumno
    #            SET nombre = '{alumn.nombre}',
    #            apellido = '{alumn.apellido}',
    #            edad = '{alumn.edad}'
    #            WHERE id = {id_alumn}
    #        '''
    #        conex.ejecutar_sentencia(query)
    #        conex.commit()
    #    except Exception as e:
    #        raise
    #        print(e)
    #    finally:
    #        conex.cerrar_conexion()

    #def obtenerAlumno(self, id_alumn):
    #    try:
    #        conex = Conexion()
    #        query = f'''
    #            SELECT * FROM alumno WHERE id={id_alumn}
    #        '''
    #        cursors = conex.ejecutar_sentencia(query)
    #        fila = cursors.fetchone()  
    #        alumn = Alumno(fila[1], fila[2], fila[3])
    #        print("Nro\t|\tNombre\t\t|\tApellido\t|\tEdad")
    #        print("---------------------------------------------------------------------")
    #        print(str(fila[0]),"\t|\t",alumn.nombre,"\t|\t",alumn.apellido,"\t|\t",alumn.edad)
    #        return alumn
    #    except Exception as e:
    #        raise
    #        print(e)
    #    finally:
    #        conex.cerrar_conexion()


    #def eliminarAlumno(self, id_alumn):
    #    try:
    #        conex = Conexion()
    #        query = f'''
    #            DELETE FROM alumno WHERE id={id_alumn}
    #        '''
    #        cursor = conex.ejecutar_sentencia(query)
    #        conex.commit()
    #        return True
    #    except Exception as e:
    #        raise
    #        print(e)
    #    finally:
    #        conex.cerrar_conexion()
    
    def listarNota(self):
        listado_nota=[]
        try:
            conex = Conexion()
            query = f'''
                Select * FROM nota
            '''
            cursor = conex.ejecutar_sentencia(query)
            filas = cursor.fetchall()
            print("Nro\t|\tCursoProfesor\t|\tnota1\t|\tnota2\t|\tnota3\t|\tnota4\t|\tPromedio")
            for fila in filas:
                nota = """{}\t|\t{}\t\t|\t{}\t|\t{}\t|\t{}\t|\t{}t\t|\t{}""".format(str(fila[0]), fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
                print("---------------------------------------------------------------------------------------------------------------")
                listado_nota.append(nota)
                print(nota)
            return nota
        except Exception as e:
            raise
            print(e)
        finally:
            conex.cerrar_conexion()

    #Mostrar al costado del listado alumno
    def mostrarNotaParaAlumno(self):
        listado_nota=[]
        try:
            conex = Conexion()
            query = f'''
                Select * FROM nota
            '''
            cursor = conex.ejecutar_sentencia(query)
            filas = cursor.fetchall()
            print("Nro\t|\tnota1\t|\tnota2\t|\tnota3\t|\tnota4\t|\tPromedio")
            print("-------------------------------------------------------------------------------------------")
            for fila in filas:
                nota = """{}\t|\t{}\t|\t{}\t|\t{}\t|\t{}\t|\t{}""".format(str(fila[0]),fila[2], fila[3], fila[4], fila[5], fila[6])
                listado_nota.append(nota)
                print(nota)
            return nota
        except Exception as e:
            raise
            print(e)
        finally:
            conex.cerrar_conexion()


#probar = Nota("","","","","","")
#probar.mostrarNotaParaAlumno()

#agregar = Alumno("Jose","Aguirre",6)
#agregar.agregarAlumno(agregar)

#obtener = Alumno("","","")
#obtener.obtenerAlumno(1)

#actualizar = Alumno("jesus","tuesta")
#actualizar.actualizarAlumno(1,actualizar)

#eliminar = Alumno("","")
#eliminar.eliminarAlumno(6)

#listar = Nota("","","","","","")
#listar.listarNota()