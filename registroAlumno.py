from conex import Conexion

class Alumno():
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def agregarAlumno(self, alum):
        try:
            conex = Conexion()
            query = f'''
                INSERT INTO alumno(nombre, apellido, edad)
                VALUES ('{alum.nombre}','{alum.apellido}', '{alum.edad}')          
            '''
            conex.ejecutar_sentencia(query)
            conex.commit()
        except Exception as e:
            raise
            print(e)
        finally:
            conex.cerrar_conexion()


    def actualizarAlumno(self, id_alumn, alumn):
        try:
            conex = Conexion()
            query = f'''
                UPDATE alumno
                SET nombre = '{alumn.nombre}',
                apellido = '{alumn.apellido}',
                edad = '{alumn.edad}'
                WHERE id = {id_alumn}
            '''
            conex.ejecutar_sentencia(query)
            conex.commit()
        except Exception as e:
            raise
            print(e)
        finally:
            conex.cerrar_conexion()

    def obtenerAlumno(self, id_alumn):
        try:
            conex = Conexion()
            query = f'''
                SELECT * FROM alumno WHERE id={id_alumn}
            '''
            cursors = conex.ejecutar_sentencia(query)
            fila = cursors.fetchone()  
            alumn = Alumno(fila[1], fila[2], fila[3])
            print("Nro\t|\tNombre\t\t|\tApellido\t|\tEdad")
            print("---------------------------------------------------------------------")
            print(str(fila[0]),"\t|\t",alumn.nombre,"\t|\t",alumn.apellido,"\t|\t",alumn.edad)
            return alumn
        except Exception as e:
            raise
            print(e)
        finally:
            conex.cerrar_conexion()


    def eliminarAlumno(self, id_alumn):
        try:
            conex = Conexion()
            query = f'''
                DELETE FROM alumno WHERE id={id_alumn}
            '''
            cursor = conex.ejecutar_sentencia(query)
            conex.commit()
            return True
        except Exception as e:
            raise
            print(e)
        finally:
            conex.cerrar_conexion()
    
    def listarAlumno(self):
        listado_alumno=[]
        try:
            conex = Conexion()
            query = f'''
                Select * FROM alumno
            '''
            cursor = conex.ejecutar_sentencia(query)
            filas = cursor.fetchall()
            print("Nro\t|\tNombre\t\t|\tApellido,\t|\tEdad")
            for fila in filas:
                alum = """{}\t|\t{}\t\t|\t{}\t\t|\t{}""".format(str(fila[0]), fila[1], fila[2], fila[3])
                print("-----------------------------------------------------------------------")
                listado_alumno.append(alum)
                print(alum)
            return alum
        except Exception as e:
            raise
            print(e)
        finally:
            conex.cerrar_conexion()

    #Para la clase Matricula
    def mostrarDatosAlumno(self):
        listado_alumno=[]
        try:
            conex = Conexion()
            query = f'''
                Select * FROM alumno
            '''
            cursor = conex.ejecutar_sentencia(query)
            filas = cursor.fetchall()
            print("Nro\t|\tNombre\t\t|\tApellido,\t|\tEdad")
            print("-----------------------------------------------------------------------")
            for fila in filas:
                alum = """{}\t|\t{}\t\t|\t{}\t\t|\t{}""".format(str(fila[0]), fila[1], fila[2], fila[3])
                listado_alumno.append(alum)
                print(alum)
            return alum
        except Exception as e:
            raise
            print(e)
        finally:
            conex.cerrar_conexion()



#mostrar = Alumno("","","")
#mostrar.mostrarDatosAlumno()

#agregar = Alumno("Jose","Aguirre",6)
#agregar.agregarAlumno(agregar)

#obtener = Alumno("","","")
#obtener.obtenerAlumno(1)

#actualizar = Alumno("jesus","tuesta")
#actualizar.actualizarAlumno(1,actualizar)

#eliminar = Alumno("","")
#eliminar.eliminarAlumno(6)

#listar = Alumno("","","")
#listar.listarAlumno()