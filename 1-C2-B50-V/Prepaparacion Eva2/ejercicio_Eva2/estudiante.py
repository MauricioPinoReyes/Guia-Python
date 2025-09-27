

class Estudiante():
    def __init__(self,rut,nombre,carrera):
        self.rut=rut
        self.nombre=nombre
        self.carrera=carrera

    def mostrarEstudiante(self):
        return self.rut.mostrarRut()+" > "+self.nombre+" > "+self.carrera.mostrarCarrera()
        