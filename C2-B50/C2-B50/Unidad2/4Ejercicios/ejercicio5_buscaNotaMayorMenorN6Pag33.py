n=int(input("Cuántas notas vas a ingresar (n): "))
suma=alta=0
baja=8
for i in range(n):
    mensaje="Ingresa nota "+str(i+1)+": "
    #calif=float(input("Ingresa nota: "))
    calif=float(input(mensaje))
    suma+=calif
    if calif<baja:
        baja=calif
    if calif>alta:
        alta=calif
promedio=round(suma/n,1)
print("Tu promedio es           :",promedio)
print("Calificación más baja    :",baja)
print("Calificación más alta    :",alta)
