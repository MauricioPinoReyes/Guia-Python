Proceso sin_titulo
	Definir nota1,nota2,nota3,promedio Como Real
	Escribir Sin Saltar "Ingresa nota 1:"
	Leer nota1
	Escribir Sin Saltar "Ingresa nota 2:"
	Leer nota2
	Escribir Sin Saltar "Ingresa nota 3:"
	Leer nota3
	promedio=(nota1 + nota2 + nota3)/3
	Escribir "Tu promedio es: ",promedio	
	Si promedio < 3.5 Entonces
		Escribir "Reprobado"
	SiNo
		Si promedio < 4.0 Entonces
			Escribir "Pendiente"
		SiNo
			Escribir "Aprobado"
		FinSi
	FinSi
FinProceso
