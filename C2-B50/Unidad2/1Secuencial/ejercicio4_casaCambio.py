montoPesos=int(input("Monto en pesos a cambiar: "))
valorDolar=int(input("Valor del dolar de hoy: "))
montoDolares=int(montoPesos/valorDolar)
vuelto=montoPesos-montoDolares*valorDolar
print("Monto en dólares:",montoDolares)
print("Vuelto:",vuelto)

