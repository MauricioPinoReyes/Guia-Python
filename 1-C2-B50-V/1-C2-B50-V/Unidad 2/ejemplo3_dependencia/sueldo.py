class Sueldo():
    def __init__(self,sueldoBase,bono):
        self.sueldoBase=sueldoBase
        self.bono=bono
    
    def mostrarSueldo(self):
        totalSueldo=self.sueldoBase+self.bono
        return  "\nDetalle Sueldos\n"+\
                "Sueldo base    : "+str(self.sueldoBase)+"\n"+\
                "Bono           : "+str(self.bono)+"\n"+\
                "Total sueldo   : "+str(totalSueldo)
    
    def otrosMetodos(self):
        pass
    