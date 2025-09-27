class Cliente():
    def __init__(self,id,apellidos,nombres,edad,eCivil,estado):
        self.id=id
        self.apellidos=apellidos
        self.nombres=nombres
        self.edad=edad
        self.eCivil=eCivil          # 1=Sol, 2=Cas, 3=Viu, 4=Div
        self.estado=estado          # True = Activo     False = INACTIVO
    
    def mostrarCliente(self):
        return  "\nDATOS DEL/LA CLIENTE\n"+\
                "Id         : "+str(self.id)+"\n"+\
                "Apellido   : "+self.apellidos+"\n"+\
                "Nombres    : "+self.nombres+"\n"+\
                "Edad       : "+str(self.edad)+"\n"+\
                "E. Civil   : "+self.mostrarECivil()+"\n"+\
                "Estado     : "+self.mostrarEstado()+"\n"

    def mostrarECivil(self):
        eCivil=""
        match self.eCivil:
            case 1:
                eCivil="Soltero/a"
            case 2:
                eCivil="Casado/a"
            case 3:
                eCivil="Viudo/a"
            case 4:
                eCivil="Divorciado/a"
        return eCivil
    
    def mostrarEstado(self):
        if self.estado:
            return "ACTIVO"
        else:
            return "INACTIVO"

    def cambiarEstado(self):
        # agregar pregunta de confirmacion
        if self.estado:
            self.estado=False
        else:
            self.estado=True
