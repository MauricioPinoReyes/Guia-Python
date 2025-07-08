numHa=int(input("Cantidad de hectáreas a reforestar: "))
numMt2=numHa*10000
if numMt2 <= 1000000:
    porPinos=50
    porOyamel=30
    porCedros=20
else:
    porPinos=70
    porOyamel=20
    porCedros=10
mt2Pinos=int(numMt2*porPinos/100)
mt2Oyamel=int(numMt2*porOyamel/100)
mt2Cedros=int(numMt2*porCedros/100)
cantidadPinos=round(mt2Pinos/10*8,0)
cantidadOyamel=round(mt2Oyamel/15*15,0)
cantidadCedros=round(mt2Cedros/18*10,0)
print("Cantidad de PINOS    :",cantidadPinos)
print("Cantidad de OYAMEL   :",cantidadOyamel)
print("Cantidad de CEDROS   :",cantidadCedros)
