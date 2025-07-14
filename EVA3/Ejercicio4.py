#4.	Función que reciba un número entero de máximo 10 dígitos (mayor que cero) 
# y lo devuelva invertido, por ejemplo, si recibe el 397, debe devolver el 793 

def ingresarNumero():
     while True:
        numero = int(input("Ingrese numero: "))
        if numero > 0 and numero  < 9999999999:
            return numero
        else:
            print("Número fuera de rango. Intente de nuevo.")

        
def invertirNumero(numero):
    numeroString = str(numero)
    numeroInvertido = ""
    for i in range(len(numeroString) - 1, -1, -1):
        numeroInvertido = numeroInvertido + numeroString[i]
    
    return int(numeroInvertido)

def main():
    numero = ingresarNumero()
    numeroInvertido= invertirNumero(numero)
    print(f"El número original es: {numero}")
    print("================")
    print(f"El número invertido es: {numeroInvertido} ")
    


##PP
main()