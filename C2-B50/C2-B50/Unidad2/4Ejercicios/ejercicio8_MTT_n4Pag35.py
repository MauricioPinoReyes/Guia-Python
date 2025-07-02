n=int(input("Cuántos vehículo cruzaron la frontera: "))
contaAuto=contaSW=contaJeep=contaCamion=contaMoto=0
for i in range(n):
    print("Ingresa 1=Auto, 2=SW, 3=Jeep, 4=Camión, 5=Moto")
    mensaje="Tipo Vehículo "+str(i+1)+": "
    # tipoVeh=int(input("Tipo Vehículo: "))
    tipoVeh=int(input(mensaje))
    if tipoVeh==1:
        contaAuto+=1
    elif tipoVeh==2:
        contaSW+=1
    elif tipoVeh==3:
        contaJeep+=1
    elif tipoVeh==4:
        contaCamion+=1
    else:
        contaMoto+=1
print("Cantidad de autos    :",contaAuto)
print("Cantidad de SW       :",contaSW)
print("Cantidad de Jeep     :",contaJeep)
print("Cantidad de camiones :",contaCamion)
print("Cantidad de motos    :",contaMoto)



