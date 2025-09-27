class Rut():
    def __init__(self,rut,dv):
        self.rut=rut # 12345678
        self.dv=dv # "K"

    def mostrarRut(self):
        return str(self.rut)+"-"+self.dv # 12345678-K   
    
    def validarRut(self):
        #código de validación rut
        return True