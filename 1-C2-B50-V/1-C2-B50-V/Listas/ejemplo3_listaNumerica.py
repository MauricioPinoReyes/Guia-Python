"""
Normalmente las listas pasan por 5 procesos, sin embargo, esto es relativo
pues dependerá de la aplicación que uno construya
A lo anterior, se agrega el hecho de que Python tiene funciones especialmente
creadas para las listas

Veamos un ejemplo:
"""
# PASO 1: Definir el largo de la lista
n=int(input("Cuántas notas vas a ingresar?: "))

# PASO 2: Definir la lista con la cual se va a trabajar
notas=[]

# PASO 3: Leer o asignar valores a la lista (en este caso vamos a asignar)
for i in range(n):
    #calificacion=float(input("Ingresa nota: "))
    #notas.append(calificacion)
    notas.append(float(input("Ingresa nota: ")))
print("\nLas notas ingresadas son:",notas)

# PASO 4: Proceso sobre la lista, en este caso calcularemos el promedio
suma=0
for i in range(n):
    suma+=notas[i]  # suma = suma + notas[i]
promedio=round(suma/n,1)

# PASO 5: Entregar resultados
print("\nTu promedio es:",promedio)
