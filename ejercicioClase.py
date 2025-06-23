#3)	En la Cámara de Diputados se levanta una encuesta con todos los 
# integrantes con el fin de determinar qué porcentaje de los n diputados 
# está a favor del Tratado de Libre Comercio con EEUU, que porcentaje está 
# en contra y que porcentaje se abstiene de opinar

""" aFavor=enContra=abstencion=0
votos = int(input("Ingrese cantidad de votos: "))
for x in range(votos):
    print("Ingrese 1 A Favor, 2 En Contra, 3 Abstencion")
    voto = int(input("Ingrese voto: "))
    if voto == 1:
        aFavor+=1
    elif voto == 2:
        enContra+=1
    else:
        abstencion+=1

print(f"El total de votos es: {votos} ")
print(f"El porcentaje de votos a favor es: {(aFavor/votos)*100} ")
print(f"El porcentaje de votos en contra es: {(enContra/votos)*100} ")
print(f"El porcentaje de abstenciones es: {(abstencion/votos)*100} ") """


#6)	Un jefe zona desea determinar cuántas personas de cada una de las secciones 
# que componen su zona asisten el día de las votaciones. Las secciones son: norte, 
# sur y centro. También desea determinar cuál es la sección con mayor número de votantes  

#=================================================
#======SOLUCION 1 SIN CONSIDERAR IGUALDAD DE VOTOS
#=================================================
""" norte=sur=centro=0

cantPersonas = int(input("Ingrese cantidad de votantes: "))
for x in range(cantPersonas):
    print("Ingrese 1 Norte: 2 Sur, 3 Centro: ")
    voto = int(input("Ingrese voto: "))
    if voto == 1:
        norte+=1
    elif voto ==2:
        sur+=1
    else:
        centro+=1

if norte > sur and norte > centro:
    print("Zona norte tiene mayor cantidad de votanes ")
elif sur > norte and sur > centro:
    print("Zona Sur tiene mayor cantidad de votanes ")
else:
    print("Zona Centro tiene mayor cantidad de votanes ")

print(f"El total de personas es: {cantPersonas} ")
print(f"Votantes zona norte : {norte} ")
print(f"Votantes zona sur: {sur} ")
print(f"Votantes zona centro: {centro} ")

if norte > sur and norte > centro:
    print("Zona norte tiene mayor cantidad de votanes ")
elif sur > norte and sur > centro:
    print("Zona Sur tiene mayor cantidad de votanes ")
else:
    print("Zona Centro tiene mayor cantidad de votanes ") """




#=================================================
#======SOLUCION 2 CONSIDERANDO IGUALDAD DE VOTOS====
#=================================================

""" cantPersonas=int(input("Ingrese cantidad de votantes: "))
norte=sur=centro = 0  

for x in range(cantPersonas):
    print("Ingrese 1 Norte: 2 Sur, 3 Centro: ")
    voto = int(input("Ingrese voto: "))
    if voto == 1:
        norte += 1
    elif voto == 2:
        sur += 1
    else:
        centro += 1

print(f"\nEl total de personas es: {cantPersonas}")
print(f"Votantes zona norte: {norte}")
print(f"Votantes zona sur: {sur}")
print(f"Votantes zona centro: {centro}\n")


if norte==sur==centro:
    print("Hay un empate triple: todas las zonas tienen la misma cantidad de votantes")
elif norte == sur and norte > centro:
    print("Empate entre Norte y Sur como zonas con mayor cantidad de votantes")
elif norte == centro and norte > sur:
    print("Empate entre Norte y Centro como zonas con mayor cantidad de votantes")
elif sur == centro and sur > norte:
    print("Empate entre Sur y Centro como zonas con mayor cantidad de votantes")
elif norte > sur and norte > centro:
    print("Zona Norte tiene mayor cantidad de votantes")
elif sur > norte and sur > centro:
    print("Zona Sur tiene mayor cantidad de votantes")
else:
    print("Zona Centro tiene mayor cantidad de votantes") """


