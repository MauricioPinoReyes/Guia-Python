Proceso sin_titulo
	Definir valorNeumatico1,valorNeumatico2 Como Entero
	Definir cantidadNeumatico,valorPagar Como Entero
	Escribir Sin Saltar "Valor de neum�tico (menos de 5): "
	Leer valorNeumatico1
	Escribir Sin Saltar "Valor de neum�tico (mas de 5): "
	Leer valorNeumatico2
	Escribir Sin Saltar "Cu�ntos neum�ticos vas comprar: "
	Leer cantidadNeumatico
	Si cantidadNeumatico < 5 Entonces
		valorPagar=cantidadNeumatico*valorNeumatico1
	SiNo
		valorPagar=cantidadNeumatico*valorNeumatico2
	FinSi	
FinProceso
