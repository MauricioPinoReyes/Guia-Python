#1.	Función menú de opciones con las cuatro operaciones básicas 
# (sumar, restar, multiplicar y dividir). Casa función debe 
# devolver el resultado de la operación (puedes tener una 
# función única que realice las cuatro operaciones)

def ingresarNumeros():
    numero1 = int(input("Ingrese el primer número:"))
    numero2 = int(input("Ingrese el segundo número:"))
    return numero1,numero2

def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b

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


#2.	Función que reciba un texto de caracteres y cuente cuántas vocales contiene

""" def ingresarTexto():
    return input("Ingrese texto : ").lower()

def contarVocales(texto):
    contador = 0
    for letra in texto:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            contador+=1
    return contador

def main():
    texto = ingresarTexto()
    cantVocales = contarVocales(texto)
    print(f"La cantidad de vocales es: {cantVocales}")
    
##PP
main() """

#3.	Función que reciba un número entre 1 y 999 y devuelva el número separado en 
# unidad, decena y centena, si por ejemplo recibe:
#a.	El 238, debe devolver el 2, 3 y 8
#b.	El 97, debe devolver 0, 9 y 7
#c.	El 8, debe devolver 0, 0 y 8

""" def ingresarNumero():
    while True:
        numero = int(input("Ingrese numero: "))
        if 1 <= numero <= 999:
            return numero
        else:
            print("Número fuera de rango. Intente de nuevo.")

def separarNumero(numero):
    centenas = numero // 100
    decenas = (numero % 100) // 10
    unidades = numero % 10
    
    return centenas, decenas, unidades

def main():    
    numero = ingresarNumero()
    c, d, u = separarNumero(numero)
    print(f"{c}, {d} y {u}")

##PP
main() """



#4.	Función que reciba un número entero de máximo 10 dígitos (mayor que cero) 
# y lo devuelva invertido, por ejemplo, si recibe el 397, debe devolver el 793 

""" def ingresarNumero():
     while True:
        numero = int(input("Ingrese numero: "))
        if numero > 0 and numero  < 9999999999:
            return numero
        else:
            print("Número fuera de rango. Intente de nuevo.")

        
def invertirNumero(numero):
    numeroString = str(numero)
    numeroInvertido = ""
    for i in range(len(numeroString) - 1, -1, -1):
        numeroInvertido = numeroInvertido + numeroString[i]
    
    return int(numeroInvertido)

def main():
    numero = ingresarNumero()
    numeroInvertido= invertirNumero(numero)
    print(f"El número original es: {numero}")
    print("================")
    print(f"El número invertido es: {numeroInvertido} ")
    


##PP
main() """


