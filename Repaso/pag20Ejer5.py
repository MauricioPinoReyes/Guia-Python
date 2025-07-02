#  PAG 20 ejercicio 5
#5)	Una persona desea saber cuánto dinero se genera por concepto de 
# intereses sobre la cantidad que tiene en inversión en el banco. 
# El decidirá reinvertir los intereses siempre y cuando estos excedan 
# a $7000, y en ese caso desea saber cuánto dinero tendrá finalmente en su cuenta.

#==============================================
#Nota: Funcion cargarDatos() optimizada:
#==============================================
""" def cargarDatos():
    while True:
        dineroInvertido = float(input("Ingrese dinero invertido: "))  # Input dentro del while
        if dineroInvertido > 0:
            break
        print("Debe ingresar un número mayor a 0.")  # Mensaje de error fuera del else
    
    while True:
        interes = float(input("Ingrese interés: "))  # Input dentro del while
        if interes > 0:
            break
        print("El interés debe ser mayor a 0.")  # Mensaje de error fuera del else
    
    return dineroInvertido, interes """


def cargarDatos():
    dineroInvertido = float(input("Ingrese dinero invertido: "))
    while True:
        if dineroInvertido > 0:
            #return dineroInvertido # Nota: no se puede usar dos return en la misma funcion
            break
        else:
            dineroInvertido = float(input("Debe ingresar un numero mayor a 0.Ingrese dinero invertido: ")) 
    
    interes = float(input("Ingrese interes: "))
    while True:
        if interes > 0:
            #return interes # Nota: no se puede usar dos return en la misma funcion
            break
        else:
            interes = float(input("El interes debe ser mayor a 0.Ingrese interes: "))
    return dineroInvertido,interes

def calularDatos(dineroInvertido,interes):
    if dineroInvertido > 7000:
        return (dineroInvertido * interes) + dineroInvertido
    else:
        return dineroInvertido

def leerRespuesta():
    return input("Desea continuar (S/N): ").upper()

def main():
    while True:
        dineroInvertido,interes = cargarDatos()
        print(f"El saldo en la cuenta es: {calularDatos(dineroInvertido,interes)}")
        if dineroInvertido > 7000:
            print("El dinero será reinvertino")
        else:
             print("El dinero NO será reinvertino")   
        if leerRespuesta()=="N":
            break

#PP

main()





