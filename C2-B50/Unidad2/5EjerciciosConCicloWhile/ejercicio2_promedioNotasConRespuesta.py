while True:
    nota1=float(input("Ingresa nota 1: "))
    nota2=float(input("Ingresa nota 2: "))
    promedio=round((nota1+nota2)/2,1)
    print("Tu promedio es:",promedio)
    if promedio >= 4.0:
        print("Felicitaciones has aprobado")
    else:
        print("Lo lamento, has reprobado")
    if input("Desesa calcular otro promedio (S/N): ").upper()=="N":
        break
    """
    respuesta=input("Desesa calcular otro promedio (S/N): ").upper()
    if respuesta=="N":
        break
    """