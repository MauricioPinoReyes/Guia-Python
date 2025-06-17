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

""" costo_pieza = float(input("Ingrese el costo por pieza: "))
numero_piezas = int(input("Ingrese la cantidad de piezas: "))
monto_compra = costo_pieza * numero_piezas

if monto_compra > 500000:
    monto_a_invertir = monto_compra * 0.55
    prestamo_bancario = monto_compra * 0.30
    
else:
    monto_a_invertir = monto_compra * 0.70
    prestamo_bancario = 0
    
credito_fabricante = monto_compra - (monto_a_invertir + prestamo_bancario)
interes_fabricante = credito_fabricante * 0.20 """

#print(f"""
#---------------------------------
#Monto a Invertir: ${monto_a_invertir:.2f}
#Préstamo Bancario: ${prestamo_bancario:.2f}
#Crédito Fabricante: ${credito_fabricante:.2f}
#Intereses Fabricante: ${interes_fabricante:.2f}
#---------------------------------
#""")

#==============================================================
#====================PROBLEMAS PROPUESTOS PAG 23===============
#==============================================================

# 1) Calcular el total que una persona debe pagar por la compra de 
# neumáticos en un supermercado, si el precio de cada neumático es 
# de $64.500 si se compran menos de 5 neumáticos y de $51.200 si se compran 5 o más.

""" cant_neumaticos = int(input("Ingrese cantidad de neumaticos: "))


if cant_neumaticos < 5:
    precio_compra = cant_neumaticos * 64500
else:
    precio_compra = cant_neumaticos * 51200

print("El total de la compra es: ")
print(precio_compra)    """     



""" # Constantes para precios y umbral de descuento
PRECIO_NORMAL = 64500
PRECIO_DESCUENTO = 51200
CANTIDAD_MINIMA_DESCUENTO = 5

try:
    # Entrada de datos con validación
    cantidad_neumaticos = int(input("Ingrese la cantidad de neumáticos: "))
    
    if cantidad_neumaticos < 0:
        print("Error: La cantidad no puede ser negativa")
    else:
        # Cálculo del precio según cantidad
        if cantidad_neumaticos >= CANTIDAD_MINIMA_DESCUENTO:
            precio_unitario = PRECIO_DESCUENTO
            total = cantidad_neumaticos * PRECIO_DESCUENTO
        else:
            precio_unitario = PRECIO_NORMAL
            total = cantidad_neumaticos * PRECIO_NORMAL
        
        # Mostrar resultados formateados
        print("\nDetalle de la compra:")
        print(f"- Cantidad de neumáticos: {cantidad_neumaticos}")
        print(f"- Precio unitario aplicado: ${precio_unitario:,.2f}")
        print(f"- Total a pagar: ${total:,.2f}")

except ValueError:
    print("Error: Debe ingresar un número entero válido") """

# 2)En un supermercado se hace una promoción, mediante la cual el cliente 
# obtiene un descuento dependiendo de un número que se escoge al azar. 
# Si el número escogido es menor que 74 el descuento es del 15% sobre el 
# total de la compra, si es mayor o igual a 74 el descuento es del 20%.  
# Obtener cuánto dinero se le descuenta.

# numero al azar - descuento - total_compra 

""" import random

numero_azar = random.randint(1,100)
total_compra = float(input("Ingrese el total de la compra: "))
if numero_azar < 74:
    descuento = total_compra * 0.15
else:
    descuento = total_compra * 0.20
print(f"El numero al azar es: {numero_azar}")
print("====================")
print("El descuento de la compra es: ")
print(descuento)
print("=================")
print("El total de la compra es:")
print(total_compra)
print("=================")
print("El total a pagar es: ")
print(total_compra-descuento) """

