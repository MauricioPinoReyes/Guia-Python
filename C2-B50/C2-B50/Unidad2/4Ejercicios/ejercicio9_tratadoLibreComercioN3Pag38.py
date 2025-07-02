n=int(input("Cuántos Diputados votan: "))
contaAp=contaAb=contaRe=0
for i in range(n):
    print("Digita 1=Aprueba, 2=Rechaza 3=Abstiene")
    mensaje="Ingresa el voto (1,2,3): "+str(i+1)+": "
    tipoVoto=int(input(mensaje))
    if tipoVoto==1:
        contaAp+=1
    elif tipoVoto==2:
        contaRe+=1
    else:
        contaAb+=1
porApruebo=round(contaAp/n*100,2)
porRechazo=round(contaRe/n*100,2)
porAbstencion=100-porApruebo-porRechazo

