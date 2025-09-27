"""
Crear una lista de n posiciones con edades entre 0 y 120 de manera
aleatoria
Luego, buscar la edad mayor, la menor y calcular el promedio de edades
"""
import random
n=int(input("Cuántas edades quieres generar (n): "))
edades=[]

for i in range(n):
    edades.append(random.randint(0,120))

print("\nLas edades generadas son:",edades)
print("\nLa menor edad es:",min(edades))
print("\nLa mayor edad es:",max(edades))
print("\nEl promedio de edades es:",int(sum(edades)/n))

