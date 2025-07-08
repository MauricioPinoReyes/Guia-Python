nota1=float(input("Ingresa nota 1: "))
nota2=float(input("Ingresa nota 2: "))
nota3=float(input("Ingresa nota 3: "))
promedio=round((nota1+nota2+nota3)/3,1)
print("Tu promedio es:",promedio)
if promedio >= 4.0:
    print("Aprobado")
elif promedio < 3.5:
    print("Reprobado")
else:
    print("Pendiente")
"""
if promedio >= 4.0:
    print("Aprobado")
else:
    if promedio < 3.5:
        print("Reprobado")
    else:
        print("Pendiente")
"""