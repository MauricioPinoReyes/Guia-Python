montoCompra=int(input("Ingresa monto de la compra: "))
edad=int(input("Cuál es tu edad: "))
descuento=0
if edad >= 65:
    descuento=int(montoCompra*0.2)
totalPago=montoCompra-descuento
print("Tu descuento es:",descuento)
print("El total a pagar es:",totalPago)
