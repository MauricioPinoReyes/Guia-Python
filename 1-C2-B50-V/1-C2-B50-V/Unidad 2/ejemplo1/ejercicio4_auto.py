class Auto():
    def __init__(self,marca,modelo,anio,color):
        self.marca=marca
        self.modelo=modelo
        self.anio=anio
        self.color=color

    def mostrarAuto(self):
        return  "\nLos datos del Auto son:\n"+\
                "Marca  : "+self.marca+"\n"+\
                "Modelo : "+self.modelo+"\n"+\
                "Año    : "+str(self.anio)+"\n"+\
                "Color  : "+self.color

# PP
a=Auto("Subaru","Impreza",2018,"Gris Oscuro")
print(a.mostrarAuto())
b=Auto("Hyundai","Creta",2014,"Blanca")
print(b.mostrarAuto())
b=Auto("Toyota","Yaris",2020,"Azul")
print(b.mostrarAuto())



