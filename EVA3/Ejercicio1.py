#1.	Función menú de opciones con las cuatro operaciones básicas 
# (sumar, restar, multiplicar y dividir). Casa función debe 
# devolver el resultado de la operación (puedes tener una 
# función única que realice las cuatro operaciones)

def ingresarNumeros():
    numero1 =float(input("Ingrese el primer número:"))
    numero2 = float(input("Ingrese el segundo número:"))
    return numero1,numero2

def sumar(a,b):
    return round(a+b,2)

def restar(a,b):
    return round(a-b,2)

def multiplicar(a,b):
    return round(a*b,2)

def dividir(a,b):
    return round(a/b,2) 

def operar(a, b):
    while True:
        print("Operaciones disponibles:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        operacion = int(input("Ingrese operacion: "))
        
        if operacion == 1:
            return sumar(a,b)
        elif operacion == 2:
            return restar(a,b)
        elif operacion == 3:
            return multiplicar(a,b)
        elif operacion == 4:
            if b == 0:
                print("Error: No se puede dividir entre cero. Intente otra operación.")
            else:
                return dividir(a,b)
        else:
            print("Opción inválida. Intente de nuevo.")

def main():
    numero1, numero2 = ingresarNumeros()
    resultado = operar(numero1,numero2)
    print(f"El resultado de la operacion es: {resultado}")

#PP
main()