class Mantencion():
    def __init__(self,descripcion,fecha):
        self.descripcion=descripcion
        self.fecha=fecha

    def mostrarMantencion(self):
        return  "Detalle Mantención\n"+\
                "Descripción    : "+self.descripcion+"\n"+\
                "Fecha          : "+self.fecha
    
    