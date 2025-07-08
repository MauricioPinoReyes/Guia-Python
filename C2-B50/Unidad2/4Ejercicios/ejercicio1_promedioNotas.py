"""
Enunciado:
Leer n calificaciones (notas), calcular el promedio e indicar si está
aprobado o reprobado
"""
n=int(input("Cantidad de notas (n): "))
suma=0
for i in range(n):
    nota=float(input("Ingresa nota: "))
    suma += nota
promedio=round(suma/n,1)
print("Tu promedio es:",promedio)
if promedio >= 4.0:
    print("Felicitaciones, has aprobado")
else:
    print("Lo lamente, has reprobado")