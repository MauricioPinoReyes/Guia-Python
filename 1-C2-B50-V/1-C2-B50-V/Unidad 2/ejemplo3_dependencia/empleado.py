class Empleado():
    def __init__(self,id,apellidos,nombres,cargo,sueldo):
        self.id=id
        self.apellidos=apellidos
        self.nombres=nombres
        self.cargo=cargo
        self.sueldo=sueldo
    
    def mostrarEmpleado(self):
        return  "\nDetalle Empleado\n"+\
                "Id             : "+str(self.id)+"\n"+\
                "Apellidos      : "+self.apellidos+"\n"+\
                "Nombres        : "+self.nombres+"\n"+\
                "Cargo          : "+self.cargo+"\n"+\
                self.sueldo.mostrarSueldo()
    