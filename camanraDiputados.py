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

norte=sur=centro=0

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
    print("Zona Centro tiene mayor cantidad de votanes ")


#4)	Una persona que va de compras a la tienda “Enano, S.A.”, decide llevar un control 
# sobre lo que va comprando, para saber la cantidad de dinero que tendrá que pagar al 
# llegar a la caja. La tienda tiene una promoción del 20% de descuento sobre aquellos 
# artículos cuya etiqueta sea roja. Determinar la cantidad de dinero que esta persona deberá pagar

cantArticulos = int(input("Ingrese cantidad de articulos: "))
for x in range(cantArticulos):
    precio = float(input("Ingrese precio del articulo {x}: "))
    
