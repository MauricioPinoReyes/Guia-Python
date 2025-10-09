class Doctor():
    def __init__(self,id,nombre,especialidad,aniosExperiencia,paciente):
        self.id=id
        self.nombre=nombre
        self.especialidad=especialidad
        self.aniosExperiencia=aniosExperiencia
        self.paciente=paciente
        
    def mostrarDoctor(self):
        return  "\nDatos del Doctor \n"+\
                "ID               : "+str(self.id)+"\n"+\
                "Nombre           : "+self.nombre+"\n"+\
                "Especialidad     : "+self.especialidad+"\n"+\
                "Años Experiencia : "+str(self.aniosExperiencia)+"\n"+\
                "Datos del Paciente   : "+self.paciente.mostrarPaciente()+"\n"

    def cambiarNombreDoctor(self):
        self.nombre = input("Ingrese Nombre Doctor: ")
        print("Nombre doctor cambiado...")
    
    
    def buscarPacientePorNombre(self,nombre):
        if nombre==self.paciente.nombre:
            print("Paciente encontrado...")
            print(self.paciente.mostrarPaciente())
        else:
            print("Paciente No encontrado...")       

    def buscarPacientePorComuna(self,comuna):
        if comuna==self.paciente.comuna:
            print("Paciente encontrado...")
            print(self.paciente.mostrarPaciente())
        else:
            print("Paciente No encontrado...")        

    def cambiarDiagnostico(self):
        self.paciente.diagnostico = input("Ingrese diagnostico:")
        print("Diagnostico Cambiado...")       


    def menu(self):
        print("** Menu del Sistema **")
        print("1. Mostrar Datos del Doctor ")     
        print("2. Cambiar Nombre del Doctor ")     
        print("3. Buscar Paciente por nombre ")     
        print("4. Buscar Paciente por comuna ")     
        print("5. Cambiar Diagnostico  ")     
        print("6. Salir del Menu  ")     
