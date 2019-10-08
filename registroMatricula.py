from conex import Conexion

class Matricula():
    def __init__(self, turno_id, salon_id, alumno_id, periodoescolar_id, nota_id):
        self.turno_id = turno_id
        self.salon_id = salon_id
        self.alumno_id = alumno_id
        self.periodoescolar_id = periodoescolar_id
        self.nota_id = nota_id
    
    def agregarMatricula(self, matr):
        try:
            conex = Conexion()
            query = f'''
                INSERT INTO matricula(turno_id, salon_id, alumno_id, periodoescolar_id, nota_id)
                VALUES ('{matr.turno_id}','{matr.salon_id}', '{matr.alumno_id}', '{matr.periodoescolar_id}', '{matr.nota_id}')
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
    
    def listarMatricula(self):
        listado_matricula = []
        try:
            conex = Conexion()
            query = f'''
                Select * FROM matricula
            '''
            cursor = conex.ejecutar_sentencia(query)
            filas = cursor.fetchall()
            print("Nro\t|\tturno\t|\tsalon\t|\talumno\t|PeriodoEscolar\t|\tnota")
            for fila in filas:
                matricu = """{}\t|\t{}\t|\t{}\t|\t{}\t|\t{}\t|\t{}""".format(str(fila[0]), fila[1], fila[2], fila[3], fila[4], fila[5])
                print("----------------------------------------------------------------------------------------")
                listado_matricula.append(matricu)
                print(matricu)
            return matricu
        except Exception as e:
            raise
            print(e)
        finally:
            conex.cerrar_conexion()



    #Metodo especial para la clase ALUMNO
    def mostrarMatricula(self):
        listado_matricula = []
        try:
            conex = Conexion()
            query = f'''
                Select * FROM matricula
            '''
            cursor = conex.ejecutar_sentencia(query)
            filas = cursor.fetchall()
            print("Nro\t|\tturno\t|\tsalon\t|\talumno\t|PeriodoEscolar\t|\tnota")
            print("----------------------------------------------------------------------------------------")
            for fila in filas:
                matricu = """{}\t|\t{}\t|\t{}\t|\t{}\t|\t{}\t|\t{}""".format(str(fila[0]), fila[1], fila[2], fila[3], fila[4], fila[5])
                listado_matricula.append(matricu)
                print(matricu)
            return matricu
        except Exception as e:
            raise
            print(e)
        finally:
            conex.cerrar_conexion()


#agregar = Alumno("Jose","Aguirre",6)
#agregar.agregarAlumno(agregar)

#obtener = Alumno("","","")
#obtener.obtenerAlumno(1)

#actualizar = Alumno("jesus","tuesta")
#actualizar.actualizarAlumno(1,actualizar)

#eliminar = Alumno("","")
#eliminar.eliminarAlumno(6)

#listar = Matricula("","","","","")
#listar.listarMatricula()

#mostrar = Matricula("","","","","")
#mostrar.mostrarMatricula()