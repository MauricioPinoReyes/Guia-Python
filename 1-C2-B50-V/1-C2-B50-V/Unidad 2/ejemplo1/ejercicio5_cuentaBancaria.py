class Cuenta():
    def __init__(self,nombre,saldo):
        self.nombre=nombre
        self.saldo=saldo

    def mostrarSaldo(self):
        return "\nNombre: "+self.nombre+"\tSaldo:"+str(self.saldo)
    
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
        else:
            print("\nSaldo insuficiente")

    def menu(self):
        return  "\nMENU DE OPERACIONES\n"+\
                "1. Mostrar Saldo\n"+\
                "2. Relizar Depósito\n"+\
                "3. Realizar Giro\n"+\
                "4. Finalizar\n"

    def leerOpcionMenu(self):
        return int(input("Ingresa una opción (1-4): "))
    
    def leerMonto(self,mensaje):
        return int(input("Ingresa monto a "+mensaje+": "))

#PP
cta=Cuenta("Juanito",200000)
while True:
    print(cta.menu())
    opc=cta.leerOpcionMenu()
    if opc==1:
        print(cta.mostrarSaldo())
    elif opc==2:
        cta.depositar(cta.leerMonto("DEPOSITAR"))
    elif opc==3:
        cta.girar(cta.leerMonto("GIRAR"))
    else:
        break
print("\nHasta la vista baby....")

# tarea: AGREGAR CONTROL DE EXCEPCIONES try/except