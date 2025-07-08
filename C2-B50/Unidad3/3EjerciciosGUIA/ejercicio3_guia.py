"""
Función que reciba un número entero y devuelva 
True si es par y False en caso contrario
"""
def leerNumero():
    return int(input("Ingresa un número entero: "))

def verificarParImpar(numero):
    return numero%2==0
    """
    if numero%2==0:
        return True
    else:
        return False
    """
#PP
#if verificarParImpar(leerNumero()) == True:
if verificarParImpar(leerNumero()):
    print("El número es PAR")
else:
    print("El número es IMPAR")

