n=int(input("Cuántas personas votan: "))
contaNorte=contaSur=contaCentro=0
for i in range(n):
    print("Digita 1=Norte, 2=Sur 3=Centro")
    mensaje="Ingresa la zona (1,2,3): "+str(i+1)+": "
    zona=int(input(mensaje))
    if zona==1:
        contaNorte+=1
    elif zona==2:
        contaSur+=1
    else:
        contaCentro+=1
print("La cantidad de votos de La Zona Norte    :",contaNorte)
print("La cantidad de votos de La Zona Sur      :",contaSur)
print("La cantidad de votos de La Zona Centro   :",contaCentro)
if  contaNorte>contaSur and contaNorte>contaCentro:
    print("La Zona Norte fue la más votada")
elif contaSur>contaNorte and contaSur>contaCentro:
    print("La Zona Sur fue la más votada")
else:
    print("La Zona Centro fue la más votada")