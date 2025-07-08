n=int(input("A cuántos estudiantes calcularás el promedio: "))
i=1
while i <= n:
    print("\nIngresa notas para el/la estudiante "+str(i))
    nota1=float(input("Ingresa nota 1: "))
    nota2=float(input("Ingresa nota 2: "))
    promedio=round((nota1+nota2)/2,1)
    print("Tu promedio es:",promedio)
    if promedio >= 4.0:
        print("Felicitaciones has aprobado")
    else:
        print("Lo lamento, has reprobado")
    i+=1 # i=i+1
