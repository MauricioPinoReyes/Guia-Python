class Paciente():
    def __init__(self,nombre,comuna,fono,diagnostico):
        self.id=id
        self.nombre=nombre
        self.comuna=comuna
        self.fono=fono
        self.diagnostico=diagnostico

    def mostrarPaciente(self):
        return  "\nDatos del Paciente\n"+\
                "Nombre      : "+self.nombre+"\n"+\
                "Comuna      : "+self.comuna+"\n"+\
                "Fono        : "+self.fono+"\n"+\
                "Diagnostico : "+self.diagnostico+"\n"

    

        