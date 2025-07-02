Proceso sin_titulo
	Definir valorNeumatico1,valorNeumatico2 Como Entero
	Definir cantidadNeumatico,valorPagar Como Entero
	Escribir Sin Saltar "Valor de neumático (menos de 5): "
	Leer valorNeumatico1
	Escribir Sin Saltar "Valor de neumático (mas de 5): "
	Leer valorNeumatico2
	Escribir Sin Saltar "Cuántos neumáticos vas comprar: "
	Leer cantidadNeumatico
	Si cantidadNeumatico < 5 Entonces
		valorPagar=cantidadNeumatico*valorNeumatico1
	SiNo
		valorPagar=cantidadNeumatico*valorNeumatico2
	FinSi	
FinProceso
