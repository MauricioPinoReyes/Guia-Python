Proceso sin_titulo
	Definir montoPesos,valorDolar,montoDolares,vuelto Como Entero
	// ac� se est� leyendo el monto en pesos a cambiar
	Escribir Sin Saltar "Monto en pesos a cambiar:"
	Leer montoPesos
	Escribir Sin Saltar "Valor del d�lar de hoy:"
	Leer valorDolar
	montoDolares=TRUNC(montoPesos/valorDolar)
	vuelto=montoPesos-montoDolares*valorDolar
	Escribir "Monto en d�lares: ",montoDolares
	Escribir "Vuelto: ",vuelto
FinProceso