#=============================
#=======VERSION IA============
#=============================
""" import random

# Generar número aleatorio
numero_azar = random.randint(1, 100)

# Pedir total de la compra (con validación)
while True:
    try:
        total_compra = float(input("Ingrese el total de la compra: $"))
        if total_compra >= 0:
            break
        else:
            print("Error: Ingrese un monto positivo.")
    except ValueError:
        print("Error: Ingrese un número válido.")

# Calcular descuento
if numero_azar < 74:
    descuento = total_compra * 0.15
    porcentaje = "15%"
else:
    descuento = total_compra * 0.20
    porcentaje = "20%"

# Mostrar resultados
print("\n" + "=" * 30)
print(f"Número aleatorio: {numero_azar} → Descuento: {porcentaje}")
print(f"Total compra: ${total_compra:.2f}")
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Total a pagar: ${(total_compra - descuento):.2f}")
print("=" * 30) """


# 3)Calcular el número de pulsaciones que debe tener una persona por 
#  cada 10 segundos de ejercicio aeróbico; la fórmula que se aplica 
# cuando el sexo es femenino es: 
#             num. pulsaciones = (220 - edad)/10
#              y si el sexo es masculino:
#		      num. pulsaciones = (210 - edad)/10


""" print("Ingrese sexo de la persona")
numero = int(input("1 Para masculino, 2 para femenino: "))
edad = int(input("Ingrese edad de la persona: "))
if numero == 1:
    numero_pulsaciones = (220 - edad)/10
elif numero == 2:
    numero_pulsaciones = (210 - edad)/10    

print(f"El número de pulsaciones es de : {numero_pulsaciones} ")
 """

""" CONSULTAR AL PROFESOR SOBRE QUE DEBERIA PSAR SI EL MONTO ES 50.999 (PROBLEMAS DE HUMBRAL)"""

# 4) El “Banco Ahorre Aquí” para su departamento de inversiones estableció 
# un programa para captar clientes, que consiste en lo siguiente: Si el monto 
# a invertir el cliente es menor que $50.999 la comisión que cobrará el banco
# será del 1% del monto invertido, y si el monto a invertir es mayor que $50.999 
# la comisión que cobrará el banco será del 0.3% del monto invertido. El banco 
# desea determinar cuál será la comisión que debe pagar un cliente.

""" monto_invertir = float(input("Ingrese monto a invertir: "))
if monto_invertir < 50999:
    comision = monto_invertir * 0.001
else:
    comision = monto_invertir * 0.003

print("La comision a pagar es: ")
print(comision) """


""" CONSULTAR AL PROFESOR SOBRE QUE DEBERIA PSAR SI EL MONTO ES 500.000 (PROBLEMAS DE HUMBRAL)"""

# 5) El Ministerio de Vivienda y Urbanismo ofrece casas de interés social, bajo 
# las siguientes condiciones: Si los ingresos del postulante son de $500.000 o 
# menos el pie de la casa será del 15% del costo de la casa y el resto se 
# distribuirá en pagos mensuales, a pagar en diez años. Si los ingresos del 
# postulante son de $500.000 o más el pie será del 30% del costo de la casa y 
# el resto se distribuirá en pagos mensuales a pagar en 7 años.
# El Ministerio quiere obtener cuanto deberá pagar un postulante por concepto 
# de pie de la casa y cuanto por cada pago mensual.

#ingresos_postulante - pie_casa - costo_casa - pago_mensual

""" ingresos_postulante = float(input("Ingrese los ingresos del postulante: "))
costo_casa = float(input("Ingrese el costo de la casa: "))
if ingresos_postulante <=500000:
    pie_casa = costo_casa * 0,15
else:
    pie_casa = costo_casa * 0,30 """


# 6) Como un nuevo plan de austeridad el gobierno ha establecido el programa 
# SARV (Sistema de Ahorro para el Retiro Voluntario) que consiste en que los 
# dueños de la empresa deben obligatoriamente depositar en una cuenta bancaria 
# un porcentaje del sueldo de los trabajadores; adicionalmente los trabajadores 
# pueden solicitar a la empresa que deposite directamente una cuota fija o un 
# porcentaje de su sueldo en la cuenta del SARV, la cual le será descontada de su pago.
# Un/a trabajador/a que ha decidido aportar a su cuenta del SARV desea saber la cantidad
# total de dinero que estará depositado a esa cuenta cada mes, y el pago mensual que recibirá.


