"""
Enunciado:
Leer n calificaciones (notas), calcular el promedio e indicar si está
aprobado o reprobado
"""
""" n=int(input("Cantidad de notas (n): "))
suma=0
for i in range(n):
    nota=float(input("Ingresa nota: "))
    suma += nota
promedio=round(suma/n,1)
print("Tu promedio es:",promedio)
if promedio >= 4.0:
    print("Felicitaciones, has aprobado")
else:
    print("Lo lamente, has reprobado") """

def leerN():
    while True:
        cantNotas=int(input("Ingrese cantidad de notas : "))
        if cantNotas > 0 :
            return cantNotas
        else:
            print("El número debe ser mayor a 0")
    

def calcularPromedio():
    n=leerN()
    suma=0
    for _ in range(n):
        while True:
            nota=float(input("Ingresa nota: "))
            if nota >= 1.0 and nota <= 7.0:
                suma += nota
                break
            else:
                print("Nota fuera de rango: ")
            
    return round(suma/n,1)

def mostrarSituacionFinal():
    promedio=calcularPromedio()
    situacion="Aprobado/a"
    if promedio < 4.0:
        situacion="Reprobado/a"
    else:
        situacion
    return situacion, promedio
#PP


print("=====================")
situacion, promedio = mostrarSituacionFinal()
print("Tu situacion es: ",situacion)
print("Tu promedio es: ",promedio)
