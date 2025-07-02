"""
import sys
print(sys.maxsize)
# 9223372036854775807
"""
n=int(input("Cuántos índices de camiones ingresará: "))
# Leyendo el índice del 1er camión para tomarlo como referencia
indice=float(input("Indice del camión 1: "))
mayor=menor=indice  # se asume que el 1er índice es el mayor y el menor
# for i in range(n-1):
for i in range(1,n):
    indice=float(input("Indice del camión: "))
    if indice > mayor:
        mayor=indice
    if indice < menor:
        menor=indice
print("\nReporte Final")
print("El camión que más contaminó es con   :",mayor)
print("El camión que menos contaminó es con :",menor)



