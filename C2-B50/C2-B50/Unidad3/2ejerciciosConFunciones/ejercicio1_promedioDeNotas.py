"""
Enunciado:
Leer n calificaciones (notas), calcular el promedio e indicar si está
aprobado o reprobado

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
"""
def leerN():
    return int(input("Cantidad de notas (n): "))
    #n=int(input("Cantidad de notas (n): "))
    #return n

def calcularPromedio():
    n=leerN()
    suma=0
    for i in range(n):
        nota=float(input("Ingresa nota: "))
        suma += nota
    return round(suma/n,1)

def mostrarSituacionFinal():
    promedio=calcularPromedio()
    situacion="Aprobado/a"
    if promedio<4.0:
        situacion="Reprobado/a"
    return promedio,situacion

# PP
#print("Tu promedio es:",calcularPromedio())
(promedio,situacion)=mostrarSituacionFinal()
print("Tu promedio es   :",promedio)
print("Situación final  :",situacion)
