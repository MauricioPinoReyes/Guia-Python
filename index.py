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


cap_inv = float(input("Ingrese capital:"))
gan = cap_inv * 0.02
print(gan)

