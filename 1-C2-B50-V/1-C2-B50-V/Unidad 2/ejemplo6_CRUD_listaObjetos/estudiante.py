class Estudiante():
    def __init__(self,id,nombre,edad):
        self.id=id
        self.nombre=nombre
        self.edad=edad
    
    def mostrarEstudiante(self):
        return str(self.id)+"\t"+self.nombre+"\t"+str(self.edad)
    
    def menu(self):
        print("\nMENU DE OPCIONES")
        print("1. Agregar Estudiante (C)reate")
        print("2. Buscar Estudiante (R)ead")
        print("3. Actualizar Estudiante (U)pDate")
        print("4. Eliminar Estudiante (D)elete")
        print("5. Mostrar Estudiantes")
        print("6. Salir")

    def leerId(self):
        return int(input("Ingresa ID: "))
        # TAREA: VALIDAR/CONTROLAR EXCEPCIONES
    
    def buscarEstudiante(self,id,lista):
        for item in lista:
            if id==item.id:
                return item
        return None
    
    def agregarEstudiante(self,id):
        # Validar/Controlar excepciones >>>> TAREA
        nombre=input("Ingresa nombre: ")
        edad=int(input("Ingresa edad: "))
        return Estudiante(id,nombre,edad)
    