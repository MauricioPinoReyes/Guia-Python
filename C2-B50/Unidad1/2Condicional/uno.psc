Proceso sin_titulo
	// Se dará un 20% de descuento a las personas mayores
	// de edad y que residan en Maipú
	Definir precio,descuento,edad Como Entero
	Definir comuna Como Caracter
	Escribir Sin Saltar "Precio a pagar:"
	Leer precio
	Escribir Sin Saltar "Cuál es tu edad:"
	Leer edad
	Escribir Sin Saltar "Comuna donde vives:"
	Leer comuna
	descuento=0
	Si edad >= 65 Entonces
		Si comuna="Maipú" Entonces
			descuento=trunc(precio*0.2)
		FinSi
	FinSi
	
	
	
FinProceso
