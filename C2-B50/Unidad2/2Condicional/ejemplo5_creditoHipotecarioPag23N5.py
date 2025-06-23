precioCasa=int(input("Cuál es el precio de la casa: "))
sueldo=int(input("Cuál es el sueldo della trabajador/a: "))
if sueldo <= 500000:
    pie=int(precioCasa*0.15)
    cuota=int((precioCasa-pie)/120)
else:
    pie=int(precioCasa*0.30)
    cuota=int((precioCasa-pie)/84)
print("El PIE a entregar es:",pie)
print("La cuota mensual es de:",cuota)
