Proceso sin_titulo
	Definir montoPesos,valorDolar,montoDolares,vuelto Como Entero
	// acá se está leyendo el monto en pesos a cambiar
	Escribir Sin Saltar "Monto en pesos a cambiar:"
	Leer montoPesos
	Escribir Sin Saltar "Valor del dólar de hoy:"
	Leer valorDolar
	montoDolares=TRUNC(montoPesos/valorDolar)
	vuelto=montoPesos-montoDolares*valorDolar
	Escribir "Monto en dólares: ",montoDolares
	Escribir "Vuelto: ",vuelto
FinProceso
