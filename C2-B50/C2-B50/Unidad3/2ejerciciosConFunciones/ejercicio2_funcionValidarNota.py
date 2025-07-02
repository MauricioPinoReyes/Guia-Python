"""
TAREA 1:
Construya una función que lea una nota y valide que 
sea válida
RANGO 1.0 a 7.0
"""
def validarNota():
    while True:
        nota=float(input("Ingresa una nota (1.0-7.0): "))
        if nota>=1 and nota<=7.0:
            return nota
        else:
            print("Nota fuera de rango")
        """
        if nota<1 or nota>7:
            print("Nota fuera de rango")
        else:
            return nota
        """

def leerN():
    while True:
        n=int(input("Ingresa el nùmero de notas (n>0): "))
        if n>0:
            return n
        else:
            print("El n debe ser > 0")

#PP
n=leerN()
suma=0
for i in range(n):
    suma += validarNota()
promedio=round(suma/n,1)
if promedio>=4:
    print("APROBADO")
else:
    print("REPROBADO")
    

