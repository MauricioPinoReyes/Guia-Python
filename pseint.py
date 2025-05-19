# 	Problemas Secuenciales resueltos

#1) Suponga que una persona desea invertir su capital en 
#   el ”BancoEstado” y desea saber cuánto dinero ganará después 
#   de un mes si el banco paga a razón de 2% mensual.

""" cap_inv = float(input("Ingrese capital: "))
gan = cap_inv * 0.02
print(gan) """

# 2) Un vendedor recibe un sueldo base más un 10% extra por 
# comisión de sus ventas, el vendedor desea saber cuánto dinero 
# obtendrá por concepto de comisiones por las tres ventas que 
# realiza en el mes y el total que recibirá en el mes tomando 
# en cuenta su sueldo base y comisiones.

""" sueldo_base = float(input("ingrese sueldo Base: "))
venta1 = float(input("ingrese venta 1: "))
venta2 = float(input("ingrese venta 2: "))
venta3 = float(input("ingrese venta 3: "))

total_ventas = venta1 + venta2 + venta3
comision = total_ventas * 0.10
total_pagar = sueldo_base + comision
print("El sueldo a pagar es :")
print(total_pagar)
print("El total de las comisiones es: ")
print(comision) """

# 3) Una tienda ofrece un descuento del 15% sobre el total de la compra y 
# un cliente desea saber cuánto deberá pagar finalmente por su compra.

""" compra = float(input("Ingrese valor de la compra: "))
total_pagar = compra * 0.85
print("El total a pagar del cliente es: ")
print(total_pagar) """

# 4) Un alumno desea saber cuál será su calificación final en la materia 
#   de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
#	55% del promedio de sus tres calificaciones parciales.
#	30% de la calificación del examen final. 
#	15% de la calificación de un trabajo final.

""" nota1 = float(input("Ingrese nota 1:"))
nota2 = float(input("Ingrese nota 2:"))
nota3 = float(input("Ingrese nota 3:"))
promedio = (nota1+nota2+nota3)/3
nota_ex_final = float(input("Ingrese nota examen final:"))
nota_tr_final = float(input("Ingrese nota trabajo final:"))
nota_final = (promedio * 0.55) + (nota_ex_final * 0.30) + (nota_tr_final * 0.15)

print("Nota final: ")
print(nota_final)
 """

# 5) Un profesor desea saber qué porcentaje de hombres y que porcentaje de 
#   mujeres hay en un grupo de estudiantes.

""" hombres = float(input("Ingrese cantidad de hombres: "))
mujeres = float(input("Ingrese cantidad de mujeres: "))
total_alumnos = hombres + mujeres
porcentaje_hombres = (hombres/total_alumnos) * 100
porcentaje_mujeres = (mujeres/total_alumnos) * 100
print("El pocentaje de hombres es: ")
print(porcentaje_hombres)
print("El porcentaje de mujeres es: ")
print(porcentaje_mujeres) """

#====================== PENDIENTE =========================
# 6) Realizar un algoritmo que calcule la edad de una persona.
#====================== PENDIENTE =========================


# 1)Dada una cantidad en pesos, obtener la equivalencia en dólares.
""" VALOR_DOLAR = 900
pesos = float(input("Ingrese pesos: "))
dolares = pesos / VALOR_DOLAR
print(dolares) """


# 2) Leer un número y escribir el valor absoluto del mismo.
""" numero = float(input("Ingrese numero: ")) 
if numero < 0:
    numero * -1 

print("Valor absoluto sin formula: ")
print(numero)    

print("Valor absoluto con formula: ")
print(abs(numero)) """

# 3)Calcular el número de pulsaciones que una persona debe tener por cada 10 
# segundos de ejercicio, si la fórmula para las pulsaciones por minuto es:
#     num. pulsaciones = (220 - edad)/10

""" edad = float(input("Ingrese edad: "))
num_pulsaciones = (220 - edad)/10
print("El numero de pulsaciones por minuto es: ")
print(num_pulsaciones) """

# 4) Calcular el nuevo sueldo de un empleado fiscal si obtuvo un reajuste 
#  del 4,5% sobre su sueldo anterior.

""" REAJUSTE = 0.045
sueldo_anterior = float(input("Ingrese sueldo: "))
sueldo_actual = (sueldo_anterior * REAJUSTE) + sueldo_anterior
print("El sueldo actual es de : ")
print(sueldo_actual) """

