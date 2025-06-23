Proceso sin_titulo
	// Un negocio otroga un 20% de descuento a la
	// compra, si la persona es mayor de edad (>=65 años)
	Definir edad,montoCompra,descuento,totalPago Como Entero
	Escribir Sin Saltar "Ingresa el monto de la compra:"
	Leer montoCompra
	Escribir Sin Saltar "Cuál es tu edad:"
	Leer edad
	descuento=0
	Si edad >= 65 Entonces
		descuento=TRUNC(montoCompra*0.2)
	FinSi
	totalPago=montoCompra-descuento	
	Escribir "Tu descuento es: ",descuento
	Escribir "EL total a pagar es: ",totalPago
FinProceso
