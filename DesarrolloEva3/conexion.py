import sqlite3
from sqlite3 import Error

class DAO():
    def __init__(self):
        try:
            self.conexion = sqlite3.connect('bdpruebas.sqlite3')
            # Crear un cursor para ejecutar comandos
            self.cursor = self.conexion.cursor()
            print("Conexión exitosa y BD creada/abierta")
        except Error as ex:
            print("Error de conexión: {0}".format(ex))
    
    def crearTablaEstudiante(self):
        try:
            self.cursor.execute('''
                CREATE TABLE estudiante(
	                id_estudiante INTEGER PRIMARY KEY,
	                rut TEXT,
                    nombres TEXT,
                    apellidos TEXT,
                    estado INTEGER
                )
            ''')
            self.conexion.commit()
            print("Tabla creada exitosamente")
        except Error as ex:
            print(f"Error creando tabla: {ex}")

    def crearTablaCalificacion(self):
        try:
            self.cursor.execute('''
                CREATE TABLE calificacion(
                    id_calificacion INTEGER PRIMARY KEY,
                    id_estudiante INTEGER REFERENCES estudiante(id_estudiante),
                    asignatura TEXT,
                    nota REAL
                )
            ''')
            self.conexion.commit()
            print("Tabla creada exitosamente")
        except Error as ex:
            print(f"Error creando tabla: {ex}")        


    def agregarRegistrosTablaEstudiante(self):
        try:
            estudiantes = [
                ('14464221-k','Pepe','Tapia',1),
                ('15464221-9','Carlos','Torres',1),
                ('16464221-8','Claudia','Reyes',2)
            ]
            
            for estudiante in estudiantes:
                self.cursor.execute('''
                    INSERT INTO estudiante (rut,nombres,apellidos,estado)
                    VALUES (?, ?, ?, ?)
                ''', estudiante)
            
            self.conexion.commit()
            print("registros agregados exitosamente")
            
        except Error as ex:
            print(f"Error agregando registros: {ex}")

    def agregarRegistrosTablaCalificacion(self):
        try:
            calificaciones = [
                (2,"Bases de Datos",3.5),
                (2,"Bases de Datos",6.5),
                (1,"Algebra",5.5),
                (1,"Algebra",6.7),
                (3,"Programacion",3.0)
            ]
            
            for calificacion in calificaciones:
                self.cursor.execute('''
                    INSERT INTO calificacion (id_estudiante,asignatura,nota)
                    VALUES (?, ?, ?)
                ''', calificacion)
            
            self.conexion.commit()
            print("registros agregados exitosamente")
            
        except Error as ex:
            print(f"Error agregando registros: {ex}") 


    def obtenerEstudiantes(self):
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM estudiante")
                resultado=cursor.fetchall()
                return resultado
            except Error as ex:
                print("Error de conexión: {0}".format(ex))          

    def obtenerEstudiantesConNotas(self):
            try:
                cursor=self.conexion.cursor()
                cursor.execute('''SELECT estudiante.id_estudiante, estudiante.nombres, estudiante.apellidos, calificacion.asignatura, calificacion.nota
                                  FROM estudiante
                                  JOIN calificacion ON estudiante.id_estudiante = calificacion.id_estudiante''')
                resultado=cursor.fetchall()
                return resultado
            except Error as ex:
                print("Error de conexión: {0}".format(ex))  
    
    def obtenerPromediosEstudiantePorId(self, id_estudiante):
        try:
            cursor = self.conexion.cursor()
            cursor.execute('''
                SELECT 
                    e.nombres,
                    e.apellidos,
                    c.asignatura,
                    ROUND(AVG(c.nota), 2)
                FROM estudiante e
                JOIN calificacion c ON e.id_estudiante = c.id_estudiante
                WHERE e.id_estudiante = {0}
                GROUP BY e.id_estudiante, e.nombres, e.apellidos, c.asignatura
            '''.format(id_estudiante))
            resultados = cursor.fetchall()
            return resultados
        except Error as ex:
            print("Error de conexión: {0}".format(ex))
            return None

    def agregarEstudiante(self,estudiante):
            try:
                cursor=self.conexion.cursor()
                query="INSERT INTO estudiante (rut,nombres,apellidos,estado) VALUES ('{0}','{1}','{2}',{3})"
                cursor.execute(query.format(estudiante[0],estudiante[1],estudiante[2],estudiante[3]))
                self.conexion.commit()
                print("Estudiante agregado OK..")
            except Error as ex:
                print("Error de conexión: {0}".format(ex)) 

    def agregarNota(self,calificacion):
            try:
                cursor=self.conexion.cursor()
                query="INSERT INTO calificacion (id_estudiante,asignatura,nota) VALUES ('{0}','{1}','{2}')"
                cursor.execute(query.format(calificacion[0],calificacion[1],calificacion[2]))
                self.conexion.commit()
                print("Nota agregada OK..")
            except Error as ex:
                print("Error de conexión: {0}".format(ex))

    def buscarEstudiante(self,id):
         try:
            cursor=self.conexion.cursor()
            cursor.execute("SELECT * FROM estudiante WHERE id_estudiante = {0}".format(id))
            resultado=cursor.fetchone()
            return resultado
         except Error as ex:
                    print("Error de conexión: {0}".format(ex))




    def actualizarEstudiante(self,estudiante):
            try:
               cursor=self.conexion.cursor()
               query="UPDATE estudiante SET rut='{0}',nombres='{1}',apellidos='{2}',estado={3} WHERE id_estudiante={4}" 
               cursor.execute(query.format(estudiante[1],estudiante[2],estudiante[3],estudiante[4],estudiante[0]))
               self.conexion.commit()
               print("Estudiante actualizado OK..") 
            except Error as ex:
                    print("Error de conexión: {0}".format(ex))


    def cerrarConexion(self):
         self.conexion.close()
         print("Conexion Cerrada.")


dao = DAO()
""" promedioEstudiante = dao.obtenerPromedioEstudiantePorId(1)
print(promedioEstudiante) """
  
#print(estudiantesconNota)
###########################################
#### CREAR TABLAS E INSERTAR REGISTROS ####
###########################################

#dao.crearTablaEstudiante()
#dao.crearTablaCalificacion()
#dao.agregarRegistrosTablaEstudiante()
#dao.agregarRegistrosTablaCalificacion()

###############################
######## PRUEBAS ##############
##############################
        
#promedios = dao.obtenerPromediosEstudiantePorId(1)
#print(promedios)   #   [('Pepe', 'Tapia', 'Algebra', 6.1), ('Pepe', 'Tapia', 'Programacion', 4.3)]   