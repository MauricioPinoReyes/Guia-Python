nota1=float(input("Ingresa nota 1: "))
nota2=float(input("Ingresa nota 2: "))
nota3=float(input("Ingresa nota 3: "))
promedio=round((nota1+nota2+nota3)/3,1)
print("Tu promedio es:",promedio)
if promedio >= 4.0:
    print("Felicitaciones has aprobado")
else:
    print("Lo lamento, has reprobado")


