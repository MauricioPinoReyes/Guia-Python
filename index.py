""" Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco 
se ingresaron. Tener en cuenta que un espacio en blanco es igual a
" ", en cambio una cadena vacía es "" """

""" oracion = input("Ingrese oracion: ")
contador = 0
x = 0
while x <len(oracion):
    if oracion[x] == " ":
        contador = contador + 1    
    x = x + 1

print("La cantidad de espacios vacios es: ")
print(contador)
print("============")
print(oracion) """




# Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. 
# Contar la cantidad de vocales. Crear un segundo string con toda la oración en 
# minúsculas para que sea más fácil disponer la condición que verifica que es una vocal.

""" oracion = input("Ingrese oracion: ")
contador = 0

x = 0
while x < len(oracion):
    oracion_minuscula = oracion.lower()
    if oracion_minuscula[x] == "a" or oracion_minuscula[x] == "e" or oracion_minuscula[x] == "i" or oracion_minuscula[x] == "o" or oracion_minuscula[x] == "u":
        contador = contador + 1
    print(oracion[x])

    x = x + 1

print("La cantidad de vocales es: " )
print(contador)

print("===========")
print(oracion)     """

# Solicitar el ingreso de una clave por teclado y almacenarla en una 
# cadena de caracteres. Controlar que el string ingresado tenga 
# entre 10 y 20 caracteres para que sea válido, en caso contrario 
# mostrar un mensaje de error.

""" clave = input("Ingrese clave: ")
if len(clave) >=10 and len(clave) <=20:
    print("Clave valida")
else:
    print("Clave invalida")    

print(len(clave)) """

#Definir por asignación una lista con 8 elementos enteros. 
#Contar cuantos de dichos valores almacenan un valor superior a 100.

""" lista = [1,45,600,6,23,44,12,120]
contador = 0
x = 0
while x < len(lista):
    if lista[x] > 100:
        contador = contador + 1
    print(lista[x])
    x = x + 1

print("Mayores a 100 ")
print(contador) """

# Definir una lista por asignación con 5 enteros. Mostrar por 
# pantalla solo los elementos con valor iguales o superiores a 7.

""" lista = [1,5,60,6,23,4,2]
contador = 0
x = 0
while x < len(lista):
    if lista[x] >= 7:
        contador = contador + 1
    print(lista[x])
    x = x + 1

print("Mayores o igusales 7 ")
print(contador) """

# Almacenar en una lista los sueldos (valores float) de 5 operarios. 
# Imprimir la lista y el promedio de sueldos

""" NUM_SUELDOS = 5
sueldos = []
suma = 0

for x in range(NUM_SUELDOS):
    valor = float(input("Ingrese el sueldo del operario:"))
    sueldos.append(valor)
    suma += valor

print("Lista de sueldos:", sueldos)
print("Promedio de sueldos:", suma / NUM_SUELDOS) """


# Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
# Obtener el promedio de las mismas. Contar cuántas personas son más altas 
# que el promedio y cuántas más bajas.


# Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 
# empleados (4 por la mañana y 4 por la tarde) Confeccionar un programa 
# que permita almacenar los sueldos de los empleados agrupados en dos listas.
# Imprimir las dos listas de sueldos.

# Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. 
# Mostrar el nombre de persona menor en orden alfabético.

# Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje 
# si se repite dentro de la lista (es decir si dicho valor se encuentra 
# en 2 o más posiciones en la lista)

""" lista = [2,4,6,1,7]

mayor = lista[0]
for x in range(1,len(lista)):
    if lista[x] > mayor :
         mayor = lista[x]

print(mayor) """

# Crear y cargar dos listas con los nombres de 5 productos en una y sus 
# respectivos precios en otra. Definir dos listas paralelas. Mostrar cuantos 
# productos tienen un precio mayor al primer producto ingresado.  

""" productos = ["A","B","C","D","E"]
precios = [1000,1500,2500,800,1200]

cantidad = 0 

for x in range(1,len(precios)):
    if precios[x] > precios[0]:
        cantidad = cantidad + 1

print(cantidad)   """      



# En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente:
# a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
# b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, 
#   colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7, y 
#   colocar "Insuficiente" si la nota es inferior a 4.
# c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.

""" alumnos = ["A","B","C","D"]
notas = [5,7,3,10]
condicion = ""

for x in range(len(alumnos)):
    if notas[x] >= 8:
        condicion = "Muy Bueno"
    elif notas[x] <=7 and notas[x] >=4:
        condicion ="Bueno"
    else:
        condicion = "Insuficiente"        
    print(alumnos[x]+ " " + str(notas[x])+ " " + condicion) """
    


# Realizar un programa que pida la carga de dos listas numéricas enteras 
# de 4 elementos cada una. Generar una tercer lista que surja de la suma 
# de los elementos de la misma posición de cada lista. Mostrar esta tercer lista.

""" lista1 = [3,4,5,2]
lista2 = [2,2,9,8]
lista3 = []

suma = 0
for x in range(len(lista1)):
    suma = lista1[x] + lista2[x]
    lista3.append(suma)

print(lista3)     """

# Desplazar el valor mayor de la lista a la última posición.

""" lista1 = [10,2,9,3,1]

for x in range(4):
    if lista1[x]>lista1[x+1]:
        aux=lista1[x]
        lista1[x]=lista1[x+1]
        lista1[x+1]=aux

print("Lista ordenada")        
print(lista1)     """    

# Ordenar de menor a mayor una lista

