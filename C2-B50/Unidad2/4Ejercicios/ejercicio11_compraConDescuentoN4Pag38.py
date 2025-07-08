n=int(input("Cuántas artículos compró la persona: "))
totalPago=0
for i in range(n):
    print("Artículo # "+str(i+1))
    precio=int(input("Precio del artículo: "))
    etiqueta=input("Etiqueta (B=Blanca, N=Negra): ").upper()
    if etiqueta=="N":
        totalPago+=int(precio*0.8)
    else:
        totalPago+=precio
print("El total a pagar es:",totalPago)

# HACER ESTE CICLO PARA VARIOS CLIENTES
# SUGERENCIA: INSERTAR OTRO CICLO DENTRO DE LOS ARTICULOS
