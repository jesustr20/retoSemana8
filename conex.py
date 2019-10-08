import pymysql
import pymysql.cursors
class Conexion():
    def __init__(self, server="localhost", user="root", passwrd="sasa", db="colegio"):
        self.db = pymysql.connect(server, user, passwrd, db)
        self.cursors = self.db.cursor()
        #print("Conexion establecida")

    def ejecutar_sentencia(self, sql):
        self.cursors.execute(sql)
        return self.cursors
    
    def cerrar_conexion(self):
        self.db.close()
        #print("Desconectado")
    
    def commit(self):
        self.db.commit()
        return
    
    def rollback(self):
        self.db.rollback()
        return