# 5) En un hospital rural existen tres áreas: Ginecología, Pediatría, Traumatología. 
#    El presupuesto anual del hospital se reparte conforme a la siguiente tabla:
#  
#            Área			Porcentaje del presupuesto
#			Ginecología			    40%
#			Traumatología		    30%
#			Pediatría			    30%
#
# Obtener la cantidad de dinero que recibirá cada área, para cualquier monto 
# presupuestal, que el Gobierno tiene destinado para este año.
""" PRE_GINECOLOGIA = 0.40
PRE_TRAUMATOLOGIA = 0.30
PRE_PEDIATRIA = 0.30

presupuesto = float(input("Ingrese presupuesto: "))
ginecologia = presupuesto * PRE_GINECOLOGIA
traumatologia = presupuesto * PRE_TRAUMATOLOGIA
pedriatria = presupuesto * PRE_PEDIATRIA
print("El presupusto de Ginecologia es: ")
print(ginecologia)
print("El presupuesto de Traumatologia es: ")
print(traumatologia)
print("El presupuesto de Pediatria es: ")
print(pedriatria) """


# 6) El dueño de una tienda compra un artículo a un precio determinado. 
#    Obtener el precio en que lo debe vender para obtener una ganancia del 32%.
""" CONST_GANANCIA = 1.32
precio_compra = float(input("Ingrese precio de compra: "))
precio_venta = precio_compra * CONST_GANANCIA
print("El precio de venta es de :")
print(precio_venta) """

# 7) Todos los lunes, miércoles y viernes, una persona corre la misma ruta y cronometra 
#  los tiempos obtenidos. Determinar el tiempo promedio que la persona tarda en 
#  recorrer la ruta en una semana cualquiera.

""" lunes = float(input("Ingrese tiempo lunes: "))
miercoles = float(input("Ingrese tiempo miercoles: "))
viernes = float(input("Ingrese tiempo viernes: "))

tiempo_promedio = (lunes+miercoles+viernes)/3
print("El tiempo promedio recorrido es: ")
print(tiempo_promedio) """

# 8) Tres personas deciden invertir su dinero para fundar una empresa. 
#   Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje 
#   que cada quien invierte con respecto a la cantidad total invertida.

""" inv_persona1 = float(input("Ingrese cantidad invertida: "))
inv_persona2 = float(input("Ingrese cantidad invertida: "))
inv_persona3 = float(input("Ingrese cantidad invertida: "))
total_inversion = inv_persona1+inv_persona2+inv_persona3
por_inv_per_1 =(inv_persona1/total_inversion)*100
por_inv_per_2 =(inv_persona2/total_inversion)*100
por_inv_per_3 =(inv_persona3/total_inversion)*100

print("El porcentaje de inversion de la persona 1 es: ")
print(por_inv_per_1)
print("El porcentaje de inversion de la persona 2 es: ")
print(por_inv_per_2)
print("El porcentaje de inversion de la persona 3 es: ")
print(por_inv_per_3) """

# ==========================================================
# ========== ESTRUCTURAS DE CONDICIONALES ==================
# ==========================================================

# 1) Un hombre desea saber cuánto dinero se genera por concepto de intereses 
# sobre la cantidad que tiene invertida en el banco. El decidirá reinvertir los 
# intereses siempre y cuando estos excedan a $7.000, y en ese caso desea saber 
# cuánto dinero tendrá finalmente en su cuenta.

""" capital = float(input("Ingrese capital: "))
pocentaje_interes = float(input("Ingrese porcentaje de interes: "))
interes = capital*pocentaje_interes
if interes > 7000:
    capital_final = capital + interes
    print("El capital final es: ")
    print(capital_final)
else:
    print("EL dinero no sera invertido")
 """
# 2) Determinar si un alumno aprueba, queda pendiente o reprueba una asignatura, 
# considerando que aprobará si su promedio es igual o superior a la nota 4.0, queda 
# pendiente cuando su nota está entre un 3.5 y 3.9 (ambas inclusive) y reprueba en 
# caso de obtener nota inferior a 3.5.

""" promedio = float(input("Ingrese promedio: "))
if promedio >= 4:
    print("Aprobado")
elif promedio < 3.5:
    print("Reprobado")
else:
    print("Pendiente")
 """

#3) En un almacén se hace un 20% de descuento a los clientes cuya compra 
# supere los $7.500  ¿Cuál será la cantidad que pagará una persona por su compra?

""" compra = float(input("Ingrese compra: "))

if compra > 7500:
    descuento = compra * 0.20
else:
    descuento = 0

total_compra = compra - descuento    
print("El total de la compra es: ")
print(total_compra) """

# 4) Una persona necesita calcular su sueldo semanal, el cual se 
#   obtiene de la siguiente manera:
#  	    
#     Si trabaja 40 horas o menos se le paga $5.000 por hora
#  	    
#     Si trabaja más de 40 horas se le paga $5.000 por cada una de las 
#     primeras 40 horas y $7.500 por cada hora extra.

""" horas = int(input("Ingrese cantidad de horas: "))
if horas > 40:
    horas_extra = (horas - 40) * 7500
    sueldo = 40*5000 + horas_extra
    print("El sueldo es: ")
    print(sueldo)
else:
    sueldo = horas * 5000
    print("El sueldo es: ")
    print(sueldo) """


#==================================================
#====================REPETIDO======================
#==================================================

