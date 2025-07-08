"""
Dado un número, determinar
1) Si es > 0
2) Si es = 0
3) Si es < 0
"""
def leerNumero():
    return float(input("Ingresa un número: "))

def verificarNumero(numero):
    if numero > 0:
        return "El número es mayor a cero"
    elif numero < 0:
        return "El número es menor a cero"
    else:
        return "El número es igual a cero"

def leerRespuesta():
    return input("Desea continuar (S/N): ").upper()

def main():
    while True:
        print(verificarNumero(leerNumero()))
        if leerRespuesta()=="N":
            break
# PP
main()