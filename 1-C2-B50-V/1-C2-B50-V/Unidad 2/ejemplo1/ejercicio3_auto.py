class Auto():
    def __init__(self):
        self.marca="Kia"
        self.modelo="Rio 5"
        self.anio=2020
        self.color="Gris"
    
    def mostrarAuto(self):
        print("\nLos datos del auto son:")
        print("Marca    :",self.marca)
        print("Modelo   :",self.modelo)
        print("Año      :",self.anio)
        print("Color    :",self.color)

    def mostrarAuto2(self):
        return  "\nLos datos del Auto son (2):\n"+\
                "Marca  : "+self.marca+"\n"+\
                "Modelo : "+self.modelo+"\n"+\
                "Año    : "+str(self.anio)+"\n"+\
                "Color  : "+self.color
# PP
a=Auto()
a.mostrarAuto()
print(a.mostrarAuto2())
