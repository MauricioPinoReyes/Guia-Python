class Vehiculo():
    def __init__(self,id,nombre,marca,modelo,anio,mantencion):
        self.id=id
        self.nombre=nombre
        self.marca=marca
        self.modelo=modelo
        self.anio=anio
        self.mantencion=mantencion
    
    def mostrarVehiculo(self):
        return  "\nDatos del Vehículo\n"+\
                "Id             : "+str(self.id)+"\n"+\
                "Nombre CLIENTE : "+self.nombre+"\n"+\
                "Marca          : "+self.marca+"\n"+\
                "Modelo         : "+self.modelo+"\n"+\
                "Año            : "+str(self.anio)+"\n"+\
                self.mantencion.mostrarMantencion()

    def cambiarVehiculo(self):
        self.id=int(input("Id del Vehículo: "))
        self.nombre=input("Nombre del/la CLIENTE: ")
        self.marca=input("Marca: ")
        self.modelo=input("Modelo: ")
        self.anio=input("Año: ")
        self.mantencion.descripcion=input("Descripción: ")
        self.mantencion.fecha=input("Fecha: ")

    def buscarVehiculo(self,id):
        if id==self.id:
            print("Vehículo encontrado...")
            print(self.mostrarVehiculo())
        else:
            print("Vehículo NO encontrado...")
        
    def cambiarMantencion(self):
        self.mantencion.descripcion=input("Descripción: ")
        self.mantencion.fecha=input("Fecha: ")

    def menu(self):
        print("\nMENU TALLER")
        print("1. Mostrar vehículo")
        print("2. Cambiar vehículo")
        print("3. Buscar vehículo")
        print("4. Cambiar mantención")
        print("5. Finalizar")
    
    
        

        