# 5) Una persona desea saber cuánto dinero se genera por concepto de intereses sobre la 
# cantidad que tiene en inversión en el banco. El decidirá reinvertir los intereses 
# siempre y cuando estos excedan a $7000, y en ese caso desea saber cuánto dinero 
# tendrá finalmente en su cuenta.

#6)	Escriba un algoritmo que lea dos números e imprímalos en forma ascendente

""" numero1 = int(input("Ingrese el primer numero:"))
numero2 = int(input("Ingrese el segundo numero:"))
if (numero1 < numero2):
    print(str(numero1) + " " + str(numero2))
else:
    print(str(numero2) + " " + str(numero1)) """


# 7) Una persona enferma, que pesa 70 kg, se encuentra en reposo y desea saber 
#    cuántas calorías consume su cuerpo durante todo el tiempo que realice una 
#    misma actividad. Las actividades que tiene permitido realizar son únicamente 
#    dormir o estar sentado en reposo. Los datos que tiene son que estando dormido 
#    consume 1.08 calorías por minuto y estando sentado en reposo consume 1.66 calorías
#    por minuto. 

""" actividad = input("Ingrese actividad: ")
minutos = int(input("Ingrese cantidad de minutos: "))
calorias_consumidas = 0

if actividad == "sentado":
    calorias_consumidas = minutos * 1.66
elif actividad == "dormido":
     alorias_consumidas = minutos * 1.08

print(calorias_consumidas)    """     


# 8) Escribir un algoritmo que despliegue el nombre de un artículo, clave, 
#  precio original y su precio con descuento. El descuento lo hace en base a 
# la clave, si la clave es 01 el descuento es del 10% y si la clave es 02 el 
# descuento en del 20% (solo existen dos claves).

""" nombre_articulo = input("Ingrese nombre: ")
clave = input("Ingrese clave: ")
precio_original = float(input("Ingrese precio original: "))


if clave == "01":
    porcentaje_descuento = 0.10
elif clave == "02":
    porcentaje_descuento = 0.20
else:
    print("Clave no válida. No se aplicará descuento.")
    porcentaje_descuento = 0

precio_descuento = precio_original * (1 - porcentaje_descuento)

print(
    f"Nombre Artículo: {nombre_articulo} - Clave: {clave} - "
    f"Precio Original: {precio_original:.2f} - "
    f"Precio con Descuento: {precio_descuento:.2f}"
) """


# 9) Hacer un algoritmo que calcule el total a pagar por la compra de camisas. 
#  Si se compran tres camisas o más se aplica un descuento del 20% sobre el 
#  total de la compra y si son menos de tres camisas un descuento del 10%

""" numero_camisas = int(input("Ingrese número de camisas: "))
precio = float(input("Ingrese precio de la camisa: "))
if numero_camisas >=3:
    precio_final = numero_camisas * (precio * (1-0.20))
else:
    precio_final = numero_camisas * (precio * (1-0.10))
print(f"Total a pagar: {precio_final}") """

# 10) Una empresa quiere hacer una compra “rayos de bicicleta” a una fábrica de 
#     bicicletas. La empresa, dependiendo del monto total de la compra, decidirá 
#     qué hacer para pagar al fabricante.
#  • Si el monto total de la compra excede de $500 000 la empresa tendrá la 
#    capacidad de invertir de su propio dinero un 55% del monto de la compra, 
#    pedir prestado al banco un 30% y el resto lo pagará solicitando un crédito 
#    al fabricante.
#  • Si el monto total de la compra no excede de $500 000 la empresa tendrá capacidad 
#    de invertir de su propio dinero un 70% y el restante 30% lo pagará solicitando 
#    crédito al fabricante.
#  • El fabricante cobra por concepto de intereses un 20% sobre la cantidad que 
#    se le pague a crédito.
#  • El algoritmo debe entregar la cantidad que la empresa debe invertir, el 
#    monto del préstamo bancario, el crédito que otorgará el proveedor y el interés 
#    que éste cobrará.

costo_pieza = float(input("Ingrese el costo por pieza: "))
numero_piezas = int(input("Ingrese la cantidad de piezas: "))
monto_compra = costo_pieza * numero_piezas

if monto_compra > 500000:
    monto_a_invertir = monto_compra * 0.55
    prestamo_bancario = monto_compra * 0.30
    
else:
    monto_a_invertir = monto_compra * 0.70
    prestamo_bancario = 0
    
credito_fabricante = monto_compra - (monto_a_invertir + prestamo_bancario)
interes_fabricante = credito_fabricante * 0.20

print(f"""
---------------------------------
Monto a Invertir: ${monto_a_invertir:.2f}
Préstamo Bancario: ${prestamo_bancario:.2f}
Crédito Fabricante: ${credito_fabricante:.2f}
Intereses Fabricante: ${interes_fabricante:.2f}
---------------------------------
""")