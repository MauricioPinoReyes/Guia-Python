from estudiante import Estudiante

class Nota(Estudiante):
    def __init__(self,rut,nombre,carrera,id,notaEva,asignatura,numEva,fecha):
        super().__init__(rut,nombre,carrera)
        self.id=id
        self.notaEva=notaEva
        self.asignatura=asignatura
        self.numEva=numEva
        self.fecha=fecha

    def mostrarNota(self):
        return super().mostrarEstudiante()+" > "+str(self.id)+" > "+str(self.notaEva)+" > "+\
        self.asignatura+" ("+str(self.numEva)+\
            ") > "+self.fecha.mostrarFecha()