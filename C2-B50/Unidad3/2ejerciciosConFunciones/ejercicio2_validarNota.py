""" construya una funcion que lee una nota y valide
que sea valida (rango 1.0 a 7.0) """

def leerNota():
    while True:
        nota=int(input("Ingrese nota : "))
        if nota >= 1.0 and nota <= 7.0:
            return nota
        else:
            print("Nota fuera de rango")
        
            

leerNota()    