""" lista2 = [10,2,9,3,1]

for k in range(4):
    for x in range(4-k):
        if lista2[x]>lista2[x+1]:
            aux=lista2[x]
            lista2[x]=lista2[x+1]
            lista2[x+1]=aux

print("Lista ordenada")
print(lista2) """

# Solicitar por teclado la cantidad de empleados que tiene la empresa. 
# Crear y cargar una lista con todos los sueldos de dichos empleados. 
# Imprimir la lista de sueldos ordenamos de menor a mayor.

""" cant_empleados = int(input("Ingrese cantidad de empleados: "))
sueldos = []

for x in range(cant_empleados):
    sueldo = float(input("Ingrese sueldo: "))
    sueldos.append(sueldo)

for k in range(cant_empleados-1):
    for x in range(cant_empleados-1-k):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux

print(sueldos)     """


# Crear y cargar en un lista los nombres de 5 países y en otra lista 
# paralela la cantidad de habitantes del mismo. Ordenar alfabéticamente e 
# imprimir los resultados. Por último ordenar con respecto a la cantidad de 
# habitantes (de mayor a menor) e imprimir nuevamente.


""" cap_inv = float(input("Ingrese capital:"))
gan = cap_inv * 0.02
print(gan) """

#========================================================
#============REPASO BUCLE WILE===========================
#========================================================

#Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe 
#cuántos tienen notas mayores o iguales a 7 y cuántos menores.

""" x=1
mayores_iguales_7 = 0
menores_7 = 0
while x<=10:
    nota = float(input(f"Ingrese nota {x}: "))
    if nota >= 7:
        mayores_iguales_7 = mayores_iguales_7 + 1
    else:
        menores_7 = menores_7 + 1
    x=x+1

print(f"Las notas mayores o iguales a 7 son: {mayores_iguales_7}")
print("==========================================")
print(f"Las notas mayores o iguales a 7 son: {menores_7}") """


# Se ingresan un conjunto de n alturas de personas por teclado. Mostrar 
# la altura promedio de las personas

""" suma = 0
cant_personas = int(input("Ingrese la cantidad de personas: "))
x=1
while x <= cant_personas:
    altura = float(input(f"Ingrese la altura de la persona {x}: "))
    suma = suma + altura
    x=x+1

print("La suma de las alturas es:")
print(suma)    
print(f"El promedio de las alturas es: {round((suma/cant_personas),2)}") """

# En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, 
# realizar un programa que lea los sueldos que cobra cada empleado e informe 
# cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. 
# Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.

""" def cargar_sueldos():
    sueldos = []
    cant_empleados = int(input("Ingrese cantidad de Empleados: "))
    for x in range(cant_empleados):
        sueldo = float(input(f"Ingrese sueldo del empleado {x+1}: "))
        sueldos.append(sueldo)
    return sueldos

def determinar_sueldos(sueldos):
    contador1 = 0
    contador2 = 0
    for x in range(len(sueldos)):
        if sueldos[x] >= 100 and sueldos[x] <= 300:
            contador1 = contador1 + 1
        else:
            contador2 = contador2 + 1    
    return contador1, contador2

def imprimir_resultados(contador1,contador2):
    print(f"La cantidad de sueldos que estan entre 100 y 300 son: {contador1}")
    print(f"La cantidad de sueldos mayores a 300 son : {contador2}")


sueldos = cargar_sueldos()
contador1,contador2 = determinar_sueldos(sueldos)
imprimir_resultados(contador1,contador2) """


#============================================
#============    SOLUCION IA  ===============
#============================================

""" def cargar_sueldos():
    sueldos = []
    cant_empleados = int(input("Ingrese cantidad de Empleados: "))
    for i in range(cant_empleados):
        while True:
            sueldo = float(input(f"Ingrese sueldo del empleado {i + 1}: "))
            if 100 <= sueldo <= 500:
                sueldos.append(sueldo)
                break
            else:
                print("El sueldo debe estar entre $100 y $500. Intente nuevamente.")
    return sueldos

def calcular_estadisticas(sueldos):
    empleados_100_a_300 = 0
    empleados_mas_300 = 0
    gasto_total = 0
    
    for sueldo in sueldos:
        gasto_total += sueldo
        if 100 <= sueldo <= 300:
            empleados_100_a_300 += 1
        else:
            empleados_mas_300 += 1
    
    return empleados_100_a_300, empleados_mas_300, gasto_total

def imprimir_resultados(empleados_100_a_300, empleados_mas_300, gasto_total):
    print(f"\nEmpleados que cobran entre $100 y $300: {empleados_100_a_300}")
    print(f"Empleados que cobran más de $300: {empleados_mas_300}")
    print(f"Gasto total en sueldos: ${gasto_total:.2f}")

# Ejecución principal
sueldos = cargar_sueldos()
empleados_100_a_300, empleados_mas_300, gasto_total = calcular_estadisticas(sueldos)
imprimir_resultados(empleados_100_a_300, empleados_mas_300, gasto_total) """

# Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc. 
# (No se ingresan valores por teclado)

""" numero = 11
for x in range(25):
    print(numero)
    numero = numero + 11  """

# Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 - 24, etc.

""" mult8=8
while mult8<=500:
    print(mult8)
    mult8=mult8+8 """

#Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un 
# mensaje cual de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", 
# "Lista 2 mayor", "Listas iguales")Tener en cuenta que puede haber dos o más estructuras 
# repetitivas en un algoritmo.