#4)	Una persona que va de compras a la tienda “Enano, S.A.”, decide llevar un control 
# sobre lo que va comprando, para saber la cantidad de dinero que tendrá que pagar al 
# llegar a la caja. La tienda tiene una promoción del 20% de descuento sobre aquellos 
# artículos cuya etiqueta sea roja. Determinar la cantidad de dinero que esta persona deberá pagar

# HACER ESTE CLICLO PARA VARIOS CLIENTES
# SUGERENCIA: INSERTAR OTRO CICLO DENTRO DE LOS ARTICULOS

precioTotal=0
cant_clientes = int(input("Ingrese cantidad de clientes: "))
for x in range(cant_clientes):
    cantArticulos = int(input("Ingrese cantidad de articulos: "))
    for x in range(cantArticulos):
        precio = float(input(f"Ingrese precio del articulo {x+1}: "))
        etiqueta = int(input("Etiqueta roja? 1 para si, 0 para no: "))
        if etiqueta == 1:
            precio = precio * 0.80
        precioTotal += precio

print(f"La cantidad de articulos ingresados es: {cantArticulos} ")
print(f"El precio total de la compra es: {precioTotal} ")





#=================================================
#======SOLUCION 1 INGRESANDO TOTAL DE ARTICULOS===
#=================================================

""" precioTotal=0
cantArticulos = int(input("Ingrese cantidad de articulos: "))
for x in range(cantArticulos):
    precio = float(input(f"Ingrese precio del articulo {x+1}: "))
    etiqueta = int(input("Etiqueta roja? 1 para si, 0 para no: "))
    if etiqueta == 1:
        precio = precio * 0.80
    precioTotal += precio

print(f"La cantidad de articulos ingresados es: {cantArticulos} ")
print(f"El precio total de la compra es: {precioTotal} ") """



#================================================================
#======SOLUCION 2 CON VALIDACION===
#=================================================================    

""" precioTotal=descuentoTotal= 0

cantArticulos = int(input("Ingrese cantidad de artículos: "))
while cantArticulos <= 0:
    print("Error: La cantidad debe ser mayor que 0.")
    cantArticulos = int(input("Ingrese cantidad de artículos: "))

for x in range(cantArticulos):
    precio = float(input(f"Ingrese precio del artículo {x+1}: "))
    while precio <= 0:
        print("Error: El precio debe ser positivo.")
        precio = float(input(f"Ingrese precio del artículo {x+1}: "))
    
    etiqueta = int(input("¿Etiqueta roja? 1 para sí, 0 para no: "))
    while etiqueta not in [0, 1]:
        print("Error: Ingrese 1 (sí) o 0 (no).")
        etiqueta = int(input("¿Etiqueta roja? 1 para sí, 0 para no: "))
    
    if etiqueta == 1:
        descuento = precio * 0.20
        precio = precio * 0.80
        descuentoTotal += descuento
    
    precioTotal += precio


precioTotalRedondeado = round(precioTotal, 2)
descuentoTotalRedondeado = round(descuentoTotal, 2)

print("\n--- Resumen de compra ---")
print(f"Cantidad de artículos: {cantArticulos}")
print(f"Precio total: ${precioTotalRedondeado}")
print(f"Ahorro por descuentos: ${descuentoTotalRedondeado}") """

""" precioTotal=0
bandera = True

while bandera==True:
    precio = int(input("Ingrese precio (0 para salir): "))
    etiqueta = int(input("Ingrese etiqueta (0 para salir): "))
    if precio == 0 or etiqueta == 0:
        #break
        bandera=False
    if etiqueta == 1:
        precio = precio * 0.80
    precioTotal += precio

#print(f"La cantidad de articulos ingresados es: {cantArticulos} ")
print(f"El precio total de la compra es: {precioTotal} ")  """   



#===============================================================
#=========================CICLO WHILE===========================
#===============================================================    

#SOLUCION 1 HECHA POR EL PROFE

""" n=int(input("A cuantos estudianes calcularas el promedio: "))
i=1
while i <= n:
    print("\nIngresa notas para el/la estudiente "+str(i))
    nota1=float(input("ingresa nota 1: "))
    nota2=float(input("ingresa nota 2: ")) """