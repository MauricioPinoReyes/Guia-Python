class Cuenta():
    def __init__(self,nombre,saldo,sobregiro,MAXSG):
        self.nombre=nombre
        self.saldo=saldo
        self.sobregiro=sobregiro
        self.MAXSG=MAXSG    # MAXSG: Máximo sobregiro

    def mostrarSaldo(self):
        return  "\n*** Consulta Saldo ***:\n"+\
                "Nombre     : "+self.nombre+"\n"+\
                "Saldo      : "+str(self.saldo)+"\n"+\
                "Sobregiro  : "+str(self.sobregiro)+"\n"+\
                "Máximo SG  : "+str(self.MAXSG)
    
    def depositar(self,monto):
        if monto>0:
            self.saldo+=monto
            print("\nDepósito realizado exitosamente")
        else:
            print("\nEl monto a depositar debe ser >0")

    def girar(self,monto):
        if monto <= self.saldo:
            self.saldo-=monto
            print("\nGiro realizado exitosamente")
        elif monto <= self.saldo+self.sobregiro:
            self.sobregiro-=(monto-self.saldo)
            self.saldo=0
            print("\nGiro realizado exitosamente")
        else:
            print("\nSaldo insuficiente")

    def abonarSobregiro(self,monto):
        pass

    def menu(self):
        return  "\nMENU DE OPERACIONES\n"+\
                "1. Mostrar Saldo\n"+\
                "2. Realizar Depósito\n"+\
                "3. Realizar Giro\n"+\
                "4. Abonar al Sobregiro\n"+\
                "5. Finalizar\n"

    def leerOpcionMenu(self):
        return int(input("Ingresa una opción (1-5): "))
    
    def leerMonto(self,mensaje):
        return int(input("Ingresa monto a "+mensaje+": "))

#PP
cta=Cuenta("Juanito",200,500,500)
while True:
    print(cta.menu())
    opc=cta.leerOpcionMenu()
    if opc==1:
        print(cta.mostrarSaldo())
    elif opc==2:
        cta.depositar(cta.leerMonto("DEPOSITAR"))
    elif opc==3:
        cta.girar(cta.leerMonto("GIRAR"))
    elif opc==4:
        cta.abonarSobregiro(cta.leerMonto("ABONAR"))
    else:
        break
print("\nHasta la vista baby....")

# tarea: AGREGAR CONTROL DE EXCEPCIONES try/except