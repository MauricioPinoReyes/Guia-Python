#  PAG 20 ejercicio 5
#5)	Una persona desea saber cuánto dinero se genera por concepto de 
# intereses sobre la cantidad que tiene en inversión en el banco. 
# El decidirá reinvertir los intereses siempre y cuando estos excedan 
# a $7000, y en ese caso desea saber cuánto dinero tendrá finalmente en su cuenta.

dineroInvertido = float(input("Ingrese dinero invertido: "))

while True:
    if dineroInvertido > 0:
        break
    else:
        dineroInvertido = float(input("Debe ingresar un numero mayor a 0.Ingrese dinero invertido: ")) 


interes = float(input("Ingrese interes: "))
while True:
    if interes > 0:
        break
    else:
        interes = float(input("El interes debe ser mayor a 0.Ingrese interes: "))


totalCuenta = 0

if dineroInvertido > 7000:
    totalCuenta= (dineroInvertido * interes) + dineroInvertido
else:
    print("El dinero no se reinvertirá...")

print("El dinero total de la  cuenta es: ",totalCuenta)