#==============================================
#=============SEGUIR CON CICLOS PAG 31=========
#==============================================

# 1) Calcular el promedio de un alumno que tiene n calificaciones en la 
# asignatura de Introducción a la Programación.

""" suma = 0

cantidad_calificaciones = int(input("Ingrese cantidad de calificaciones: "))
x=1
while x < cantidad_calificaciones:
    calificacion = float(input(f"Ingrese calificacion {x}: "))
    suma = suma + calificacion
    x=x+1

print("El promedio del alumno es: ")
print(suma/cantidad_calificaciones) """


#2) Leer n números y obtener su cubo y su cuarta.
 

""" def cargar_numeros():
    numeros = []
    cant_numeros = int(input("Ingrese cantidad de números: "))
    for x in range(cant_numeros):
        numero = int(input("Ingrese número: "))
        numeros.append(numero)
    return numeros

def elevar_al_cubo_cuarta(numeros):
    cubos = []
    cuartas = []
    for x in range(len(numeros)):
        cubo = numeros[x]**3
        cubos.append(cubo)
        cuarta = numeros[x]**4
        cuartas.append(cuarta)
    return cubos, cuartas


def imprimir_resultados(cubos,cuartas):
    print("Números al cubo: ")
    print(cubos)
    print("Números a la cuarta: ")
    print(cuartas)

numeros = cargar_numeros()
cubos,cuartas = elevar_al_cubo_cuarta(numeros)
imprimir_resultados(cubos,cuartas) """
    

#==============================================
#=============CODIGO IA================
#==============================================

""" def cargar_numeros():
    numeros = []
    try:
        cant_numeros = int(input("Ingrese cantidad de números: "))
        for i in range(cant_numeros):
            while True:
                try:
                    numero = float(input(f"Ingrese el número {i + 1}: "))
                    numeros.append(numero)
                    break
                except ValueError:
                    print("¡Error! Ingrese un número válido.")
        return numeros
    except ValueError:
        print("¡Error! La cantidad debe ser un número entero.")
        return []

def calcular_potencias(numeros):
    numeros_al_cubo = [numero ** 3 for numero in numeros]
    numeros_a_la_cuarta = [numero ** 4 for numero in numeros]
    return numeros_al_cubo, numeros_a_la_cuarta

def imprimir_resultados(numeros, cubos, cuartas):
    print("\nResultados:")
    print("Número\tCubo\tCuarta")
    print("-" * 25)
    for num, cubo, cuarta in zip(numeros, cubos, cuartas):
        print(f"{num:.2f}\t{cubo:.2f}\t{cuarta:.2f}")

# Ejecución principal
numeros = cargar_numeros()
if numeros:  # Solo continuar si se ingresaron números válidos
    cubos, cuartas = calcular_potencias(numeros)
    imprimir_resultados(numeros, cubos, cuartas) """


#3) Leer n números e imprimir solamente los números positivos

#===Solucion 1
""" cant_numeros = int(input("Ingrese cantidad de números: "))

for _ in range(cant_numeros):
    numero = int(input("Ingrese número: "))
    if numero > 0:
        print(numero) """
       

#===Solucion 2
""" def cargar_numeros():
    numeros = []
    cant_numeros = int(input("Ingrese cantidad de números: "))
    for _ in range(cant_numeros):
        numero = int(input("Ingrese número: "))
        numeros.append(numero)
    return numeros

def imprimir_positivos(numeros):
    for numero in numeros:
        if numero > 0:
            print(numero)   


numeros = cargar_numeros()
imprimir_positivos(numeros) """

