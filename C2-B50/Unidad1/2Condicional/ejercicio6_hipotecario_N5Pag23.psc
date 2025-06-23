Proceso sin_titulo
	Definir sueldo,valorCasa,pie,valorCuota,saldo Como Entero
	Escribir Sin Saltar "Sueldo de la persona:"
	Leer sueldo
	Escribir Sin Saltar "Valor de la casa:"
	Leer valorCasa
	Si sueldo <= 500000 Entonces
		pie=trunc(valorCasa*0.15)
		saldo=valorCasa-pie
		valorCuota=trunc(saldo/120)		// 120 = 10 años x 12 meses
	SiNo
		pie=trunc(valorCasa*0.30)
		saldo=valorCasa-pie
		valorCuota=trunc(saldo/84)		//  84 = 7 años x 12 meses		
	FinSi
	Escribir "Pie a entregar: ",pie
	Escribir "Saldo por pagar: ",saldo
	Escribir "VAlor de la cuota: ",valorCuota
FinProceso
