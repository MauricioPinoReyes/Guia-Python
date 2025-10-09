class Estudiante():
    def __init__(self,id,nombre,carrera,asignatura):
        self.id=id
        self.nombre=nombre
        self.carrera=carrera
        self.asignatura=asignatura

    def mostrarEstudiante(self):
        return "\nDatos Estudiante\n"+\
                "Id Estudiante : "+str(self.id)+"\n"+\
                "Nombre Estudiante : "+self.nombre+"\n"+\
                "Nombre Carrera : "+self.carrera+"\n"+\
                self.asignatura.mostrarAsignatura()+"\n"

    def cambiarAsignatura(self):
        self.asignatura.nombreAsignatura=input("Nombre Asignatura: ")

    def cambiarCarrera(self):
        self.carrera=input("Nombre Carrera: ")

    def cambiarNotas(self):
        self.asignatura.nota1=float(input("Ingrese nota 1: "))
        self.asignatura.nota2=float(input("Ingrese nota 2: "))

    def menu(self):
        print("\nMENU ")
        print("1. Mostrar Estudiante")
        print("2. Cambiar Asignatura")
        print("3. Cambiar Carrera")
        print("4. Cambiar Notas")
        print("5. Finalizar")
