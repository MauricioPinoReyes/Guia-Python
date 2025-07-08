#1.	Función menú de opciones con las cuatro operaciones básicas 
# (sumar, restar, multiplicar y dividir). Casa función debe 
# devolver el resultado de la operación (puedes tener una 
# función única que realice las cuatro operaciones)

""" def operaciones_basicas(num1, num2, operacion):
    
    if operacion == 1:  # Sumar
        return num1 + num2
    elif operacion == 2:  # Restar
        return num1 - num2
    elif operacion == 3:  # Multiplicar
        return num1 * num2
    elif operacion == 4:  # Dividir
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: división por cero"
    else:
        return None

def menu():
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    opcion = int(input("Seleccione una operación (1-4): "))
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    resultado = operaciones_basicas(num1, num2, opcion)
    
    if resultado is not None:
        print(f"El resultado es: {resultado}")
    else:
        print("Operación no válida") """




#2.	Función que reciba un texto de caracteres y cuente cuántas vocales contiene

""" def contar_vocales(texto):
    contador = 0
    for caracter in texto:
        if caracter.lower() in {'a', 'e', 'i', 'o', 'u'}:
            contador += 1
    return contador

texto = input("Ingrese un texto: ")
print(f"El texto contiene {contar_vocales(texto)} vocales") """




#3.	Función que reciba un número entre 1 y 999 y devuelva el número separado en 
# unidad, decena y centena, si por ejemplo recibe:
#a.	El 238, debe devolver el 2, 3 y 8
#b.	El 97, debe devolver 0, 9 y 7
#c.	El 8, debe devolver 0, 0 y 8

""" def separar_numero(numero):
    if numero < 1 or numero > 999:
        return "Número fuera de rango"
    
    centenas = numero // 100
    decenas = (numero % 100) // 10
    unidades = numero % 10
    
    return centenas, decenas, unidades


c, d, u = separar_numero(238)
print(f"Centenas: {c}, Decenas: {d}, Unidades: {u}") """





#4.	Función que reciba un número entero de máximo 10 dígitos (mayor que cero) 
# y lo devuelva invertido, por ejemplo, si recibe el 397, debe devolver el 793 

""" def invertir_numero(numero):
    if numero <= 0 or numero > 9999999999:
        return "Número fuera de rango válido"
    
    numero_invertido = 0
    while numero > 0:
        digito = numero % 10
        numero_invertido = numero_invertido * 10 + digito
        numero = numero // 10
    
    return numero_invertido


num = int(input("Ingrese un número: "))
print(f"El número invertido es: {invertir_numero(num)}") """