# 4)Leer n números e imprimir cuantos son positivos, cuantos negativos y cuantos neutros.


""" def cargar_numeros():
    numeros = []
    cant_numeros = int(input("Ingrese cantidad de números: "))
    for _ in range(cant_numeros):
        numero = int(input("Ingrese número: "))
        numeros.append(numero)
    return numeros

def determinar_numeros(numeros):
    cont1=0
    cont2=0
    cont3=0
    for numero in numeros:
        if numero > 0:
            cont1 += 1
        elif numero < 0:
            cont2 +=1
        else:
            cont3 +=1        
    return cont1,cont2,cont3

def imprimir_resultados(cont1,cont2,cont3):
    print(f"La cantidad de números positivos es: {cont1}")
    print(f"La cantidad de números negativos es: {cont2}")
    print(f"La cantidad de números neutros es: {cont3}")

numeros = cargar_numeros()
positivos,negativos,neutros = determinar_numeros(numeros)
imprimir_resultados(positivos,negativos,neutros) """


# 5) Leer n números negativos y convertirlos a positivos e imprimir dichos números.

#===Solucion 1

""" cant_numeros = int(input("Ingrese cantidad de números negativos: "))

for x in range(cant_numeros):
        numero_negativo = int(input("Ingrese número negativo: "))
        numero_positivo = numero_negativo * -1
        print(numero_positivo) """


#===Solucion 2
""" def cargar_numeros_negativos():
    numeros_negativos = []
    cant_numeros = int(input("Ingrese cantidad de números: "))
    for _ in range(cant_numeros):
        numero_negativo = int(input("Ingrese número negativo: "))
        numeros_negativos.append(numero_negativo)
    return numeros_negativos

def cambiar_a_positivos(numeros_negativos):
    numeros_positivos = []
    for numero in numeros_negativos:
        numero_positivo = numero * -1
        numeros_positivos.append(numero_positivo)
    return numeros_positivos    


numeros_negativos = cargar_numeros_negativos()
print("=======cambio a positivo============")
numeros_positivos = cambiar_a_positivos(numeros_negativos)
print(numeros_positivos) """


# 6) Suponga que se tiene un conjunto de calificaciones de un grupo de n alumnos. 
# Realizar un algoritmo para calcular la calificación promedio y la calificación 
# más baja de todo el grupo.

#===Solucion 1
""" calificaciones = [6,7,4,5,2,7,6,1,3,2]
suma = 0
calificacion_menor = calificaciones[0]

for x in range(1,len(calificaciones)):
    if calificaciones[x] < calificacion_menor:
         calificacion_menor = calificaciones[x]

for x in range(len(calificaciones)):
    suma += calificaciones[x]
            
print("El promedio es: ")
print(suma/len(calificaciones))
print("La calificasion menor es: ")
print(calificacion_menor) """

#===Solucion 2

""" n=int(input("Ingrese cantidad de calificaciones: "))
suma=0
baja=8
for x in range(n):
    calif=float(input("Ingrese calificacion: "))
    suma+=calif
    if calif<baja:
        baja=calif

print(f"El promedio de las calificaciones es: {suma/n}")
print(f"La calificacion más baja es: {baja}") """


# 7) Calcular e imprimir la tabla de multiplicar de un número cualquiera. 
# Imprimir el multiplicando, el multiplicador y el producto. 

""" multiplicando = int(input("Ingrese tabla: "))
for multiplicador in range(1,11):
    producto = multiplicando * multiplicador
    print(f"{multiplicando} x {multiplicador} = {producto}") """

#===Solucion 2


#=================================================
#=======PROBLEMAS PROPUESTOS PAG 34===============
#=================================================

#1)	Simular el comportamiento de un reloj digital, imprimiendo la hora, 
# minutos y segundos de un día desde las 0:00:00 horas hasta las 23:59:59 horas

for h in range(24):
    for m in range(60):
        for s in range(60):
            print(h,":",m,":",s)
