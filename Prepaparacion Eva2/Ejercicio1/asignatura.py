class Asignatura():
    def __init__(self,nombreAsignatura,nota1,nota2):
        self.nombreAsignatura=nombreAsignatura
        self.nota1=nota1
        self.nota2=nota2

    def mostrarAsignatura(self):
        # calcula promedio ponderado
        promedioPonderado = (self.nota1 * 0.3) + (self.nota2 * 0.7)
        
        return "\nDatos de la Asignatura\n"+\
                "Nombre Asignatura  : "+self.nombreAsignatura+"\n"+\
                "Nota 1  30%           : "+str(self.nota1)+"\n"+\
                "Nota 2  70%           : "+str(self.nota2)+"\n"+\
                "Promedio Ponderado : "+str(round(promedioPonderado, 2))+"\n"
                








